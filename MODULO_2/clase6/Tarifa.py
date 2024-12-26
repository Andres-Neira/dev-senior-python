from abc import ABC , abstractmethod

class EstrategiaTarifa(ABC):

    @abstractmethod
    def calcularTarifa(self, distancia, tiempo):
        raise NotADirectoryError('Se debe implementar este metodo')

class TarifaFija(EstrategiaTarifa):
    def calcularTarifa(self, distancia, tiempo):
        return 100

class TarifaHora(EstrategiaTarifa):
    def calcularTarifa(self, distancia, tiempo):
        return tiempo*25

class TarifaKilometro(EstrategiaTarifa):
    def calcularTarifa(self, distancia, tiempo):
        return distancia*2

class CalculadoraTarifa:
    def __init__(self, estrategia):
        self.estrategia = estrategia

    def cambiaEstrategia(self, estrategia):
        self.estrategia = estrategia

    def calcular(self, distancia, tiempo):
        return self.estrategia.calcularTarifa(distancia, tiempo)

arriendo1 = TarifaFija()
calculador = CalculadoraTarifa(arriendo1)
print('La tarifa fija es : ', calculador.calcular(10,5))

calculador.cambiaEstrategia(TarifaHora())
print(' Tarifa por hora : ', calculador.calcular(100,2))

calculador.cambiaEstrategia(TarifaKilometro())
print(' La tarifa por kilometros : ', calculador.calcular(100,3))
