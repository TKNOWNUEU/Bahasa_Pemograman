## fungsi

def fungsi():
  print("selamat datang di function")

## Memanggil fungsi

def fungsi():
  print("selamat datang di function")

fungsi()


#scope
x = "di luar" #variabel x di luar fungsi

def scope(): #membuat fungsi
  print(x) #menggunakan variabel x di luar fungsi

scope() #memanggil fungsi


#global scope 
y = "y di luar" #variabel y di luar fungsi
x = "x di luar" #variabel x di luar fungsi
def globalscope():
  global y
  y = "y di dalam" #variabel y di dalam fungsi
  x = "x di dalam" #variabel x di dalam fungsi

globalscope() #memanggil fungsi
print (y) #menggunakan variabel y di luar fungsi
print (x) #menggunakan variabel x di luar fungsi



