from database import cursor, conn

def add_student(name, surname, class_name, age):
    cursor.execute("""
        INSERT INTO students (name, surname, class_name, age)
        VALUES (?, ?, ?, ?)
    """, (name, surname, class_name, age))
    conn.commit()


def get_students():
    cursor.execute("SELECT * FROM students")
    return cursor.fetchall()


def delete_student(student_id):
    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()


def update_student(student_id, name, surname, class_name, age):
    cursor.execute("""
        UPDATE students
        SET name=?, surname=?, class_name=?, age=?
        WHERE id=?
    """, (name, surname, class_name, age, student_id))
    conn.commit()