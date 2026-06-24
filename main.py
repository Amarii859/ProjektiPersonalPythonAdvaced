
from fastapi import FastAPI
from schemas import Student
from crud import (
    get_students,
    add_student,
    update_student,
    delete_student
)

app = FastAPI()


# GET all students
@app.get("/students")
def read_students():
    return get_students()


# POST student
@app.post("/students")
def create_student(student: Student):
    add_student(
        student.name,
        student.surname,
        student.class_name,
        student.age
    )
    return {"message": "Student added successfully"}


# PUT student
@app.put("/students/{student_id}")
def edit_student(student_id: int, student: Student):
    update_student(
        student_id,
        student.name,
        student.surname,
        student.class_name,
        student.age
    )
    return {"message": "Student updated successfully"}


# DELETE student
@app.delete("/students/{student_id}")
def remove_student(student_id: int):
    delete_student(student_id)
    return {"message": "Student deleted successfully"}
