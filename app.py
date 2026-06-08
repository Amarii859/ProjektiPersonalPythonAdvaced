import streamlit as st
from crud import add_student, get_students

st.title("School Management System")

menu = st.sidebar.selectbox("Menu", ["Add Student", "View Students"])

if menu == "Add Student":
    name = st.text_input("Name")
    surname = st.text_input("Surname")
    class_name = st.text_input("Class")
    age = st.number_input("Age")

    if st.button("Add"):
        add_student(name, surname, class_name, age)
        st.success("Student added!")

elif menu == "View Students":
    students = get_students()
    for s in students:
        st.write(s)