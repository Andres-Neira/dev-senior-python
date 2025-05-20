from abc import ABC, abstractmethod
from datetime import datetime

class Persona(ABC):
    def __init__(self, nombre, contacto,direccion):
        self.nombre=nombre
        self.contacto=contacto
        self.direccion=direccion

    @abstractmethod
    def mostrar_informacion(self):
        pass

class Mascota(ABC):
    def __init__(self, nombre, especie, raza, edad):
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.edad = edad
        self.historial_citas=[]

    @abstractmethod
    def agregar_al_historial(self, detalles_servicio):
        pass
class Cita(ABC):
    def __init__(self, fecha, hora, servicio, veterinario):
        self.fecha=fecha
        self.hora=hora
        self.servicio=servicio
        self.veterinario=veterinario

    @abstractmethod
    def actualizar(self, **kwargs):
        pass

#definicion de subclases
class Cliente(Persona):
    def __init__(self, nombre, contacto,direccion):
        super().__init__(nombre, contacto,direccion)
        self.mascota = []

    def agregar_mascota(self, mascota):
        self.mascota.append(mascota)

    def mostrar_informacion(self):
        return f'Cliente : {self.nombre} contacto : {self.contacto} direccion : {self.direccion}'

class RegistroMascota(Mascota):
    def agregar_al_historial(self, detalles_servicio):
        self.historial_citas.append(detalles_servicio)

    def obtener_historia(self):
        return self.historial_citas

class CitaMascota(Cita):
    def actualizar(self, **kwargs):
        for clave, valor in kwargs.items():
            if hasattr(self, clave):
                setattr(self, clave, valor)

class SistemaVeterinaria:
    def __init__(self):
        self.clientes = []

    def registrar_cliente(self):
        try:

            nombre= input('Ingrese el nombre del cliente').strip()
            contacto = input('Ingrese el contacto :').strip()
            direccion = input('Ingrese la direccion ').strip()
            if not nombre or not contacto or not direccion:
                raise ValueError('Todos los datos son obligatorios')

            cliente = Cliente(nombre, contacto, direccion)
            self.clientes.append(cliente)
            print('Cliente registrado con exito!')

        except ValueError as e:
            print(f'Error :{e}')


    def registrar_mascota(self):
        try:

            nombre_cliente = input('Ingrese nombre dle cliente al que asociar la mascota').strip()
            cliente = next((c for c in self.clientes if c.nombre == nombre_cliente),None)

            if not cliente:
                raise ValueError('Cliente no encontrado')

            nombre_mascota=input('Ingrese el nombre de la mascota : ').strip()
            especie = input('Ingrese la especie : ').strip()
            raza = input('Ingrese la raza : ').strip()
            edad = int(input('Ingrese la edad : ').strip())

            if not nombre_mascota or not especie or not raza or edad <=0:
                raise ValueError('Detalles de la mascota invalidos')

            mascota=RegistroMascota(nombre_mascota,especie,raza,edad)
            cliente.agregar_mascota(mascota)

        except ValueError as e:
            print(f'Error : {e}')
    def programar_cita(self):
        try:

            nombre_cliente=input('Ingres el nombre del cliente al que asociar la mascota : ').strip()
            nombre_mascota=input('Ingres el nombre de la mascota : ').strip()


            cliente = next((c for c self.clientes if c.nombre == nombre_cliente),None)
            if not cliente:
                raise ValueError('Cliente no encontrado')

            mascota = next((m for m in self.cliente.mascotas if m.nombre == nombre_mascota),None)
            if not mascota:
                raise ValueError('Mascota no encontrada')

            fecha = input('Ingrese la fecha (AAA-MM-DD)').strip()
            hora = input('Ingrese la hora (hh:mm)').strip()
            servicio = input('Ingres el servicio (consulta , vacunación, etc)').strip()
            veterinario= input('Ingrese el nombre del veterinario').strip()


            datetime.strptime(fecha,"%Y-%m-%d")
            datetime.strptime(hora,"%H:%M")

            if not servicio or not veterinario:
                raise ValueError("Detalle de la cita invalidos")

        except ValueError as e:
            print(f'Error : {e}')
