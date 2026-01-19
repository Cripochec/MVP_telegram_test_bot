CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    tg_id INTEGER UNIQUE,
    username TEXT,
    role TEXT DEFAULT 'user'
);