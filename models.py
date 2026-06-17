# models.py
import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "school.db")


def get_connection():
    return sqlite3.connect(DB_PATH, check_same_thread=False)


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    # Students table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        surname TEXT NOT NULL,
        class_name TEXT NOT NULL,
        age INTEGER NOT NULL
    )
    """)

    # Teachers table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS teachers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        surname TEXT NOT NULL,
        subject TEXT NOT NULL,
        age INTEGER NOT NULL
    )
    """)

    conn.commit()
    conn.close()