class Animal:
    def __init__(self,nombre):
        self.nombre=nombre

    def hablar(self):
        return f'Todo animal habla de alguna forma'
    def __str__(self):
        return f'El nombre del animal es {self.nombre}'

class Perro(Animal):
    def __init__(self,nombre,raza):
        super().__init__(nombre)
        self.raza=raza

    def hablar(self):
        return f'Guau guau'
    def __str__(self):
        return f'El nombre de perro es {self.nombre} y raza es : {self.raza}'

Animal1=Animal('Wisky')
Perro1=Perro('tequila','doberman')
print(Animal1.hablar())
print(Animal1.__str__())
print(Perro1.hablar())
print(Perro1.__str__())
