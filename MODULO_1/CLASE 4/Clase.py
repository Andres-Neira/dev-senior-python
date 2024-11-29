# codificacion camel case
ventasTotales = 0
#solicitar el numero de productos
numProductos = int(input("Ingrese el numero de productos a gestionar"))

# Listas para almacenar la infomracion
nombres = []
precios = []
cantidades = []

print("ingreso inicial de productos a la tienda")

# capturar informacion y almacenar en listas, segun cantidad
for i in range(numProductos):
    print(f'producto {i+1}: ')
    nombre = input('Ingrese el nombre del producto : ').lower()
    nombres.append(nombre)
    precio = float(input("Ingrese el precio del producto : "))
    if precio > 0:
        precios.append(precio)
    else:
        print('precio erroneo')
    cantidad = int(input("Ingrese la cantidad del producto : "))
    if cantidad>0:
        cantidades.append(cantidad)
    else:
        print('cantidad erronea')


# ciclo menu principal
while True:
    print('\n---MENU GESTION DORGUERIA---')
    print('1. Vender producto')
    print('2. Mostrar inventario')
    print('3. mostrar ventas totales')
    print('4. salir')
    opcion = int(input("Ingrese una opcion : "))

    # ingresar a cada una de las opciones
    if opcion == 1:
        print('\n vender producto')
        nombreVenta = input('Ingrese el nombre del producto a vender').lower()
        cantidadVender = int(input('Ingrese la cantidad a vender'))
        productoEncontrado = False
        #busca nombre de producto
        for i in range(len(nombres)):
            if nombres[i] == nombreVenta:
                productoEncontrado = True
                # mira que la cantidad alcanza para la venta
                if cantidadVender <= cantidades[i]:
                    totalVenta = cantidadVender*precios[i]
                    ventasTotales += ventasTotales
                    cantidades[i]-=cantidadVender
                    # el :.2f cierra los decimales que se quieren ver
                    print(f'Venta realizada total de esta venta es ${totalVenta:2f}')
                    print(f' Quedan {cantidades[i]} unidades de {nombres[i]} en inventario')
                else:
                    print(f'Cantidad insuficiente de inventario, ya que solo tenemos {cantidades[i]}')
                break
        if not productoEncontrado:
            print(f'producto no encontrado en el inventario')
    # mostrar inventario
    elif opcion == 2:
        print('\n Inventario de Productos')
        for i in range(len(nombres)):
            print(f'Producto {i+1} : {nombres[i]}  precio : {precios[i]} cantidad : {cantidades[i]}')
    # mostrar ventas acumuladas
    elif opcion == 3:
        print(f'\n ventas totales acumuladas {ventasTotales:.2f}')
    # finaliza el programa
    elif opcion == 4:
        print('Gracias por usar el sistema de gestiondrogueria dev senior')
        break
    # si ingresa mal el numero solicita
    else:
        print('Opcion invalida, ingresar entre(1-4)')