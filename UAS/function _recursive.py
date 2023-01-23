'''function adalah sebuah blok kode yang dapat dipanggil berulang kali tanpa harus menulis ulang kode yang sama.
function dapat menerima parameter dan mengembalikan nilai.'''
def nama(nama_depan):
  print(nama_depan + " adalah nama depan")

nama("udin")
nama("susi")

'''recursive function adalah function yang memanggil dirinya sendiri contoh faktorial:  
4! = 4 * 3 * 2 * 1 = 24  
faktorial(n) = n * faktorial(n-1)
maksudnya dalah jika n = 4 maka faktorial(4) = 4 * faktorial(3) = 4 * 3 * faktorial(2) = 4 * 3 * 2 * faktorial(1) = 4 * 3 * 2 * 1 = 24
ia akan terus berulang sampai n = 0, maka faktorial(0) = 1 dan akan mengembalikan nilai 1 ke faktorial(1) = 1 * 1 = 1 
dan akan terus berulang sampai n = 4, maka faktorial(4) = 4 * 3 * 2 * 1 * 1 = 24'''
def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n-1)

print(faktorial(4))