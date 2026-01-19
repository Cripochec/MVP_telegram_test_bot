import sqlite3

DB_NAME = "bot.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    with get_connection() as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            tg_id INTEGER UNIQUE,
            username TEXT,
            role TEXT DEFAULT 'user'
        )
        """)

def add_user(tg_id: int, username: str, role: str):
    with get_connection() as conn:
        conn.execute(
            "INSERT OR IGNORE INTO users (tg_id, username, role) VALUES (?, ?, ?)",
            (tg_id, username, role)
        )

def get_user_role(tg_id: int) -> str | None:
    with get_connection() as conn:
        cur = conn.execute(
            "SELECT role FROM users WHERE tg_id = ?",
            (tg_id,)
        )
        row = cur.fetchone()
        return row[0] if row else None
