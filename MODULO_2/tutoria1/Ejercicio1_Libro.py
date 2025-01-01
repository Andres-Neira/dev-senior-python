'''  1. Clase `Libro`: Crea una clase llamada `Libro` que tenga 
los atributos: Título y Autor. 
Implementa un método `descripcion` que devuelva un texto como: `"El libro [Título] fue escrito por [Autor]."`'''

class Libro:

    def __init__(self, titulo, autor):
        self.titulo=titulo
        self.autor=autor

    def descripcion(self):
        return f'El libro {self.titulo} fue escrito por {self.autor}'

libro1=Libro('matar a un ruiz señor','Jean grean')
print(libro1.descripcion())