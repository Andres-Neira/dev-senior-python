import logging
from dataclasses import dataclass

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="registro_Ejercicio2.log",
    filemode="a" # a crea historico w mira el ultimo
)

#Crear un nuevo handler para gestionar mensaje de auditoria por.log y por consola

console_handler=logging.StreamHandler() # crea una instancia , es decir un nuevo manejador
console_handler.setLevel(logging.DEBUG) # configurar el nivel del logging, en este caso el nivel m´s leve
console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')) # da formato de salida al logging
logging.getLogger().addHandler(console_handler) # Agrega la instancia

@dataclass
class Factura:
    cliente : str
    Cantidad : int
    precio_unitario : float

    def procesar(self):
        try:
            logging.info(f"Iniciando el procesos de fabricación")

            if self.Cantidad<=0:
                raise ValueError(f"La cantidad del producto debe ser mayor a cero")
            if self.precio_unitario<=0:
                raise ValueError(f'El precio debe ser mayor a cero')

            total= self.Cantidad*self.precio_unitario
            logging.info(f"Factura procesada --- Total de la compra : {total} - Cliente : {self.cliente}")

        except ValueError as e:
            logging.error(f'Error de validación del cliente : {self.cliente} : {e}')

        except ValueError as e:
            logging.error(f'Error inesperado al procesar la factura de {self.cliente} : {e}')

        finally:
            logging.info(f'El proceso de facturación para {self.cliente} Finalizo')

# se ejecuta el codigo
if __name__=="__main__" :
    Factura1=Factura(cliente="Juan",Cantidad=4,precio_unitario=12.5)
    Factura1.procesar()

    Factura2=Factura(cliente="Maria",Cantidad=0,precio_unitario=0.2)
    Factura2.procesar()

    Factura2=Factura(cliente="Maria",Cantidad=12,precio_unitario=-3)
    Factura2.procesar()