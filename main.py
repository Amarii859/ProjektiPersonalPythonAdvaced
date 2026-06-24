from fastapi import FastAPI
from crud import (
    get_students,
    add_student,
    update_student,
    delete_student
)

app = FastAPI()


@app.get("/students")
def read_students():
    return get_students()


@app.post("/students")
def create_student(
    name: str,
    surname: str,
    class_name: str,
    age: int
):
    add_student(name, surname, class_name, age)
    return {"message": "Student added"}


@app.put("/students/{student_id}")
def edit_student(
    student_id: int,
    name: str,
    surname: str,
    class_name: str,
    age: int
):
    update_student(
        student_id,
        name,
        surname,
        class_name,
        age
    )
    return {"message": "Student updated"}


@app.delete("/students/{student_id}")
def remove_student(student_id: int):
    delete_student(student_id)
    return {"message": "Student deleted"}

