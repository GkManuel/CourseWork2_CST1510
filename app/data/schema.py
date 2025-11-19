import sqlite3
from pathlib import Path

DB_PATH = Path("DATA/intelligence_platform.db")

def create_all_tables():
    """Creates all tables"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    #users_table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       username TEXT NOT NULL UNIQUE,
       password_hash TEXT NOT NULL,
       role TEXT DEFAULT 'user'
    )    
    """)

    #cyber_incidents_table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cyber_incidents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            severity TEXT NOT NULL,
            status TEXT DEFAULT 'open',
            date TEXT       
    )
    """)

    #Datasets_table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS datasets_metadata (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            source TEXT,
            category TEXT,
            size INTEGER
    )
    """)

    #IT_tickets table
    cursor.execute("""
   CREATE TABLE IF NOT EXISTS it_tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            priority TEXT NOT NULL,
            status TEXT DEFAULT 'open',
            created_date TEXT
    )
    """)

    conn.commit()
    conn.close()
    print("All tables created")