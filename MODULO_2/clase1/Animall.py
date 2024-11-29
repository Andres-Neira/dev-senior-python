class Animall:

    cantidadAnimales = 0

    def __init__(self, name):
        self.name = name
        Animall.cantidadAnimales +=1


    @classmethod
    def totalAnimales(cls):
        return f'tengo {cls.cantidadAnimales} animalitos'

animalito1 = Animall('Ron')
animalito2 = Animall('Rayo')
animalito3 = Animall('Toby')

print(animalito3.name)
print(Animall.cantidadAnimales)
print(Animall.totalAnimales())