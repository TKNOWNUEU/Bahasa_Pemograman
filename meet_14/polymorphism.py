# polimorfisme adalah kemampuan sebuah objek untuk memiliki banyak bentuk atau bentuk yang berbeda. 
# polimorfisme dapat terjadi karena adanya inheritance, dimana sebuah objek dapat memiliki bentuk yang berbeda
# karena adanya inheritance.

class DBD:
    def __init__(self,nama,perk,item):
        self.nama = nama
        self.perk = perk
        self.item = item
        

class david(DBD):
    def __init__(self,nama,perk,item):
        super().__init__(nama,perk,item)
    
    def special(self):
        print("setelah menggunakan dead hard, survivor akan mendapatkan efek kebal selama 0.5 detik")


class bill(DBD):
    def __init__(self,nama,perk,item):
        super().__init__(nama,perk,item)

    def special(self):
        print("dengan unbreakable, waktu untuk bangun dipercepat 35%")

class meg(DBD):
    def __init__(self,nama,perk,item):
        super().__init__(nama,perk,item)
    
    def special(self):
        print("saat sprint burst diaktifkan, movement speed menjadi 150% selama 3 detik")

class claudette(DBD):
    def __init__(self,nama,perk,item):
        super().__init__(nama,perk,item)
    
    def special(self):
        print("dengan self care, healing speed naik 35%, dan bisa heal tanpa item medkit")

survivor1 = david("david","dead hard","Alex's Toolbox")
survivor2 = bill("bill","unbreakable","Ranger Med-Kit")
survivor3 = meg("meg","sprint burst","Utility Flashlight")
survivor4 = claudette("claudette","self care","Rainbow Map")

print("nama =",survivor1.nama,"perk =", survivor1.perk, "item =", survivor1.item)
survivor1.special()
print("nama =",survivor2.nama,"perk =", survivor2.perk, "item =", survivor2.item)
survivor2.special()
print("nama =",survivor3.nama,"perk =", survivor3.perk, "item =", survivor3.item)
survivor3.special()
print("nama =",survivor4.nama,"perk =", survivor4.perk, "item =", survivor4.item)
survivor4.special()