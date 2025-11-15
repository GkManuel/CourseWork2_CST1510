import sqlite3
import pandas as pd
import bcrypt
from pathlib import Path

#Define paths
DATA_DIR = Path("DATA")
DB_PATH =DATA_DIR / "intelligence_platform.db"

#Create DATA folder if it doesn't exist
DATA_DIR.mkdir(parents=True, exist_ok=True)

#Helper function to get a database connection
def get_connection():
    """Returns a new SQLite connection to the intelligence platform DB.
     Caller must close it with conn.close()"""
    conn = sqlite3.connect(DB_PATH)
    return conn

if __name__ == "__main__":
    print("Imports successful!")
    print(f" DATA folder: {DATA_DIR.resolve()}")
    print(f" Database will be created at: {DB_PATH.resolve()}")