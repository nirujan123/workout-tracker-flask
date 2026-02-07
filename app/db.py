import sqlite3
from flask import current_app, g

def get_db():
    if not hasattr(g, "db"):
        g.db = sqlite3.connect(current_app.config["DATABASE"])
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    db = getattr(g, "db", None)
    if db is not None:
        db.close()

def init_db():
    db = get_db()
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS workouts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            exercise TEXT NOT NULL,
            sets INTEGER NOT NULL,
            reps INTEGER NOT NULL,
            weight REAL NOT NULL,
            created_at TEXT NOT NULL DEFAULT (datetime('now'))
        );
        """
    )
    db.commit()

def insert_workout(date, exercise, sets, reps, weight):
    db = get_db()
    db.execute(
        """
        INSERT INTO workouts (date, exercise, sets, reps, weight)
        VALUES (?, ?, ?, ?, ?);
        """,
        (date, exercise, sets, reps, weight)
    )
    db.commit()

def get_all_workouts():
    db = get_db()
    rows = db.execute(
        """
        SELECT id, date, exercise, sets, reps, weight, created_at
        FROM workouts
        ORDER BY date DESC, id DESC
        """
    ).fetchall()
    return rows
