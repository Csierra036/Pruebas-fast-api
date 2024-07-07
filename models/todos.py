from pydantic import BaseModel
from typing import Optional

class Todo(BaseModel):
    name: str
    description: str
    completed: bool

class Person(BaseModel):
    name: str
    lastname: str
    email: Optional[str] = None #the campus is optional if the user not say notghing email is None(NULL)