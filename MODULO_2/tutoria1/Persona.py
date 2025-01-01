class Persona:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def mayorEdad(self):
        if self.age > 18:
            return f'Es mayor de edad tiene {self.age}'
        else:
            print('Es menor de edad')


persona1=Persona('Persona',12)

print(persona1.mayorEdad())