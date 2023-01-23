import mysql.connector 

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_uas"
)

myconn=conn.cursor()
sql = "INSERT INTO Makanan (nama, harga, rasa) VALUES (%s, %s, %s)"
val = ("Nasi Goreng", 10000, "Pedas")
myconn.execute(sql, val)

conn.commit()

print("{} data ditambahkan".format(myconn.rowcount))