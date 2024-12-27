'''2. Clase `Persona`: Diseña una clase `Persona`
con los atributos: Nombre y Edad.
Incluye un método `es_mayor_de_edad` que retorne `True`
si la edad es 18 o mayor, de lo contrario, `False`.'''

class Persona:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        edad=False

    def mayorEdad(self):
        if self.age>=18:
            edad=True
        else:
            edad=False
        return print(edad)
    
persona1=Persona('Andres',15)
persona1.mayorEdad()