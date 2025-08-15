import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (adjust host/user/password to my setup)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",          # MySQL n ame
            password="Ethiopia_123"  # MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            # Optional: print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
