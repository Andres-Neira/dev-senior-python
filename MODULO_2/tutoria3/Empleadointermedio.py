'''### Ejercicio 1: Sistema de manejo de empleados
Crea un sistema que calcule el bono anual de empleados basado en su tipo.
Define una clase abstracta Empleado con un método abstracto calcular_bono.
Implementa clases concretas Gerente, Desarrollador y Asistente, donde cada clase tenga su propia fórmula para calcular el bono.
'''

from abc import ABC, abstractmethod

class Empleado(ABC):

    @abstractmethod
    def calcular_bono(self):
        pass

class Gerente(Empleado):

    def calcular_bono(self):
        bono=50000000*0.1
        return f' El bono es de ${bono} de un salario de $50000000 para gerente'

class Desarrollador(Empleado):

    def calcular_bono(self):
        bono=5000000*0.08
        return f' El bono es de ${bono} de un salario de $5000000 para desarrollador'

class Asistente(Empleado):

    def calcular_bono(self):
        bono=500000*0.05
        return f' El bono es de ${bono} de un salario de $500000 para asistente'

andres=Gerente()
camilo=Desarrollador()
felipe=Asistente()

print(andres.calcular_bono())
print(camilo.calcular_bono())
print(felipe.calcular_bono())