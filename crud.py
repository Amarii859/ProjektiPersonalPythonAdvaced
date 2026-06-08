from database import cursor, conn

def add_student(name, surname, class_name, age):
    cursor.execute("INSERT INTO students VALUES (NULL,?,?,?,?)",
                   (name, surname, class_name, age))
    conn.commit()

def get_students():
    cursor.execute("SELECT * FROM students")
    return cursor.fetchall()

def delete_student(id):
    cursor.execute("DELETE FROM students WHERE id=?", (id,))
    conn.commit()