# contoh cara coding sederhana
def tambah ():
    a = int(input("angka 1: "))
    b = int(input("angka 2: "))
    c = a+b
    print(c)

tambah()

def kurang ():
    a = int(input("angka 1: "))
    b = int(input("angka 2: "))
    c = a-b
    print(c)
kurang()

def pilihan ():
    print("1. tambah")
    print("2. kurang")
    print("exit")

while True:
    pilihan()
    pil=int(input("pilihan :"))
    if pil == 1:
        tambah()
    elif pil == 2:
        kurang()
    else :
        break
