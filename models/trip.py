import sqlite3

class Trip:
    def __init__(self, user_id, destination, date, price):
        self.id = None
        self.user_id = user_id
        self.destination = destination
        self.date = date
        self.price = price

    def create(self, conn):
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO trips (user_id, destination, date, price) VALUES (?, ?, ?, ?)",
                           (self.user_id, self.destination, self.date, self.price))
            self.id = cursor.lastrowid
            conn.commit()
            print(f"Trip created successfully: {self.destination}")
        except sqlite3.IntegrityError as e:
            conn.rollback() 
            print(f"Error: {e}")
        finally:
            pass  

    @classmethod
    def get_by_user_id(cls, conn, user_id):
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM trips WHERE user_id = ?", (user_id,))
        rows = cursor.fetchall()
        trips = []
        for row in rows:
            trip = cls(user_id=row[1], destination=row[2], date=row[3], price=row[4])
            trip.id = row[0]
            trips.append(trip)
        return trips
