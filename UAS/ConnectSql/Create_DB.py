import mysql.connector 

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

myconn=conn.cursor()
myconn.execute("CREATE DATABASE db_uas")

print("Database berhasil dibuat")