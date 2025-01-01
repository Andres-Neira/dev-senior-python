'''1. Clase `Banco`: Implementa una clase `Banco` con:
Atributo de clase `tasa_interes`.
Método de clase `actualizar_tasa(nueva_tasa)`.
Método `calcular_interes(monto)`
que calcule el interés sobre un monto basado en la tasa actual.'''

class Banco:

    tasa_interes=0.12

    @classmethod
    def actualizar_tasa(cls,nueva_tasa):
        cls.tasa_interes=nueva_tasa
        return f'nueva tasa de interes {cls.tasa_interes}'
    @staticmethod
    def actualizar_interes(monto):
        return f'Los nuevos intereses son {Banco.tasa_interes*monto} con tasa de {Banco.tasa_interes} y monto {monto}'

print(f'la tasa de interes actual es {Banco.tasa_interes}')
#print(Banco.actualizar_interes(10000))

print(Banco.actualizar_tasa(0.18))
print(Banco.actualizar_interes(10000))

print(Banco.actualizar_tasa(0.2))
print(Banco.actualizar_interes(10000))