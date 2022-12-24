jelaskan bagaimana cara mengakses fuction dan contohnya # Title: Meet 12 - Penggunaan fungsi
# Description: Meet 12 - fungsi

## fungsi

fungsi adalah sebuah blok kode yang hanya akan dijalankan saat ia dipanggil.

```python
def fungsi():
  print("selamat datang di function")
```

## Memanggil fungsi

Untuk memanggil function, gunakan nama function diikuti dengan tanda kurung.

```python

def fungsi():
  print("selamat datang di function")

fungsi()

```

## Argumen

Informasi dapat ditambahkan ke function melalui argumen. Argumen adalah nilai yang diberikan ke function saat ia dipanggil. Argumen berada di dalam tanda kurung diikuti dengan nama function.

```python

def nama(nama_depan):
  print(nama_depan + " Nama belakang")

nama("udin")

```
## Scope

Variabel yang didefinisikan di luar fungsi adalah variabel global, dan variabel yang didefinisikan di dalam fungsi adalah variabel lokal.

```python

x = "di luar"

def myfunc():
  print("cetak " + x)

myfunc()

```

## The global Keyword

Jika Anda ingin membuat perubahan pada variabel global dalam fungsi, gunakan kata kunci global.
supaya jika memanggil variabel yang sama di luar fungsi akan menghasilkan nilai yang sama.
agar tidak terjadi error, gunakan kata kunci global.

```python

x = "di luar"

def myfunc():
  global x #menggunakan global agar bisa mengubah variabel x di luar fungsi 
  x = "di dalam"

myfunc()

print("cetak " + x)

```
