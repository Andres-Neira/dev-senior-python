import logging
from dataclasses import dataclass,field

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="registro.log",
    filemode="a"
)

@dataclass
class Producto:
    nombre:str
    precio:float
    cantidad:int

    def comprar(self, cantida : int):
        if cantida > self.cantidad:
            logging.error(f" Error : no hay suficiente cantidad de producto {self.nombre}. el stock disponible es de {self.cantidad}")
            raise ValueError(f" Error : no hay suficiente cantidad de producto {self.nombre}. el stock disponible es de {self.cantidad}")
        else:
            self.cantidad-=cantida
            logging.info(f" la compra es exitosa . el stock restante es {self.cantidad}")
            return self.precio*cantida

@dataclass
class Tienda:
    productos: list[Producto] = field(default_factory=list)

    def agregarProducto(self,producto:Producto):
        self.productos.append(producto)
        logging.debug(f"{producto.nombre} fue agragado con exito el precio es de {producto.precio} - cantidad  {producto.cantidad} unidades en stock")

    def realizarCompra(self,nombre_producto : str, cantidad : int):
        producto = next(m for m in self.productos if m.nombre == nombre_producto)
        if producto:
            try:
                total=producto.comprar(cantidad)
                logging.info(f" Compra realizada {cantidad} unidades de {nombre_producto} por un total de {total}")
                return total

            except ValueError as e:
                logging.error(f"Error al efectuar la compra {e}")
            
            else:
                logging.warning(f"Error al efectura la compra {e}")

if __name__=="__main__":
    tienda=Tienda()

    inventario_portatil=Producto(nombre="Portatil",precio="12.5",cantidad=5)
    tienda.agregarProducto(inventario_portatil)
    tienda.realizarCompra(nombre_producto="Portatil",cantidad=4)
