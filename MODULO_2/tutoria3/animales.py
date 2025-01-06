'''### Ejercicio 2: Polimorfismo con animales
Crea una clase `Animal` con un método `hacer_sonido`.
Implementa dos clases derivadas, `Perro` y `Gato`, que sobrescriban este método.'''

from abc import ABC,abstractmethod

class Animal(ABC):

    @abstractmethod
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return f' Guau Guau '
    def sonido(self):
        return 'Guau guau'

class Gato(Animal):
    def hacer_sonido(self):
        return f' Miau Muau '


perro1=Perro()
gato1=Gato()
print(perro1.hacer_sonido())
print(perro1.sonido())
print(gato1.hacer_sonido())