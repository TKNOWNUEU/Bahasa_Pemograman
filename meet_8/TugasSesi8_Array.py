'''
TUGAS. :
1. Jelaskan Apa yang dimkasud dengan Array penjelasan harus disertai dengan contoh
# array adalah kumpulan data yang memiliki tipe data yang sama
'''
import array as arr
angka = arr.array('i',[1,2,3]) 
print('LINE 8| print angka dengan import array')
print(angka,'\n')
###########################
print('LINE 11| menambah angka dengan append')
angka.append(4)
print(angka,'\n')
###########################
print('LINE 15| menambah angka dengan extend')
angka.extend([5])
print(angka,'\n')
###########################
print('LINE 19| menghapus angka dengan remove') #remove menghapus angka yang ada di dalam array
angka.remove(5)
print(angka,'\n')
###########################
print('LINE 23| menghapus index dengan pop') #pop menghapus index yang ada di dalam array
angka.pop(3)
print(angka,'\n')
###########################
print('LINE 27| print angka dengan satu indeks')
print(angka[0],'\n')
###########################
print ('LINE 30| print angka dari index 1 sampai 3')
print(angka[0:3]) 
print ('LINE 32| print angka dari index 1 sampai 2')
print(angka[:2])
print ('LINE 34| print angka dari index 2 sampai 3')
print(angka[1:3],'\n')
###########################
print('LINE 37| print angka menggunakan for')
for i in angka:
    print(i)
###########################
print('\nLINE 41| print angka dengan string urutan per angka')
for urutan in angka: 
    print ('angka ' + str(urutan))
print('\nLINE 44| print angka dengan enumerate urutan per indeks')
angka = [1,2,3]
for indeks,angka in enumerate(angka):
    print ('indeks ke',indeks,'angka =',angka) 
###########################
print('\nLINE 49| print angka dengan range') 
for angka in range(1,4): #range(nilai awal,nilai akhir)
    print (angka)
''' 
range karena python menggunakan formula array, 
yang mana indexnya adalah  0 = 1 jadi kalau nilai akhir akhir 3 akan terbaca indeks 1 sampai 2, 
karena pada nilai ke 1 = indeks 0
maka jika ingin output sampai 3 maka harus nilai akhir 4
'''