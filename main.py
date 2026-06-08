from fastapi import FastAPI
from crud import add_student, get_students

app = FastAPI()

@app.get("/students")
def read_students():
    return get_students()