import sqlite3
import pandas as pd
from pathlib import Path

DB_PATH = Path("DATA/intelligence_platform.db")
DATA_DIR = Path("DATA")


def load_all_csv_data():
    """Loads and transforms all CSV files into the correct database tables"""

    if not DB_PATH.exists():
        print("Database not found! Run schema.py first.")
        return

    conn = sqlite3.connect(DB_PATH)

    # 1. Load Cyber Incidents
    print("Loading cyber_incidents.csv...")
    cyber_path = DATA_DIR / "cyber_incidents.csv"
    if cyber_path.exists():
        df_cyber = pd.read_csv(cyber_path)

        # Transform to match required schema
        df_cyber["title"] = df_cyber["description"].fillna("Untitled Incident")
        df_cyber["severity"] = df_cyber["severity"].replace({
            "Low": "Low", "Medium": "Medium", "High": "High", "Critical": "High"
        })  # High + Critical → High for simplicity
        df_cyber["status"] = df_cyber["status"].str.lower().replace({
            "open": "open",
            "in progress": "open",
            "resolved": "resolved",
            "closed": "resolved"
        })
        df_cyber["date"] = pd.to_datetime(df_cyber["timestamp"]).dt.strftime("%Y-%m-%d")

        # Select only needed columns
        cyber_clean = df_cyber[["title", "severity", "status", "date"]].copy()

        # Remove duplicates and load
        cyber_clean.drop_duplicates(subset=["title", "date"], inplace=True)
        cyber_clean.to_sql("cyber_incidents", conn, if_exists="append", index=False)
        print(f"Loaded {len(cyber_clean)} cyber incidents")
    else:
        print("cyber_incidents.csv not found!")

    # ==========================
    # 2. Load Datasets Metadata
    # ==========================
    print("Loading datasets_metadata.csv...")
    datasets_path = DATA_DIR / "datasets_metadata.csv"
    if datasets_path.exists():
        df_datasets = pd.read_csv(datasets_path)

        # Map columns
        df_datasets["name"] = df_datasets["name"]
        df_datasets["source"] = df_datasets["uploaded_by"]
        df_datasets["category"] = "Unknown"
        df_datasets["size"] = df_datasets["rows"] * df_datasets["columns"]  # estimated size

        datasets_clean = df_datasets[["name", "source", "category", "size"]]

        datasets_clean.to_sql("datasets_metadata", conn, if_exists="append", index=False)
        print(f"Loaded {len(datasets_clean)} datasets")
    else:
        print("datasets_metadata.csv not found!")

    # ========================
    # 3. Load IT Tickets
    # ========================
    print("Loading it_tickets.csv...")
    tickets_path = DATA_DIR / "it_tickets.csv"
    if tickets_path.exists():
        df_tickets = pd.read_csv(tickets_path)

        df_tickets["title"] = df_tickets["description"].fillna("No description")
        df_tickets["priority"] = df_tickets["priority"]
        df_tickets["status"] = df_tickets["status"].str.lower().replace({
            "resolved": "resolved",
            "open": "open",
            "in progress": "open",
            "waiting for user": "open"
        })
        df_tickets["created_date"] = pd.to_datetime(df_tickets["created_at"]).dt.strftime("%Y-%m-%d")

        tickets_clean = df_tickets[["title", "priority", "status", "created_date"]]

        tickets_clean.drop_duplicates(subset=["title"], inplace=True)
        tickets_clean.to_sql("it_tickets", conn, if_exists="append", index=False)
        print(f"Loaded {len(tickets_clean)} IT tickets")
    else:
        print("it_tickets.csv not found!")

    conn.close()
    print("\nALL DATA LOADED SUCCESSFULLY!")
    print("You are now ready for Week 9 Streamlit!")


if __name__ == "__main__":
    load_all_csv_data()