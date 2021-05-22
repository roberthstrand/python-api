import os
import hvac

# API stuff
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
vault = hvac.Client
vault = hvac.Client(
  url=os.environ['VAULT_ADDR'],
  token=os.environ['TOKE']
)

class Task(BaseModel):
  name: str
  description: str
  complete: Optional[bool] = None


@app.get("/")
def read_root():
  return {"Test": "OK!"}

@app.get("/{task_id}")
def read_item(task_id: int):
  return {"task_id": task_id}

@app.put("/{task_id}")
def update_item(task_id: int, item: Task):
  return {
  "task_id": task_id,
  "task": item.name,
  "description": item.description,
  "complete": item.complete
  }