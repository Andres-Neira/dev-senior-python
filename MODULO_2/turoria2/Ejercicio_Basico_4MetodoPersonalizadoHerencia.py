'''4. Herencia con método personalizado
- Ejercicio: Agrega un método `mostrar_info` a `Coche` para mostrar los detalles del vehículo.  '''


class Vehiculo:

    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo

class Coche(Vehiculo):

    def __init__(self, marca, modelo, puertas):
        super().__init__( marca, modelo)
        self.puertas=puertas
    
    def mostrarInformacion(self):
        return f' marca : {self.marca} modelo : {self.modelo} puertas : {self.puertas}'

carro1=Coche('renault', '94','4')

print(carro1.marca)
print(carro1.modelo)
print(carro1.puertas)
print(carro1.mostrarInformacion())