'''Escribe un programa que solicite dos números al usuario y realice las siguientes operaciones: suma, resta, multiplicación y división. Muestra los resultados en pantalla.'''

# Solicitamos al usuario que ingrese dos números
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

# Realizamos las operaciones
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

# Mostramos los resultados
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")