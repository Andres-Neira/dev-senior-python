'''1. Ejercicio: Serie de Fibonacci 🌀
La serie de Fibonacci es una secuencia de números en la que cada número 
es la suma de los dos anteriores, comenzando con 0 y 1. La fórmula de Fibonacci es:

[ F(n) = F(n-1) + F(n-2) ]

Instrucciones:
Escribe un programa que solicite al usuario cuántos términos de la serie de Fibonacci desea calcular.
Usa un bucle for o while para calcular y mostrar los términos de la serie.
Ejemplo de salida:
¿Cuántos términos de la serie de Fibonacci deseas? 7
0, 1, 1, 2, 3, 5, 8'''

num=int(input("Digite un número : "))
i=0
for i in range(num):
    if i==0:
        a=0
        b=0
        c=a+b
        print(c)
    elif i==1:
        a=i-1
        b=i
        c=a+b
        print(c)
    else:
        c=a+b
        print(c)
        a=b
        b=c
       



    
        
