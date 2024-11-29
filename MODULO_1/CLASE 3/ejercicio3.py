'''Ejercicio 3: Números Pares e Impares
Escribe un programa que recorra los números del 1 al 20 e imprima si cada número es par o impar.
Usa un bucle for para recorrer los números y condicionales para determinar si un número es par o impar.'''

numero=1
print("inicio")
for numero in range(1,21,1):
    print(numero)
    if numero%2==0:
        print("el numero es par")
    else:
        print("El numero es impar")
