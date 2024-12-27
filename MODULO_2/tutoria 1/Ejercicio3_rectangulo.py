'''3. Clase `Rectangulo`: Crea una clase `Rectangulo`
con: Atributos: `largo`, `ancho`. Métodos: `area` (calcula el área del rectángulo).
Ejemplo:
rect = Rectangulo(5, 4)
print(rect.area())  # Salida: 20'''

class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo=largo
        self.ancho=ancho
        area=0
    def area(self):
        area=self.largo*self.ancho
        print(area)

rectangulo1=Rectangulo(5,15)
rectangulo1.area()
