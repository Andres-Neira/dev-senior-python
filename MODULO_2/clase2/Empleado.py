class Empleado:
    def __init__(self,nombre,salario):
        self._nombre=nombre
        self._salario=salario

    def mostrarInformacion(self):
        return f'Nombre: {self._nombre}, salario : {self._salario}'

    def obtenerSalario(self):
        return self._salario

    def establecerSalario(self,nuevoSalario):
        if nuevoSalario <1300000:
            return f'El salario no puede ser menor al salario minimo'
        self._salario= nuevoSalario
        return f'El nuevo salario es : {self._salario}'
    
Empleado1=Empleado('Andres',1300000)
print(Empleado1.mostrarInformacion())
print(Empleado1.obtenerSalario())
print(Empleado1.establecerSalario(1200000))
print(Empleado1.establecerSalario(2500000))