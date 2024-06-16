import sqlite3

DATABASE_NAME = 'trip_booking.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn

def create_tables(conn):
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL
                )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS trips (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    destination TEXT NOT NULL,
                    date TEXT NOT NULL,
                    price REAL NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES users (id)
                )''')

    conn.commit()

def close_connection(conn):
    conn.close()
