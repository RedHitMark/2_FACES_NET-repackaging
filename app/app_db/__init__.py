import mysql.connector
import os

def get_connection():
    connection = mysql.connector.connect(
        host=os.getenv("MYSQL_HOSTNANE"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE")
    )
    return connection
