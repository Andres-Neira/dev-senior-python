from abc import ABC, abstractmethod
class FigurasGeometricas(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimetro(self):
        pass

class Circulo(FigurasGeometricas):
    def __init__(self,radio):
        self.radio = radio
    
    def ver_radio(self):
        return self.radio
    
    def area(self):
        return 2*3.1416*self.radio**2
    def perimetro(self):
        return 2*3.1416*self.radio

mi_ciruculo=Circulo(4)
print(mi_ciruculo.ver_radio())
print(mi_ciruculo.area())
print(mi_ciruculo.perimetro())