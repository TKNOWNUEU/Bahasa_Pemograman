import mysql.connector
import os

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="db_uas"
)


def insert_data(db):
    nama = input("Masukan nama: ")
    harga = input("Masukan harga: ")
    rasa = input("Masukan rasa: ")
    val = (nama, harga, rasa)
    cursor = db.cursor()
    sql = "INSERT INTO makanan (nama, harga, rasa) VALUES (%s, %s ,%s)"
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil disimpan".format(cursor.rowcount))


def show_data(db):
    cursor = db.cursor()
    sql = "SELECT * FROM makanan"
    cursor.execute(sql)
    results = cursor.fetchall()

    if cursor.rowcount < 0:
        print("Tidak ada data")
    else:
        for data in results:
            print(data)


def update_data(db):
    cursor = db.cursor()
    show_data(db)
    id = input("pilih id ")
    nama = input("Nama baru: ")
    harga = input("harga baru: ")
    rasa = input("rasa baru: ")

    sql = "UPDATE makanan SET nama=%s, harga=%s,rasa=%s WHERE id=%s"
    val = (nama, harga,rasa, id)
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil diubah".format(cursor.rowcount))


def delete_data(db):
    cursor = db.cursor()
    show_data(db)
    id = input("pilih id ")
    sql = "DELETE FROM makanan WHERE id=%s"
    val = (id,)
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil dihapus".format(cursor.rowcount))


def search_data(db):
    cursor = db.cursor()
    keyword = input("nama makanan: ")
    sql = "SELECT * FROM makanan WHERE nama LIKE %s OR harga LIKE %s"
    val = ("%{}%".format(keyword), "%{}%".format(keyword))
    cursor.execute(sql, val)
    results = cursor.fetchall()

    if cursor.rowcount < 0:
        print("Tidak ada data")
    else:
        for data in results:
            print(data)


def show_menu(db):
    print("=== APLIKASI DATABASE PYTHON ===")
    print("1. Insert Data")
    print("2. Tampilkan Data")
    print("3. Update Data")
    print("4. Hapus Data")
    print("5. Cari Data")
    print("0. Keluar")
    print("------------------")
    menu = input("Pilih menu> ")

    # clear screen
    os.system("clear")

    if menu == "1":
        insert_data(db)
    elif menu == "2":
        show_data(db)
    elif menu == "3":
        update_data(db)
    elif menu == "4":
        delete_data(db)
    elif menu == "5":
        search_data(db)
    elif menu == "0":
        exit()
    else:
        print("Menu salah!")


if __name__ == "__main__":
    while (True):
        show_menu(db)