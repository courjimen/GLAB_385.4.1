import mysql.connector as mydbconnection
from mysql.connector import Error

#modular means it's easy to change and move around, plug and play, can stand alone
def insert_record(id, name, price, date):
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

#create a record tuple/variable took function parameters and made a tuple
        record = (id, name, price, date)

        # Create a SQL Query we want to run
        # replace values with %s to use parameterized values
        query = '''
            INSERT INTO laptop (ID, Name, Price, Purchase_Date)
                VALUES(%s, %s, %s, %s)
        '''
        # Execute the query in SQL engine/server
        cursor.execute(query, record) # call record here to execute
        print('✅ Query Executed')

        # Have to commit the query to actually send the data/table update
        conn.commit()
        print('✅ Transaction Committed')

        print(f'{cursor.rowcount}: Record inserted successfully 🎉')

    except Error as e:
        print(f'❌ Error: {e}')

    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('Connection Closed')

# call the function and run this to insert new data/variables into the table
insert_record(1, 'Mac Book Pro', 3000, '2026-07-18')
insert_record(12, 'Lenovo Think Pad', 1400, '2025-12-25')
insert_record(9, 'Alienware', 5000, '2026-09-16')
