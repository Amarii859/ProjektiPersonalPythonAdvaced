from fastapi import FastAPI
from projekt.crud import get_students

app = FastAPI()

@app.get("/students")
def read_students():
    return get_students()

