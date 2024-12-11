from abc import ABC, abstractmethod


# CLASE ABSTRACTA= Superclase 'clases'
class Clases(ABC):
    @abstractmethod
    def operacion(self):
        pass

# creacion de subclases

class ClaseA(Clases):
    def operacion(self):
        return "Esta es clase A"

class ClaseB(Clases):
    def operacion(self):
        return ' Esta es clase B'

# CLase Factory : factoria, fabrica

class FabricaClases:

    @staticmethod
    def CreacionObjetos(tipoObjeto):
        if tipoObjeto =='A':
            return ClaseA()
        elif tipoObjeto =='B':
            return ClaseB()
        else:
            raise ValueError(f'La clase {tipoObjeto} no existe')

objeto1= FabricaClases.CreacionObjetos('A')
objeto2=FabricaClases.CreacionObjetos('C')

print(objeto1.operacion())