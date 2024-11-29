'''Ejercicio 4: Menú de Opciones
Crea un programa que muestre un menú de opciones simples
(por ejemplo, "1. Saludar", "2. Despedirse", "3. Salir")
y permita al usuario seleccionar una opción. Dependiendo de la opción,
el programa debe ejecutar una acción específica o salir del bucle
si el usuario elige "Salir". Usa un bucle while para mostrar el menú hasta que el usuario decida salir.'''

menu=""
while menu != "3":
    menu=input(" Bienvenido al Menu \n selecciones una opción \n1.Saluda\n2.Despedice\n3.Salir \nopcion? : ")
    if menu=="1":
        print("hola")
    elif menu=="2":
        print("adios")