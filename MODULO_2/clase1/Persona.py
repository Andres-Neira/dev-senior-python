class Persona:
# El nombre de la clase debe ser igual al del archivo ejemplo Persona
#El metodo init encapsula la información
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
# este metodo trabaja el metodo constructor
    def saludar(self):
        return f'Hola soy {self.nombre} y tengo {self.edad} años'

