import sqlite3

class User:
    def __init__(self, username: str, password: str):
        self.id = None
        self.username = username
        self.password = password

    def create(self, conn):
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (self.username, self.password))
            self.id = cursor.lastrowid
            conn.commit()
            print(f"User created successfully: {self.username}")
        except sqlite3.IntegrityError:
            print(f"Error: User '{self.username}' already exists.")
        finally:
            pass

    @classmethod
    def get_by_username(cls, conn, username: str):
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        row = cursor.fetchone()
        if row:
            return cls(username=row[1], password=row[2])
        return None
