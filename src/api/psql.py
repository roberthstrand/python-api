from helpers import Task
import os
import psycopg2
from fastapi.responses import JSONResponse

conn = psycopg2.connect(
    host="localhost",
    port="49153",
    database="todo",
    user="postgres",
    password=os.getenv('PSQL_PASS'))

cur = conn.cursor()

def get_all():
  cur.execute("SELECT task_id, name, description, complete FROM tasks;")
  res = cur.fetchall()

  tasklist = list()
  for task in res:
    tasklist.append(Task(
      task_id = task[0],
      name = task[1],
      description = task[2],
      complete = task[3]))
  return tasklist

def get_task(task_id):
  cur.execute("SELECT * FROM tasks WHERE task_id='{0}';".format(str(task_id)))
  res = cur.fetchone()

  # If the result of the cursor execution is none,
  # return a 404 to user
  if res == None:
    return JSONResponse(status_code=404, content={"Error":"No task with that ID"})

  res = Task(
    task_id = res[0],
    name = res[1],
    description = res[2],
    complete = res[3]
  )
  return res

def new_task(item):
  cur.execute("""
  INSERT INTO tasks (name, description, complete)
  VALUES ('{0}', '{1}', '{2}');
  """.format(
    item.name,
    item.description,
    item.complete
    ))
  conn.commit()

def update_task(item):
  #TODO: Add check if item is valid, return error if not present
  cur.execute("""
  UPDATE tasks SET
  name = '{0}',
  description = '{1}',
  complete = '{2}'
  WHERE task_id = '{3}';
  """.format(
    item.name,
    item.description,
    item.complete,
    item.task_id
    ))
  conn.commit()

def delete_task(task_id):
  cur.execute("DELETE FROM tasks WHERE task_id={0};".format(str(task_id)))
  conn.commit()
