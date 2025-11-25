from pathlib import Path
import sqlite3

#Path
CURRENT_FILE = Path(__file__).resolve()
PROJECT_ROOT = CURRENT_FILE.parent.parent.parent
DATA_DIR = PROJECT_ROOT / "DATA"
USERS_TXT = DATA_DIR / "users.txt"
DB_PATH = DATA_DIR / "intelligence_platform.db"


def migrate_users_from_file():
    #checks if users.txt file exists
    if not USERS_TXT.exists():
        print("users.txt not found, nothing to migrate")
        print(f"Expected: {USERS_TXT}")
        return

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    #reads the USERS.TXT file
    with open(USERS_TXT, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            username, password_hash = line.split(",", 1)

            # Skip if already exists
            cur.execute("SELECT 1 FROM users WHERE username = ?", (username,))
            if cur.fetchone():
                continue

            #adds new user to the database with default role of user
            cur.execute(
                "INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?)",
                (username, password_hash, "user")
            )

    conn.commit()
    conn.close()
    print("User migration completed successfully!")


if __name__ == "__main__":
    migrate_users_from_file()