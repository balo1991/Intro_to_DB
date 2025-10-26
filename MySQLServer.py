#!/usr/bin/python3
"""
Script to create the MySQL database 'alx_book_store'
If the database already exists, the script will not fail.
"""

import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL Server (edit user/password/host as needed)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password"  # <-- replace with your MySQL root password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create database if not exists
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Close connection properly
        if connection.is_connected():
            cursor.close()
            connection.close()
            # Optional confirmation
            # print("MySQL connection is closed")

if __name__ == "__main__":
    create_database()
