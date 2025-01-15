import json
class SistemaGuardado:
    __intance = None

    @staticmethod
    def get_instance():
        if SistemaGuardado.__intance is None:
            SistemaGuardado.__intance = SistemaGuardado()
            return SistemaGuardado.__intance
# inicializacion del sistema
    def __init__(self):
        self.archivo_guardado = "guardado.bat"

    def guardar_juego(self, dato_a_guaradar):
        with open(self.archivo_guardado, "w") as f: # w es para escribir write
            json.dump(dato_a_guaradar,f,indent=4)


    def cargar_juego(self,):
        with open(self.archivo_guardado,"r") as f: # r es para leer read
            return json.load(f)

class Jugador():

    def __init__(self, nombre, nivel):
        self.nombre = nombre
        self.nivel= nivel

    def guardar_progreso(self):
        guardo = SistemaGuardado.get_instance()
        data_a_guardar = self.serializar()
        guardo.guardar_juego(data_a_guardar)

    def serializar(self):
        return{
            "nombre":self.nombre,
            "nivel": self.nivel
        }
    @classmethod
    def deserializar(self,data):
            return self(data["nombre"],data["nivel"])
class cargarPartida():
    def guardar_progreso(self):
        guardo = SistemaGuardado.get_instance()
        data_a_guardar = guardo.cargarjuego()
        jugador = jugador.deserializar(data_a_guardar)
'''
jugador1= Jugador("andres",25)
guardando = SistemaGuardado.get_instance()
guardando.guardar_juego(jugador1.serializar())
'''
guardando = SistemaGuardado.get_instance()
datos_cagados = guardando.cargar_juego()
Jugador_cargando= Jugador.deserializar(datos_cagados)
print(Jugador_cargando.nombre)