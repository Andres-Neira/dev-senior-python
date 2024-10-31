'''2. Ejercicio: Cálculo del Factorial 🎯
El factorial de un número ( n ) (representado como ( n! )) 
es el producto de todos los enteros positivos hasta ( n ). La fórmula es:

[ n! = n*(n-1)(n-2) \ldots* 1 ]

Instrucciones:
Crea un programa que pida un número al usuario y calcule su factorial usando un bucle.
Muestra el resultado en pantalla.
Ejemplo de salida:
Ingresa un número para calcular su factorial: 5
El factorial de 5 es: 120'''

numero=int(input("Digite un numero"))
n=numero
mult=n
for n in range(numero,1,-1):
    n_1=n-1
    mult=mult*n_1
    print(f"el numero es {n_1} la mult {mult}")
print(mult)
