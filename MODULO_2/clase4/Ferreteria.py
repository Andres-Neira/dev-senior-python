import threading 
from abc import ABC,abstractmethod

#patron singleton
class SistemaFacturacion:
    _instancia = None
    _lock = threading.Lock

    def __new__(cls, *args,**kargs):
        if not cls._instancia:
            cls._instancia=super(SistemaFacturacion,cls).__new__(cls)
            cls._instancia._inicializacionHistorico()
        return cls._instancia
        # opcional
        '''
        with cls._lock:
            if cls._instacia is None:
                cls._instacia = super(SistemaFacturacion,cls).__new__(cls)
                cls._instacia.:incializacionHistorico()
            return cls._instacia
        '''
    def _inicializacionHistorico(self):
        self.historial = []
        print('Sistema de facturacion iniciado')

    def registrarOperacion(self,operacion):
        self.historial.append(operacion)
        print(f'La operacion es registrada {operacion}')

# clase abstracta = Superclase

class ProcesoNegocio(ABC):

    @abstractmethod
    def ejecutar(self):
        pass

class ProcesarPedido(ProcesoNegocio):

    def ejecutar(self):
        print('Procesando pedido')
        return 'Pedido Procesado'

class ProcesarFactura(ProcesoNegocio):
    def ejecutar(self):
        print('Procesando pedido')
        return 'Pedido Procesado'
    
# crear fabrica 
class FabricaProcesoNegocio:
    @staticmethod
    def crearProceso(tipoProceso):
        if tipoProceso == 'pedido':
            return ProcesarPedido()
        elif tipoProceso == 'factura':
            return ProcesarFactura()
        else:
            raise ValueError(f'El proceso {tipoProceso} no existe')

if __name__== '__main__':
    
    Sistema_Facturacion = SistemaFacturacion()
    proceso1 = FabricaProcesoNegocio.crearProceso('pedido')
    proceso2 = FabricaProcesoNegocio.crearProceso('factura')

    resultadoPedido1= proceso1.ejecutar()
    Sistema_Facturacion.registrarOperacion(resultadoPedido1)
    
    resultadoPedido2= proceso2.ejecutar()
    Sistema_Facturacion.registrarOperacion(resultadoPedido2)

    print("\n*** Historico de procesos de negocio ***\n")   
    for operacion in Sistema_Facturacion.historial:
        print(f"Transacción: {operacion}")