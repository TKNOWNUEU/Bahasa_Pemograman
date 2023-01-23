from tkinter import *

tknown = Tk() 
tknown.title("Notebook GUI") # untuk membuat judul
tknown.geometry('400x500')   # untuk membuat ukuran


a = Label(tknown, text ="Tulis Catatan :") # untuk membuat label dengan tulisan "Tulis Catatan"
a.pack()

b = Text(tknown, height = 300, width = 300) # untuk membuat kotak teks
b.pack()


tknown.mainloop() # untuk menampilkan GUI