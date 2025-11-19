# CST1500 Course Work 2
# Entry point for the Multi-Domain Intelligence Platform

from app.data.schema import create_all_tables
import sqlite3
from pathlib import Path


def main():
    print("Starting Multi-Domain Intelligence Platform")
    print("Initializing database and tables")

    # Creating database and 4 tables
    create_all_tables()

    print("Setup complete")
    print("Database: DATA/intelligence_platform.db")
    print()

    # TEMPORARY: Show all migrated users (remove later if you want)
    print("CURRENT USERS IN DATABASE")
    print("-" * 50)

    DB_PATH = Path("DATA") / "intelligence_platform.db"
    try:
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute("SELECT id, username, role FROM users ORDER BY id")
        users = cur.fetchall()

        if users:
            for user in users:
                print(f"ID: {user[0]:2d} | Username: {user[1]:15s} | Role: {user[2]}")
        else:
            print("No users found – run user_service.py first!")

        conn.close()
    except sqlite3.Error as e:
        print(f"Database error: {e}")


if __name__ == "__main__":
    main()