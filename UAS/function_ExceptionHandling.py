''' exception handling terdiri dari 3 bagian: 
1. try: adalah bagian yang akan di coba untuk dijalankan, jika tidak ada error maka akan di lanjutkan ke bagian else
2. except: adalah bagian yang akan di jalankan jika terjadi error pada bagian try
3. else: adalah bagian yang akan di jalankan jika tidak terjadi error pada bagian try
exception handling juga dapat digunakan untuk menangani error yang terjadi pada function kita, contoh:'''
def pertambahan(a, b):
    try:
        hasil = a + b
    except TypeError: 
        print("Tidak bisa menambahkan string dengan integer")
    else:
        print(hasil)

pertambahan("10", 2)
pertambahan("satu", 0)
pertambahan(10, 2)

''' exception handling TypeError adalah error yang terjadi jika kita mencoba untuk menjumlahkan string dengan integer,
jadi kita bisa menangani error tersebut dengan cara seperti di atas.
exception masih banyak lagi, untuk lebih lengkapnya bisa dilihat di https://docs.python.org/3/library/exceptions.html'''