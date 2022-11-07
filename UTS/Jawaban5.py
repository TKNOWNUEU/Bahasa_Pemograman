def menu():
    print("Pilihan")
    print("20210801149")
    print("Teddy Adi Kusuma")
    print("1. capucino")
    print("2. teh")
    print("3. Exit")
    pilihan = int(input("Masukkan pilihan anda : "))
    if pilihan == 1:
        print("Anda memilih capucino")
        harga = int(input("Masukkan harga : "))
        hargatotal = harga + (harga * 10/100) 
        ppn = harga * 10 / 100
        
        print("harga total yang harus dibayar :", hargatotal, "\ndengan ppn sebesar :", ppn)
        menu()
    elif pilihan == 2:
        print("Anda memilih teh")
        harga = int(input("Masukkan harga : "))
        hargatotal = harga + (harga * 10/100)
        ppn = harga * 10 / 100
        print("harga total yang harus dibayar :", hargatotal, "\ndengan ppn sebesar :", ppn)
        menu()
    elif pilihan == 3:
        print("Anda memilih exit")
    else:
        print("Pilihan tidak ada")
        menu()
menu()