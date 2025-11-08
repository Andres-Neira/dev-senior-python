from abc import ABC, abstractmethod
from datetime import datetime

# Creación de clase persona, con el cual se va crear el cliente y el veterinario
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

    def agregar_al_historial(self, detalles_servicio):
        pass
    def obtener_historial(self):
        pass
class Cita(ABC):
    def __init__(self, fecha, hora, servicio, veterinario):
        self.fecha=fecha
        self.hora=hora
        self.servicio=servicio
        self.veterinario=veterinario

    def actualizar(self, **kwargs):
        pass

#definicion de subclases
class Cliente(Persona):
    def __init__(self, nombre, contacto,direccion):
        super().__init__(nombre, contacto,direccion)
        self.mascotas = []

    def agregar_mascota(self, mascota):
        self.mascotas.append(mascota)

    def mostrar_informacion(self):
        return f'Cliente : {self.nombre} contacto : {self.contacto} direccion : {self.direccion}'

class RegistroMascota(Mascota):
    def agregar_al_historial(self, detalles_servicio):
        self.historial_citas.append(detalles_servicio)

    def obtener_historial(self):
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

            nombre= input('Ingrese el nombre del cliente : ').strip()
            contacto = input('Ingrese el contacto : ').strip()
            direccion = input('Ingrese la direccion : ').strip()
            if not nombre or not contacto or not direccion:
                raise ValueError('¡ Todos los datos son obligatorios !')

            cliente = Cliente(nombre, contacto, direccion)
            self.clientes.append(cliente)
            print(' Cliente registrado con exito !!')

        except ValueError as e:
            print(f'Error :{e}')


    def registrar_mascota(self):
        try:

            nombre_cliente = input('Ingrese nombre del cliente al que se le va a asociar la mascota : ').strip()
            cliente = next((c for c in self.clientes if c.nombre == nombre_cliente),None)

            if not cliente:
                raise ValueError(' Cliente no encontrado ')

            nombre_mascota=input('Ingrese el nombre de la mascota : ').strip()
            especie = input('Ingrese la especie : ').strip()
            raza = input('Ingrese la raza : ').strip()
            edad = int(input('Ingrese la edad : ').strip())

            if not nombre_mascota or not especie or not raza or edad <=0:
                raise ValueError('Detalles de la mascota invalidos')

            mascota=RegistroMascota(nombre_mascota,especie,raza,edad)
            cliente.agregar_mascota(mascota)
            print(f"Mascota {mascota.nombre} se registro con exito al cliente {cliente.nombre}")

        except ValueError as e:
            print(f'Error : {e}')
    def programar_cita(self):
        try:

            nombre_cliente=input('Ingrese el nombre del cliente al que asociar la mascota : ').strip()
            nombre_mascota=input('Ingrese el nombre de la mascota : ').strip()


            cliente = next((c for c in self.clientes if c.nombre == nombre_cliente),None)
            if not cliente:
                raise ValueError(' Cliente no encontrado ')

            mascota = next((m for m in cliente.mascotas if m.nombre == nombre_mascota),None)
            if not mascota:
                raise ValueError(' Mascota no encontrada ')

            fecha = input(' Ingrese la fecha (AAAA-MM-DD) : ').strip()
            hora = input('Ingrese la hora (hh:mm) : ').strip()
            servicio = input('Ingrese el servicio (consulta , vacunación, etc) : ').strip()
            veterinario= input('Ingrese el nombre del veterinario : ').strip()


            datetime.strptime(fecha,"%Y-%m-%d")
            datetime.strptime(hora,"%H:%M")

            if not servicio or not veterinario:
                raise ValueError("Detalle de la cita invalidos")

            cita=CitaMascota(fecha,hora,servicio,veterinario)
            mascota.agregar_al_historial(cita)
            print("cita programada con exito")

        except ValueError as e:
            print(f'Error : {e}')
    def ActualizaCita(self):
        try:
            nombre_cliente=input('Ingrese el nombre del cliente al que asociar la mascota : ').strip()
            nombre_mascota=input('Ingrese el nombre de la mascota : ').strip()


            cliente = next((c for c in self.clientes if c.nombre == nombre_cliente),None)
            if not cliente:
                raise ValueError('Cliente no encontrado')

            mascota = next((m for m in cliente.mascotas if m.nombre == nombre_mascota),None)
            if not mascota:
                raise ValueError('Mascota no encontrada')

            if not mascota.historial_citas:
                raise ValueError('No hay citas registradas para las mascotas')
            print('Citas disponibles para actualizar : ')

            for i,cita in enumerate(mascota.historial_citas):
                encabezados=("#","Fecha","Hora","Servicio","Veterinario")
                data=[[i+1,cita.fecha,cita.hora,cita.servicio,cita.veterinario]]
                print(tabulate(data,encabezados,tablefmt="fancy_grid"))
#                print(f"{i+1} fecha : {cita.fecha} Hora : {cita.hora} Servicio : {cita.servicio} Veterinario : {cita.veterinario}")
            indice=int(input('Seleccione el número de la lista a actualizar : ').strip())-1

            if indice<0 or indice>=len(mascota.historial_citas):
                raise ValueError("Selección invalida")
            print("Deje en blanco los campos que no desa actualizar")
            cita_seleccionada=mascota.historial_citas[indice]
            
            nueva_fecha=input(" Nueva fecha (AAAA-MM-DD) : ").strip()
            nueva_hora=input(" Nueva hora (HH:MM) : ").strip()
            nuevo_servicio=input("Nuevo servicio : ").strip()
            nuevo_veterianrio=input("Nuevo veterinario : ").strip()

            if nueva_fecha:
                datetime.strptime(nueva_fecha,"%Y-%m-%d")
                cita_seleccionada.actualizar(fecha =nueva_fecha)
            if nueva_hora:
                datetime.strptime(nueva_hora,"%H:%M")
                cita_seleccionada.actualizar(hora =nueva_hora)
            if nuevo_servicio:
                cita_seleccionada.actualizar(servicio =nuevo_servicio)
            if nuevo_veterianrio:
                cita_seleccionada.actualizar(veterinario =nuevo_veterianrio)
            print(" Cita actualizada con exito")



        except ValueError as e:
            print(f"Error _ {e}")
    
    def consultar_Cita(self):

        try:

            nombre_cliente=input('Ingrese el nombre del cliente al que asociar la mascota : ').strip()
            nombre_mascota=input('Ingrese el nombre de la mascota : ').strip()


            cliente = next((c for c in self.clientes if c.nombre == nombre_cliente),None)
            if not cliente:
                raise ValueError('Cliente no encontrado')

            mascota = next((m for m in cliente.mascotas if m.nombre == nombre_mascota),None)
            if not mascota:
                raise ValueError('Mascota no encontrada')
            historial=mascota.obtener_historial()
            if not historial:
                print(" No hay historial para la mascota")

            else:
                for entrada in historial:
                    encabezados=["Fecha","Hora","Servicio","Veterinario"]
                    datos=[[entrada.fecha,entrada.hora,entrada.servicio,entrada.veterinario]]
                    print(tabulate(datos,encabezados,tablefmt="grid"))
        except ValueError as e:
            print(f" Error : {e}")
        
    def Iniciar(self):
        while True:
            print("\n Sistema veterinaria")
            print("1. Registrar cliente")
            print("2. registrar Mascota")
            print("3. Programa cita")
            print("4. Actualizar Cita")
            print("5. COnsultar Cita")
            print("6. Salir")

            opcion=input("Ingrese su opcion : ").strip()

            if opcion == "1":
                self.registrar_cliente()
            elif opcion=="2":
                self.registrar_mascota()
            elif opcion=="3":
                self.programar_cita()
            elif opcion=="4":
                self.ActualizaCita()
            elif opcion=="5":
                self.consultar_Cita()
            elif opcion =="6":
                print("-----------Sistema Cerrado---------------")
                break
            else:
                print("Valor no valido , digite alguna de las opciones anteriores")

if __name__=="__main__":
    sistema= SistemaVeterinaria()
    sistema.Iniciar()
