from itertools import count

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field


app = FastAPI(title="Fullstack Demo API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


class TodoCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)


todos = [
    {"id": 1, "title": "Review FastAPI basics", "done": False},
    {"id": 2, "title": "Connect frontend to backend", "done": True},
]
next_id = count(start=3)


@app.get("/api/health")
def health():
    return {"status": "ok", "service": "fullstack-demo-api"}


@app.get("/api/todos")
def list_todos():
    return {"items": todos}


@app.post("/api/todos")
def create_todo(todo: TodoCreate):
    item = {"id": next(next_id), "title": todo.title.strip(), "done": False}
    todos.append(item)
    return {"message": "created", "item": item}


@app.patch("/api/todos/{todo_id}")
def toggle_todo(todo_id: int):
    for item in todos:
        if item["id"] == todo_id:
            item["done"] = not item["done"]
            return {"message": "updated", "item": item}
    raise HTTPException(status_code=404, detail="Todo not found")
