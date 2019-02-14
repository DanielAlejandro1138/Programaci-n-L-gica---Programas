class Persona:
    def __init__(self,edad):
        self.edad = edad

    def hablar(self,mensaje):
        print (mensaje)

Daniel = Persona(24)
Cristy = Persona(23)

print ('Soy Daniel y tengo ', Daniel.edad)
print ('Soy Cristy y tengo ', Cristy.edad)

Daniel.hablar('Hola')
Cristy.hablar('Hola,Daniel!')


