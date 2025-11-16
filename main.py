#CST1500 Course Work 2
#Entry point for the Multi_Domain Intelligence Platform

from app.data.schema import create_all_tables

def main():
    print("Starting Multi-Domain Intelligence Platform")
    print("Initializing database and tables")

    #creating database and 4 tables
    create_all_tables()

    print("Setup complete")
    print("Database: DATA/intelligence_platform.db")

if __name__ == "__main__":
    main()