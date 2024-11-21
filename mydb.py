import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'sql123'
)

# Cursor Object
cursorObject = dataBase.cursor()

# Create Database
cursorObject.execute("CREATE DATABASE elderco")

print("All Done!")