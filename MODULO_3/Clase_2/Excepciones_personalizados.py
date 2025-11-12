class ErroDePago(Exception):
    """Gestion de excepciones"""
    pass

class PasarelaDePago():
    """Simulación de estrategia tecnologica de pago"""

    @staticmethod
    def procesar_pago(numero_tarjeta,monto):

        if not numero_tarjeta.startswith("4"): # esto siver para indicar con cuanto debe de comenzar un texto
            raise ErroDePago("El número de la tarjeta no es valido")
        if monto <= 0:
            raise ErroDePago("El monto debe ser mayora 0")
        
        return f"Pago de {monto} fue procesado con exito"
    
def procesar_pago_cliente(nombre_cliente,numero_tarjeta,monto):
    try:

        print(f"Iniciando el proceso de pago para {nombre_cliente}")
        resultado=PasarelaDePago.procesar_pago(numero_tarjeta,monto)
    except ErroDePago as e:
            print(f"Error al procesar pago {e}")
    except Exception as e:
        print(f"Se produjo un error inesperado {e}")
    else:
        print(resultado)
    finally:
        print("Registro Finalizado")

if __name__=="__main__":
    procesar_pago_cliente("Jose","423125",9986)
