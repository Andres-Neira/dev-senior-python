'''5. Sistema de Inventario Simple:
Diseña una clase `Producto` con: Nombre y Precio.
Luego, implementa una clase `Inventario` que administre una lista de productos. Incluye métodos para: 
- Agregar un producto.
- Mostrar la lista de productos.
- Calcular el valor total del inventario.'''
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
class Inventario(Producto):

    def __init__(self,nombre,precio):
        super().__init__(nombre, precio)
        self.inventario=[]

    def agregar_producto(self,producto):
        self.inventario.append(producto)
        print('Prodcuto añadido con exito')

    def mostrar_inventario(self):
        for elemento in range(self.inventario):
            print(elemento)




producto1= Producto('leche',1500)
Inventario.agregar_producto('3')
