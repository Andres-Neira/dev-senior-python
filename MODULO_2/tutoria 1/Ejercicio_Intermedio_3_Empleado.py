'''3. Clase `Empleado`: Diseña una clase `Empleado`
con atributos: Nombre y Salario.
Incluye un métodoaumentar_salario` que aumente el salario en un porcentaje dado como argumento.
Ejemplo:
emp = Empleado("Luis", 2000)
emp.aumentar_salario(10)  # Incrementa el salario un 10%
print(emp.salario)  # Salida: 2200'''

class Empleado:

    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def aumentarSalario(self,porcentaje):
        self.salario = self.salario*(1+porcentaje)
        print('aumento exitoso', (porcentaje*100),'%')

empleado= Empleado('Andres', 1300000)
print(empleado.nombre,'  ',empleado.salario)
empleado.aumentarSalario(0.8)
print('salario con aumento ',empleado.salario)
