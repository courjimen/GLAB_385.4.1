import mysql.connector as mydbconnection
from mysql.connector import Error

#modular means it's easy to change and move around, plug and play, can stand alone
def connect():
    conn = None

    try:
        conn = mydbconnection.connect(
            database='usersdb',
            user='root',
            password='Orange47'
        )

        if conn.is_connected():
            print('✅ Connected to database')

        # Creates a cursor object that allows SQL actions to the MySQL server engine
        cursor = conn.cursor()

        # Create a SQL Query we want to run
        query = '''
            CREATE TABLE laptop (
                ID int(11) NOT NULL,
                Name varchar(250) NOT NULL,
                Price float NOT NULL,
                Purchase_Date date NOT NULL
            )
        '''

        cursor.execute(query)

        print('✅ Created Table')

    except Error as e:
        print(f'❌ Error: {e}')

    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('Connection Closed')

if __name__ == "__main__":
    connect()