class Persona:
  def __init__(self, _nombre, _edad, _saldo):
    self.nombre = _nombre
    self.edad = _edad
    self.saldo = _saldo

  def cumpleanhos(self):
    self.edad += 1

  def transferencia(self, persona2, monto):
    if self.saldo >= monto:
      self.saldo -= monto
      persona2.saldo += monto
      print("Transferencias")
    else:
      print("No se puede efectuar la transaccion")

  def __str__(self):
    return "Persona: " + self.nombre


p = Persona("Jose", 10, 4)
p2 = Persona("Pedro", 30, 10)
p2.transferencia(p, 7)

print("Saldo de p2: ")
print(p2.saldo)
print("Saldo de p1: ")
print(p.saldo)
