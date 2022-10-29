#JELASKAN APA YANG DIMAKSUD DENGAN FUNCTION DALAM BAHASA PEMOGRAMAN DAN BERIKAN PENJELASAN PENGGUNAANNYA !

'''
function ada untuk mempermudah codingan 
dengan menggabungkan berbagai fungsi 
contohnya parameter string untuk function
'''
def game(tangan,nama):
    print(nama + ' memilih: ' + tangan + "\n")
game('Batu','Udin')

'''
{def game(tangan,nama):} 
    game : nama variabel fungsi
    tangan,nama : banyak parameter dalam variabel fungsi pisahkan dengan ,
    selanjutnya identasi (tab) dalam scope fungsi game 

    {print(nama + ' memilih: ' + tangan)}
    print sesuaikan dengan kalimat yang di inginkan

{game('Batu','Udin')}
memanggil function game  = game()
memberikan argument : 'batu' untuk parameter tangan 
memberikan argument : 'Udin' untuk parameter nama
'''
#function aritmatika
def aritmatika(nomor1,nomor2):
    a = int(3)
    b = int(5)
    c = a+b
    print(a,'ditambah',b,'=',c)
    d = nomor1 + nomor2
    print(nomor1,'ditambah',nomor2,'=',d,"\n")
aritmatika(1,5)

'''parameter juga bisa di isi dengan argument angka '''

#function tuple argument
def absen(*nama):
  print("absen ke 3 adalah " + nama[2]) #membaca array urutan ke  2 pada argument nama
absen("cahaya", "nur", "hikari ")
absen("yondaktawu", "udin", "mamat \n")

#nilai default dalam argument
def awal(tempat = "depok"):
    print("alien turun di " + tempat)
awal('mesir')
awal() #tidak diberi argument maka akan mengikuti argumen yang sudah di buat di parameter tempat
awal('atlantis')
