
import mysql.connector
import psycopg2
import sqlite3
class Main:
    """main程序"""
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root" ,
        passwd = "",
        database = "blood_alcohol"
    )

    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE IF NOT EXISTS blood_alcohol_content")
    results = mycursor.fetchall()

    for row in results :
        print(row)

    mydb.close()