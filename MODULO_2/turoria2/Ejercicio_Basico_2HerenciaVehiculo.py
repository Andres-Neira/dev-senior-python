'''2. Herencia simple

- Ejercicio: Crea una clase `Vehiculo` con atributos `marca` y `modelo`.
Luego, crea una clase `Coche` que herede de `Vehiculo` y agrega un atributo `puertas`.  '''

class Vehiculo:

    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo

class Coche(Vehiculo):

    def __init__(self, marca, modelo, puertas):
        super().__init__( marca, modelo)
        self.puertas=puertas

carro1=Coche('renault', '94','4')

print(carro1.marca)
print(carro1.modelo)
print(carro1.puertas)
