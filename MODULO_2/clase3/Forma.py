from abc import ABC, abstractmethod

class Forma(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Circulo(Forma):
    
    def __init__(self, radio):
        self.radio = radio
        
    def area(self):
        return f"El área de un circulo es {3.14 * self.radio ** 2}"
    
    def perimetro(self):
        return f"El perimetro de un circulo es: {2 * 3.14 * self.radio}"
    
class Rectangulo(Forma):

    def __init__(self, base, altura):
        self.base=base
        self.altura=altura

    def area(self):
        return f'El area del rectangulo es {self.altura*self.base}'

    def perimetro(self):
        return f'El perimetro de un circulo es {2*self.base*self.altura}'

class cuadrado(Forma):

    def __init__(self,lado):
        self.lado=lado

    def area(self):
        return f'El area de un cuadrado es {self.lado*2}'


formas = [Circulo(5),
          Rectangulo(2, 10),
          cuadrado(8),
          Rectangulo(10, 20),
          Circulo(22)
]

for forma in formas:
    print(forma.area())
print('\n Perimetro de las formas')
#for forma in formas:
#    print(forma.perimetro())