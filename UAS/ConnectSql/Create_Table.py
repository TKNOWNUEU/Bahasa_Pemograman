import mysql.connector 

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_uas"
)

myconn=conn.cursor()
myconn.execute("CREATE TABLE Makanan (id INT AUTO_INCREMENT PRIMARY KEY, nama VARCHAR(255), harga INT(255), rasa VARCHAR(255))")

print("Table berhasil dibuat")
