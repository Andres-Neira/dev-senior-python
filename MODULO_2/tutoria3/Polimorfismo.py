class Gato:
    def sonido(self):
        return "miau miau"

class Carro:
    def sonido(self):
        return 'pii pii'

def hacer_sonido(objeto):
    print(objeto.sonido())

#instanciar

mi_gato = Gato()
mi_carro = Carro()
print(f'Mi objeto hace :')
hacer_sonido(mi_gato)
hacer_sonido(mi_carro)