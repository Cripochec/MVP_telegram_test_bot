import sqlite3
import os

DB_NAME = "bot.db"
MIGRATIONS_DIR = "migrations"

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_migrations_table(conn):
    conn.execute("""
    CREATE TABLE IF NOT EXISTS migrations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT UNIQUE
    )
    """)

def applied_migrations(conn):
    cur = conn.execute("SELECT filename FROM migrations")
    return {row[0] for row in cur.fetchall()}

def apply_migration(conn, filename):
    with open(os.path.join(MIGRATIONS_DIR, filename), "r", encoding="utf-8") as f:
        sql = f.read()
        conn.executescript(sql)
        conn.execute(
            "INSERT INTO migrations (filename) VALUES (?)",
            (filename,)
        )

def migrate():
    conn = get_connection()
    init_migrations_table(conn)

    applied = applied_migrations(conn)
    files = sorted(os.listdir(MIGRATIONS_DIR))

    for file in files:
        if file not in applied:
            print(f"Applying migration: {file}")
            apply_migration(conn, file)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    migrate()
