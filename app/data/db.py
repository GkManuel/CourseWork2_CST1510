import sqlite3
from pathlib import Path

# Points to the DATA folder in project root – correct location
DB_PATH = Path(__file__).resolve().parent.parent.parent / "DATA" / "intelligence_platform.db"

def get_connection():
    """Returns a SQLite connection with dictionary-style rows (row['username'])"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn