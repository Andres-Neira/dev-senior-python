from abc import ABC, abstractmethod

class Sujeto:
    def __init__(self):
        self._observadores = []

    def agreagarObservador(self, observador):
        self._observadores.append(observador)

    def quitarObservador(self, observador):
        self._observadores.remove(observador)

    def notificarObservador(self, mensaje):
        for observador in self._observadores:
            observador.actualizar(mensaje)
class Observador(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def actualizar(self, mensaje):
        raise NotImplementedError('Subclase debe estar implementada')

class ObservadorConcreto(Observador):
    def __init__(self, nombre):
        self.nombre = nombre
    def actualizar(self, mensaje):
        print (f'{self.nombre} recibio : {mensaje}')


sujeto = Sujeto()

obs1 = ObservadorConcreto('Observador 1')
obs2 = ObservadorConcreto('Observador 2')

sujeto.agreagarObservador(obs1)
sujeto.agreagarObservador(obs2)

sujeto.notificarObservador('Mensaje de adevertencia')