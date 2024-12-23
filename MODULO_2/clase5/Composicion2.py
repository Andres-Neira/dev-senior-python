class Tarea:
    def __init__(self, name, age):
        pass
    def ejecutar(self):
        pass

class Proyecto(Tarea):
    def __init__(self):
        pass

    def ejecutar(self):
        return('trabajando en un proyecto')

class Capacitacion(Tarea):

    def __init__(self):
        pass
    def ejecutar(self):
        return 'tomando una capacitación'

class Evaluacion(Tarea):

    def __init__(self):
        pass
    def ejecutar(self):
        return 'Realizando evaluacion'

class Empleado:
    def __init__(self, name):
        self.name = name
        self.tareas = []

    def asignar_tarea(self, tarea):
        self.tareas.append(tarea)

    def realizar_tarea(self):
        print(f'{self.name} esta realizando las siguientes tareas')
        for tarea in self.tareas:
            print(f'{tarea.ejecutar()}')

protecto = Proyecto()
capactiacion = Capacitacion()
evaluacion = Evaluacion()

empleado = Empleado('Andres Neira')

empleado.asignar_tarea(protecto)
empleado.asignar_tarea(capactiacion)
empleado.asignar_tarea(evaluacion)

empleado.realizar_tarea()