from flask import Flask, jsonify, render_template


app = Flask(__name__)


@app.route("/")
def home():
    learning_goals = [
        "Understand how Flask starts a web app.",
        "Know what a route does.",
        "Render a template with Python data.",
    ]
    return render_template("index.html", learning_goals=learning_goals)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/api/status")
def status():
    return jsonify(
        {
            "project": "minimal-flask-site",
            "status": "ok",
            "message": "Your first Flask app is running.",
        }
    )


if __name__ == "__main__":
    app.run(debug=True)
