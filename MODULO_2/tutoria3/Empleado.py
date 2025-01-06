'''###Crea una clase base `Empleado` con un método `salario`.
Hereda las clases `TiempoCompleto` y `MedioTiempo`, sobrescribiendo el cálculo del salario.
'''

from abc import ABC, abstractmethod

class Empleado(ABC):

    def __init__(self, nombre):
        self.nombre=nombre
        self.salario=0

    @abstractmethod
    def calculoSalario(self):
        pass

class TiempoCompleto(Empleado):
    def __init__(self, nombre):
        super().__init__(nombre)

    def calculoSalario(self):
        self.salario=40000*8
        return f'El salario de {self.nombre} es {self.salario}'

class MedioTiempo(Empleado):
    def __init__(self, nombre,horas):
        super().__init__(nombre)
        self.horas=horas

    def calculoSalario(self):
        self.salario=40000*self.horas
        return f'El salario de {self.nombre} es {self.salario}'

empleado1=TiempoCompleto('Andres')
empleado2=MedioTiempo('Camilo',5)
print(empleado1.calculoSalario())
print(empleado2.calculoSalario())