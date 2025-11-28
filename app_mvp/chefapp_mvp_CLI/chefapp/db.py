import sqlite3
from pathlib import Path

# Path to data/chefapp.db
DB_PATH = Path(__file__).resolve().parent.parent / "data" / "chefapp.db"

# Path to schema.sql in same directory as this file
SCHEMA_PATH = Path(__file__).resolve().parent / "schema.sql"


def get_connection():
    """Return a SQLite connection."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_database():
    """Load schema.sql and apply it."""
    conn = get_connection()

    # Load SQL from schema.sql
    with open(SCHEMA_PATH, "r") as f:
        sql = f.read()

    conn.executescript(sql)
    conn.commit()
    conn.close()

    print("Database initialized.")
