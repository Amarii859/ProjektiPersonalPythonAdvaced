import sqlite3

conn = sqlite3.connect("school.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    surname TEXT NOT NULL,
    class_name TEXT NOT NULL,
    age INTEGER NOT NULL
)
""")

conn.commit()

