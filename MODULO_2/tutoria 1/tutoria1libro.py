class libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor


    def descripcion(self):
        return f'El libro {self.titulo} fue escrito por {self.autor}'

libro1=libro('El libro del señor de los anillos ','JRR TOLKEN')
libro2 = libro('Cien años de soledad','Gabriel Garcia marquez')
print(libro1.descripcion())
print(libro2.descripcion())
