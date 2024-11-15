from datetime import datetime
import statistics
class tareas:
    # función de inicialización = metodo constructor
    def __init__(self,nombre,fechaLimite,categorias,horasDedicadas):
        self.nombre = nombre
        self.fechaLimite = fechaLimite
        self.categorias = categorias
        self.horesDedicadas = horasDedicadas
        pass
# Funcion para agregar una tarea
def agregarTarea(listaTareas):
    nombre=input("Ingrese el nombre de la tarea : ")
    # la fecha limite se debe diferenciar de la clasr
    fechaLimite_str=input("Ingrese la fecha limite de la tarea DD/MM/YYYY : ")
    try:
        fechaLimite=datetime.strptime(fechaLimite_str,'%d/%m/%y')

    except ValueError:
        print('Fecha no valida')
        return
    categorias = input('Ingrese la categoria de la carrera(Estudio, Personal, Trabajo, otras)')
    horasDedicadas_str=input('Ingrese las horas dedicadas, separadas en comas : ')
    try:
        horasDedicadas = list(map(float,horasDedicadas_str.split(',')))
    except ValueError:
        print('horas dedicadas no validas')
        return
# crear un objeto y lo agrega a lista de tareas
    tarea=tareas(nombre,fechaLimite,categorias,horasDedicadas)
    listaTareas.append(tarea)
    print('Tarea ingresada con objeto')

# funcion para visualizar tareas
def visualizarTareas(listaTareas):
    if not listaTareas:
        print('no hay tareas registradas')
        return
    for i,tarea in enumerate(listaTareas,start=1):
        print(f'\nTarea : {i} ')
        print(f'\nnombre : {tarea.nombre} ')
        print(f'\n Fecha limite : {tarea.fechaLimite.strftime('%d/%m/%y')}')
        print(f'horas dedicadas : {tarea.horasDedicadas}')

def analizarTareas(listaTareas):
    if not listaTareas:
        print('no hay tareas')
        return
    for tarea in listaTareas:
        promedio=statistics.mean(tarea.horasDedicadas)
        maximo=max(tarea.horasDedicadas)
        minimo=min(tarea.horasDedicadas)
        print(f'\n Analisis de {tarea.nombre}')
        print(f'\n Promedio de horas {promedio}')
        print(f'Maximo de horas {maximo}')
        print(f'Minimo de horas {minimo}')

def generarInforme(listaTareas):
    if not listaTareas:
        print('no hay tareas')
        return
    # abrir un archivo txt
    with open('informe_tareas.txt','w') as archivo:
        # escribir los detalles de la tarea en el archivo
        for tarea in listaTareas:
            archivo.write(f'Nombre : {tarea.nombre}\n')
            archivo.write(f'\n Analisis de {tarea.nombre}')
            archivo.write(f'\n Promedio de horas {promedio}')
            archivo.write(f'Maximo de horas {maximo}')
            archivo.write(f'Minimo de horas {minimo}')
    print(' informe generado como "informe_tareas.txt"')

def menu():
    listaTareas = []
    while True:
        print(" MENU DE OPCIONES")
        print('1. Agregar tarea')
        print('2. Visualizar tareas ')
        print('3. Analizar horas dedicadas')
        print('4. Generar informe')
        print('5. salir')
        opcion=input('Seleccione una opcion')

        if opcion=='1':
            agregarTarea(listaTareas)
        elif opcion=='2':
            visualizarTareas(listaTareas)
        elif opcion=='3':
            analizarTareas(listaTareas)
        elif opcion=='4':
            generarInforme(listaTareas)
            break
        else:
            print('Opcion invalida')

if __name__=='__main__':
    menu()