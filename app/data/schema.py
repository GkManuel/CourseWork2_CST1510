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
       incident_id INTEGER,
       timestamp TEXT,
       severity TEXT NOT NULL,
       category TEXT,
       status TEXT,
       description TEXT       
    )
    """)

    #Datasets_table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS datasets_metadata (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        dataset_id INTEGER,
        name TEXT,
        rows INTEGER,
        columns INTEGER,
        uploaded_by TEXT,
        upload_date TEXT
    )
    """)

    #IT_tickets table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS it_tickets (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       ticket_id INTEGER,
       priority TEXT,
       description TEXT,
       status TEXT,
       assigned_to TEXT,
       created_at TEXT,
       resolution_time_hours INTEGER
    )
    """)

    conn.commit()
    conn.close()
    print("All tables created")