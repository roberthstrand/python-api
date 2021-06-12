from fastapi import FastAPI
from helpers import Task
from psql import get_all, get_task, new_task, update_task, delete_task

app = FastAPI()

@app.get("/")
def read_root():
  res = get_all()
  return res

@app.get("/{task_id}")
def read_item(task_id: int):
  return get_task(task_id)

@app.put("/new")
def read_item(item: Task):
  return new_task(item)

@app.put("/update")
def read_item(item: Task):
  return update_task(item)

@app.post("/delete/{task_id}")
def read_item(task_id: int):
  return delete_task(task_id)