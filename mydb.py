import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ab@08035958219",
)
cursor_object = mydb.cursor()

cursor_object.execute("CREATE DATABASE CRMdb_new")
print("Database created successfully")
