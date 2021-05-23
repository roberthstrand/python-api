from pydantic import BaseModel
from typing import Optional

class Task(BaseModel):
  task_id: int = None
  name: str
  description: Optional[str] = ""
  complete: Optional[bool] = False