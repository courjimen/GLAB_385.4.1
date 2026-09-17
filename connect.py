import mysql.connector as mydbconnection
from mysql.connector import Error
from dotenv import load_dotenv
import os

load_dotenv()

#modular means it's easy to change and move around, plug and play, can stand alone
def connect():
    conn = None

    password = os.getenv('password')

    try:
        conn = mydbconnection.connect(
            database='usersdb',
            user='root',
            password=password
        )

        if conn.is_connected():
            print('✅ Connected to database')

    except Error as e:
        print(f'❌ Error: {e}')

    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('Connection Closed')

if __name__ == "__main__":
    connect()