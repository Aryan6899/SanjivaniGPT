from pathlib import Path
import sqlite3

BASE_DIR = Path(__file__).resolve().parents[2]
DB_PATH = BASE_DIR / "data" / "sanjivani.db"
DB_PATH.parent.mkdir(parents=True, exist_ok=True)


def get_connection():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    connection = get_connection()
    try:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS departments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                code TEXT NOT NULL UNIQUE,
                name TEXT NOT NULL UNIQUE
            )
        """)
        connection.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                prn TEXT NOT NULL UNIQUE,
                email TEXT NOT NULL UNIQUE,
                name TEXT NOT NULL,
                department_id INTEGER NOT NULL,
                year INTEGER,
                division TEXT,
                role TEXT NOT NULL DEFAULT 'student',
                FOREIGN KEY (department_id) REFERENCES departments(id)
            )
        """)
        connection.commit()
    finally:
        connection.close()


def seed_demo_data():
    connection = get_connection()
    try:
        connection.executemany(
            "INSERT OR IGNORE INTO departments (code, name) VALUES (?, ?)",
            [
                ("AIML", "Artificial Intelligence and Machine Learning"),
                ("CSE", "Computer Science and Engineering"),
                ("AIDS", "Artificial Intelligence and Data Science"),
            ],
        )
        aiml_id = connection.execute(
            "SELECT id FROM departments WHERE code = 'AIML'"
        ).fetchone()[0]
        connection.execute(
            """INSERT OR IGNORE INTO students
               (prn, email, name, department_id, year, division, role)
               VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (
                "DEMO-PRN-001",
                "demo.student@sanjivani.edu.in",
                "Demo Student",
                aiml_id,
                2,
                "A",
                "student",
            ),
        )
        connection.commit()
    finally:
        connection.close()
