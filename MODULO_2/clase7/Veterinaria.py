#ejercicio 
#1 crear clases abstractas , crear clientes con atributos nombre, contacto, dirección
#2 asociar una o mas mascotas a cada cliente
# se deben registrar las citas del mas cotas con atributos como lo son fecha , hora y servicio y veterianrio asignado
# debe de tener un menu con 1 registrar cliente, 2, registrar mascota, 3 programar cita, 4 consultar historial 5 salir
from abc import ABC, abstractmethod
from datetime import datetime

class Persona(ABC):

    def __init__(self,nombre,contacto,direccion):
        self.nombre=nombre
        self.contacto=contacto
        self.direccion=direccion

    @abstractmethod
    def mostrarInformacion(self):
        pass


class Veterinario(Persona):

    def __init__(self,nombre,contacto,direccion):
        super().__init__(nombre,contacto,direccion)

    def mostrarInformacion(self):
        print(f"el veterinario {self.nombre} se registro con exito")

class Cliente(Persona):

    def __init__(self,nombre,contacto,direccion):
        super().__init__(nombre,contacto,direccion)
        self.mascota=[]

    def agregarMascota(self,mascota):
        self.mascota.append(mascota)
        print(f"La mascota {mascota.nombrem} se registro con exito")

    def mostrarInformacion(self):
        print(f"el cliente {self.nombre} se registro con exito")


class Mascota:

    def __init__(self,nombrem,especie,raza,edad):

        self.nombrem=nombrem
        self.especie=especie
        self.raza=raza
        self.edad=edad

class Cita:

    def __init__(self,fecha,hora,servicio,veterinario):

        self.fecha=fecha
        self.hora=hora
        self.servicio=servicio
        self.veterinario=veterinario
        self.cliente=[]

    def agregarCliente(self,cliente):
        self.cliente.append(cliente)

class HistorialCitas:

    def __init__(self):
        self._historialCitas=[]

    def AgregarCita(self,cita):

        self._historialCitas.append(cita)

    def eliminarCita(self,cita):

        self._historialCitas.remove(cita)

    def modificarCita(self,cita):
        pass
def AsociarMascota(self):

veterinario1=Veterinario("Andres","3125830049","cr 13")
veterinario1.mostrarInformacion()

cliente1=Cliente("Camilo","3144572234","vr 4 asd")
cliente1.agregarMascota(Mascota("CHo","as","asa","25"))

cliente1.mostrarInformacion()