
from pydantic import BaseModel

class Student(BaseModel):
    name: str
    surname: str
    class_name: str
    age: int