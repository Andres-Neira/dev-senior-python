'''2. Herencia: Clase `Vehiculo` y `Moto`:
Crea una clase base `Vehiculo` con los atributos: Tipo y Marca.
Crea una subclase `Moto` que herede de `Vehiculo
y tenga un método `hacer_wheelie` que imprima:  `"¡La moto [Marca] está haciendo un wheelie!"`'''

class Vehiculo:

    def __init__(self, tipo, marca):
        self.tipo = tipo
        self.marca = marca

    def hacer_wheelie(self):
        return f'¡La moto tipo {self.tipo} {self.marca} está haciendo un wheelie!'

class Moto(Vehiculo):
    def __init__(self, tipo, marca, persona):
        super().__init__(tipo, marca)
        self.persona = persona
    
    def hacer_wheelie(self):
        return f'¡La moto tipo {self.tipo} + {self.marca} está haciendo un wheelie! {self.persona}'


moto1=Moto('moto', ' yamaha',2)
print(moto1.hacer_wheelie())
