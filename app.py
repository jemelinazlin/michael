# app.py

import sqlite3
from database.connection import get_db_connection, create_tables, close_connection
from models.user import User
from models.trip import Trip

def main():
    conn = get_db_connection()  # Establish a connection to your SQLite database

    create_tables(conn)  # Create tables if they don't exist

    while True:
        print("\nMenu:")
        print("1. Sign up")
        print("2. Book trip")
        print("3. View trips")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            user = User(username=username, password=password)
            user.create(conn)  # Create the user
            print(f"User created successfully: {username}")

        elif choice == "2":
            username = input("Enter username: ")
            user = User.get_by_username(conn, username)  # Retrieve the user
            if user:
                destination = input("Enter destination: ")
                date = input("Enter date (YYYY-MM-DD): ")
                price = float(input("Enter price: "))
                trip = Trip(user_id=user.id, destination=destination, date=date, price=price)
                trip.create(conn)  # Attempt to create the trip
            else:
                print(f"User not found: {username}")

        elif choice == "3":
            username = input("Enter username: ")
            user = User.get_by_username(conn, username)  # Retrieve the user
            if user:
                trips = Trip.get_by_user_id(conn, user.id)  # Retrieve trips for the user
                if trips:
                    print(f"Trips for user {username}:")
                    for trip in trips:
                        print(f"  - Trip to {trip.destination} on {trip.date} for ${trip.price:.2f}!")
                else:
                    print(f"No trips found for user {username}")
            else:
                print(f"User not found: {username}")

        elif choice == "4":
            print("Exiting...")
            close_connection(conn) 
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
