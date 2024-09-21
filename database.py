import sqlite3

# DATABASE CONNECTION AND TABLE CREATION
def connect_db():
    conn = sqlite3.connect('logs.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS records (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   date TEXT NOT NULL,
                   description TEXT NOT NULL
    )
    ''')
    conn.commit()
    return conn, cursor

# Function to add a record
def add_record(cursor, name, date, description):
    cursor.execute('INSERT INTO records (name, date, description) VALUES (?, ?, ?)', (name, date, description))
    
# Function to fetch all records
def fetch_records(cursor):
    cursor.execute('SELECT * FROM records')
    return cursor.fetchall()

# Function to delete a record
def delete_record(cursor, record_id):
    cursor.execute('DELETE FROM records WHERE id= ?', (record_id,))
    
