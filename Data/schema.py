import sqlite3
conn = sqlite3.connect('cyber_incidents.db')
def create_cyber_incidents_table(conn):
    """
    Creates the cyber incidents table if doesn't exist
       Required columns:
    - id: INTEGER PRIMARY KEY AUTOINCREMENT
    - date: TEXT (format: YYYY-MM-DD)
    - incident_type: TEXT (e.g., 'Phishing', 'Malware', 'DDoS')
    - severity: TEXT (e.g., 'Critical', 'High', 'Medium', 'Low')
    - status: TEXT (e.g., 'Open', 'Investigating', 'Resolved', 'Closed')
    - description: TEXT
    - reported_by: TEXT (username of reporter)
    - created_at: TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    """
    cursor = conn.cursor()
    create_cyber_incidents = """CREATE TABLE IF NOT EXISTS cyber_incidents (
id INTEGER PRIMARY KEY AUTOINCREMENT,
date TEXT,
incident_type TEXT severity TEXT, 
status TEXT, 
description TEXT,
reported_by TEXT, 
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)"""
    cursor.execute(create_cyber_incidents)
    conn.commit()
    print("Cyber incidents table created successfully")

create_cyber_incidents_table(conn)