# inheritance adalah pewarisan class yang memungkinkan kita untuk mendefinisikan sebuah class 
# yang mewarisi semua metode dan properti dari parent classnya.
# dengan inheritance kita bisa membuat class baru yang memiliki semua metode dan properti dari class lainnya.
# tanpa harus menulis ulang semua metode dan properti yang sudah ada di class lainnya.
class DBD:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Player(DBD):
  def __init__(self, fname, lname, item):
    super().__init__(fname, lname)
    self.item = item

  def player(self):
    print("player", self.firstname, self.lastname, "membawa", self.item)


class Killer(Player):
  pass

  def player(self):
    print("player", self.firstname, self.lastname, "membawa", self.item, "dan akan membunuhmu")

x = Player("david", "king", "Commodious Toolbox")
y = Killer("michael", "myers", "knife")

x.player()
y.player()
