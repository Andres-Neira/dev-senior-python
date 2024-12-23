class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca=marca
        self.mouesdelo=modelo

    def descripcion(self):
        return f'El vehiculo es de marca {self.marca}'

class Auto(Vehiculo):

    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas=puertas

    def descripcion(self):
        return f'El vehiculo es de marca {self.marca}, modelo {self.mouesdelo} y tiene {self.puertas}'

mi_auto = Auto('Chevrolet', 'Sedan' , 4)
print(mi_auto.descripcion())

