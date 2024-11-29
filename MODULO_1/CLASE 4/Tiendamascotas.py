productos=[]
clasificacion=[]
Categorias=[]
precios=[]
cantidades=[]
proveedores=[]
fechas=[]
totalVentas=[]
fechaVentas=[]
cantidadVentas=[]
productoVentas=[]
while True:
    print('\n INVENTARIO TIENDA DE MASCOTAS')
    print('1.Registrar nuevo producto')
    print('2.Realizar venta')
    print('3.Mostrar inventario')
    print('4.Consultar registro de ventas')
    print('5.Consultar venta acumulada')
    print('6.Salir')
    print('----------------------------------')
    opcion=input('Registre una opción : ')
# registrar inventario nuevo
    if opcion=='0':
        dato=input('Digite la clasificación')
    elif opcion=='1':
        producto=input('Escriba el nombre del producto : ').lower()
        if len(productos)>0:
            for i in range(len(productos)):
                if producto==productos[i]:
                    print('El producto ya existe')
                    break
                else:
                    categoria=input('escriba la categoria : ').lower()
                    precio=float(input('Ingrese el precio : '))
                    Cantidad=int(input('Cuanto inventario ingresa : '))
                    proveedor=input('Digite el proveedor : ').lower()
                    fecha=input('Registre fecha de creación de producto : ')
                    productos.append(producto)
                    Categorias.append(categoria)
                    precios.append(precio)
                    cantidades.append(Cantidad)
                    proveedores.append(proveedor)
                    fechas.append(fecha)
                    print('Producto registrado exitosamente')
        else:
            print('No hay registro de inventario')
            categoria=input('escriba la categoria : ').lower()
            precio=float(input('Ingrese el precio : '))
            Cantidad=int(input('Cuanto inventario ingresa : '))
            proveedor=input('Digite el proveedor : ').lower()
            fecha=input('Registre fecha de creación de producto : ')
            productos.append(producto)
            Categorias.append(categoria)
            precios.append(precio)
            cantidades.append(Cantidad)
            proveedores.append(proveedor)
            fechas.append(fecha)
            print('Primer Producto registrado exitosamente')
# registrar venta
    elif opcion =='2':
        productoVenta=input('Digite el producto a vender : ').lower()
        if len(productos)>0:
            for i in range(len(productos)):
                if productoVenta==productos[i]:
                    cantidadVenta=int(input('Ingrese la cantidad a vender : '))
                    if cantidades[i]>=cantidadVenta:
                        totalVenta=cantidadVenta*precios[i]
                        ventaAcumulada=+totalVenta
                        fechaVenta=input('Fecha de venta')
                        totalVentas.append(totalVenta)
                        fechaVentas.append(totalVenta)
                        cantidadVentas.append(cantidadVenta)
                        productoVentas.append(productoVenta)
                        cantidades[i]=cantidades[i]-cantidadVenta
                        print(f' Venta exitosa - producto :{productoVenta} cantidad : {cantidadVenta} : precio :{precios[i]} Total :{totalVenta}')
                        print(f'inventario : {cantidades[i]}')
                    else:
                        print(f'el inventario es insuficiente cantidad : {cantidades[i]}')
                        break
        else:
            print('No hay productos registrados')
# mostrar inventario
    elif opcion=='3':
        if len(productos)>0:
            for i in range(len(productos)):
                print(f'Producto :{productos[i]} Categoria : {Categorias[i]} Precio : {precios[i]} Cantidad : {cantidades[i]} Proveedor : {proveedores[i]} Fecha de ingreso : {fechas[i]}')
        else:
            print('No hay inventario registrado')

# mostrar venta
    elif opcion=='4':
        if len(productoVentas)>0:
            print('\n Registro de ventas')
            for i in range(len(productoVentas)):
                print(f'Producto : {productoVentas[i]} Cantidad Vendida : {cantidadVentas[i]} Total Ventas : {totalVentas[i]} Fecha de transacción : {fechaVentas[i]}')
        else:
            print('No se han realizado ventas')
# mostrar total de ventas
    elif opcion=='5':
        if len(productoVentas)>0:
            print(f'\n Venta acumulada : ${ventaAcumulada}')
# salir
    elif opcion=='6':
        print('Gracias por usar el programa inventario de mascotas')
        break
# error en elleción de opción
    else:
        print('\n Elija una opción valida')