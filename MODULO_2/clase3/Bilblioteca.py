class Biblioteca:
    def __init__(self, titulo,autor):
        self.titulo=titulo
        self.autor=autor
        pass

    def descripcion(self):
        return f'Libor {self.titulo} autor {self.autor}'
    #opcional
    def __str__(self):
        return f'Libro {self.titulo} autor {self.autor}'
        pass

class libro(Biblioteca):

    def __init__(self,titulo,autor,formato):
        super().__init__(titulo,autor)
        self.formato=formato

    def descripcion(self):
        return f'Libro {self.titulo} autor {self.autor} formato {self.autor}'
    
    def __str__(self):
        return f'Libro {self.titulo} autor {self.autor} formato {self.formato} str'
    
libro1=Biblioteca('La peste ','Alberto Campo')
libroDigital1=libro('El conde de monte cristo', 'Alejandro Dumas','PDF')

print(libro1.__str__())
print(libroDigital1.descripcion())

print(libroDigital1.__str__())
print(libroDigital1.descripcion())