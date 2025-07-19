import mysql.connector
from mysql.connector import Error

def get_connection():
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            password="swetha4106#",
            database="hrms_portal"
        )
        return connection
    except Error as e:
        print("Error while connecting to MySQL", e)
        return None
get_connection()
