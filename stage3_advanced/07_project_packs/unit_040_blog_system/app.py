import sqlite3
from datetime import datetime
from pathlib import Path

from flask import Flask, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash


BASE_DIR = Path(__file__).resolve().parent
DATABASE = BASE_DIR / "blog.db"

app = Flask(__name__)
app.config["SECRET_KEY"] = "change-me-before-real-deploy"
app.config["DATABASE"] = DATABASE


def get_db() -> sqlite3.Connection:
    if "db" not in g:
        g.db = sqlite3.connect(app.config["DATABASE"])
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(_error) -> None:
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db() -> None:
    db = get_db()
    db.executescript(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TEXT NOT NULL,
            author_id INTEGER NOT NULL,
            FOREIGN KEY (author_id) REFERENCES users (id)
        );
        """
    )
    db.commit()


def get_current_user():
    user_id = session.get("user_id")
    if user_id is None:
        return None

    db = get_db()
    return db.execute("SELECT id, username FROM users WHERE id = ?", (user_id,)).fetchone()


@app.context_processor
def inject_user():
    return {"current_user": get_current_user()}


@app.route("/")
def index():
    db = get_db()
    posts = db.execute(
        """
        SELECT posts.id, posts.title, posts.content, posts.created_at, users.username
        FROM posts
        JOIN users ON users.id = posts.author_id
        ORDER BY posts.id DESC
        """
    ).fetchall()
    return render_template("index.html", posts=posts)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"].strip()

        if not username or not password:
            flash("Username and password are required.")
            return render_template("register.html")

        db = get_db()
        existing = db.execute("SELECT id FROM users WHERE username = ?", (username,)).fetchone()
        if existing is not None:
            flash("This username already exists.")
            return render_template("register.html")

        db.execute(
            "INSERT INTO users (username, password_hash) VALUES (?, ?)",
            (username, generate_password_hash(password)),
        )
        db.commit()
        flash("Register success. Please login.")
        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"].strip()

        db = get_db()
        user = db.execute(
            "SELECT id, username, password_hash FROM users WHERE username = ?",
            (username,),
        ).fetchone()

        if user is None or not check_password_hash(user["password_hash"], password):
            flash("Wrong username or password.")
            return render_template("login.html")

        session.clear()
        session["user_id"] = user["id"]
        flash("Login success.")
        return redirect(url_for("index"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    flash("You are logged out.")
    return redirect(url_for("index"))


@app.route("/new", methods=["GET", "POST"])
def new_post():
    user = get_current_user()
    if user is None:
        flash("Please login before creating a post.")
        return redirect(url_for("login"))

    if request.method == "POST":
        title = request.form["title"].strip()
        content = request.form["content"].strip()

        if not title or not content:
            flash("Title and content are required.")
            return render_template("new_post.html")

        db = get_db()
        db.execute(
            """
            INSERT INTO posts (title, content, created_at, author_id)
            VALUES (?, ?, ?, ?)
            """,
            (title, content, datetime.now().strftime("%Y-%m-%d %H:%M"), user["id"]),
        )
        db.commit()
        flash("Post created.")
        return redirect(url_for("index"))

    return render_template("new_post.html")


with app.app_context():
    init_db()


if __name__ == "__main__":
    app.run(debug=True)
