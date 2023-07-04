import sqlite3
from sqlite3 import Error


def create_connection(path):
    connection = create_connection("E:\\sm_app.sqlite")
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection
