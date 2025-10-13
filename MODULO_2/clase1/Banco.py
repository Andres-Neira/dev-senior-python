class Banco:

    TASA_INTERES = 0.03

    def __init__(self, nombre):
        self.nombre = nombre
    
    @classmethod
    def cambiarTasa(cls,nuevaTasa):
        cls.TASA_INTERES=nuevaTasa

    @staticmethod
    def conversionDolares(dolares):
        return dolares*0.85

Banco1=Banco("Bacolompia")
Banco2=Banco("Banco de Bogotá")

print(Banco1.nombre)
print(Banco1.TASA_INTERES)
print(Banco2.nombre)
print(Banco2.TASA_INTERES)

print(Banco1.nombre)
Banco1.cambiarTasa(0.4)
print(Banco1.TASA_INTERES)


print(Banco2.nombre)
Banco2.cambiarTasa(0.2)
print(Banco2.TASA_INTERES)

print(Banco1.conversionDolares(1000))