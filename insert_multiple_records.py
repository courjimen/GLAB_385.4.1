import mysql.connector as mydbconnection
from mysql.connector import Error


# modular means it's easy to change and move around, plug and play, can stand alone
def connect():
    conn = None

    try:
        conn = mydbconnection.connect(
            database="usersdb", user="root", password="Orange47"
        )

        if conn.is_connected():
            print("✅ Connected to database")

        # Creates a cursor object that allows SQL actions to the MySQL server engine
        cursor = conn.cursor()

        records_to_insert = [
            (4, "HP Pavilion Power", 1999, "2019-01-11"),
            (5, "MSI WS75 9TL-496", 5799, "2019-02-27"),
            (6, "Microsoft Surface", 2330, "2019-07-23")
        ]

        # Create a SQL Query we want to run and insert p
        query = """
            INSERT INTO laptop (ID, Name, Price, Purchase_Date)
                VALUES(%s, %s, %s, %s)
        """
        # Execute the query in SQL engine/server
        cursor.executemany(query, records_to_insert) # added many for multiple and calling the function 
        print("✅ Query Executed")

        # Have to commit the query to actually send the data/table update
        conn.commit()
        print("✅ Transaction Committed")

        print(f"{cursor.rowcount}: Record inserted successfully 🎉")

    except Error as e:
        print(f"❌ Error: {e}")

    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print("Connection Closed")


if __name__ == "__main__":
    connect()
