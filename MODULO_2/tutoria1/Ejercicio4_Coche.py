'''4. Clase `Coche`: Crea una clase `Coche` con los atributos: Marca y Modelo. 
Incluye un método `arrancar` que imprima:  `
"El coche [Marca] modelo [Modelo] está arrancando."`'''

class Coche:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def arrancar(self):
        return f' El coche {self.marca} modelo {self.modelo} esta arrancando'

coche1=Coche('renault', 'Sprint')
print(coche1.arrancar())