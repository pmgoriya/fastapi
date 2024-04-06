import sqlite3

def create_connection():
    conn = sqlite3.connect('test.db')
    return conn

def create_tables(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS farmers (
                        id INTEGER PRIMARY KEY,
                        Name TEXT NOT NULL,
                        Annual_Income INTEGER,
                        Contact INTEGER UNIQUE,
                        land INTEGER,
                        gender TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY,
                        email TEXT UNIQUE,
                        password TEXT,
                        role TEXT NOT NULL)''')
    conn.commit()
