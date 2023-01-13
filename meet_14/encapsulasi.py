#variable private adalah variabel yang tidak bisa di akses dari luar class
#self.__nama = "nama" 
#variable protected adalah variabel yang bisa di akses dari subclass
#self._nama = "nama"

class BDB:

    def __init__(self, nama,token,perk):
        self.__nama = nama
        self.__token = token
        self.__perk = perk
    
    #getter untuk mengambil nilai dari private variabel
    def getNama(self):
        return self.__nama
    def gettoken(self):
        return self.__token
    def getperk(self):
        return self.__perk
    
    #setter untuk mengubah nilai dari private variabel
    def hitSurvivor(self,hit):
        self.__token += hit
        print("killer memukul survivor")
        
    def hitObsession(self,miss):
        self.__token -= miss
        print("killer memukul obsession")
    
killer = BDB("Michael Myers",1,"save the best for last")

print(killer.getNama(), killer.gettoken(), killer.getperk())
killer.hitSurvivor(1)
print(killer.getNama(), killer.gettoken(), killer.getperk())
killer.hitObsession(1)
print(killer.getNama(), killer.gettoken(), killer.getperk())


