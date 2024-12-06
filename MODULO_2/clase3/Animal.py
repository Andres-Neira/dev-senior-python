class Animal:

    def __init__(self):
        pass

    def hablar(self):
        pass

class Perro(Animal):
    def __init__(self)
        pass
    def hablar(self):
        return f'El perro hace wou'

class Gato(Animal):

    def __init__(self):
        pass

    def hablar(self):
        return f'El gato hace meow'

animales=[Perro(),
          Gato(),
          Perro(),
          Gato()]

for animal in animales:
    print(animal.hablar)