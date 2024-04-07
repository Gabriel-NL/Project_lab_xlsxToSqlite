import sqlite3

def create_table(conn):
    # Create table if not exists
    conn.execute('''CREATE TABLE IF NOT EXISTS data
                    (Name TEXT, Year INTEGER, Value REAL)''')

def check_columns(conn):
    cursor = conn.execute("PRAGMA table_info(data)")
    columns = [row[1] for row in cursor.fetchall()]
    return "Name" in columns and "Year" in columns and "Value" in columns

def insert_dummy_data(conn):
    # Insert dummy data
    dummy_data = [("John", 2000, 100.5),
                  ("Alice", 2001, 200.3),
                  ("Bob", 2002, 150.7),
                  ("Emma", 2003, 300.2),
                  ("James", 2004, 250.6),
                  ("Sophia", 2005, 180.4),
                  ("William", 2006, 220.8),
                  ("Olivia", 2007, 280.9),
                  ("Liam", 2008, 190.1),
                  ("Charlotte", 2009, 210.0)]
    conn.executemany("INSERT INTO data VALUES (?, ?, ?)", dummy_data)

def main():
    # Connect to SQLite database
    conn = sqlite3.connect('database.sqlite')

    # Create table if not exists
    create_table(conn)

    # Check if table has required columns
    if not check_columns(conn):
        print("Adding missing columns 'Name', 'Year', 'Value'")
        # Drop and recreate table with required columns
        conn.execute('''DROP TABLE data''')
        create_table(conn)

    # Insert dummy data
    insert_dummy_data(conn)

    # Commit changes and close connection
    conn.commit()
    conn.close()
    print("Dummy data inserted successfully.")

if __name__ == "__main__":
    main()
