'''4. Ejercicio: Suma de Números Naturales ➕
La suma de los primeros ( n ) números naturales se calcula con la fórmula:

[{\displaystyle \sum _{k=1}^{n}k={\frac {n(n+1)}{2}}}]

Instrucciones:
Pide al usuario un número entero positivo.
Usa la fórmula para calcular la suma de los primeros ( n ) números naturales.
Muestra el resultado en pantalla.
Ejemplo de salida:
Ingresa un número: 10
La suma de los primeros 10 números naturales es: 55'''

numero=int(input("digite el numero natural"))
inc=0
for n in range(numero+1):
    inc=inc+n
    print(n)
print(inc)
