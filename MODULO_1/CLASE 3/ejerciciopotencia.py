'''3. Ejercicio: Cálculo de Potencias 💥
Escribe un programa que solicite al usuario dos números: la base y el exponente.
El programa debe calcular la potencia utilizando la fórmula:

[ a^{n} = aaa*a \ (n\ veces)]

Instrucciones:
Solicita la base y el exponente al usuario.
Calcula la potencia utilizando el operador ** en Python.
Muestra el resultado en pantalla.
Hazlo ahora sin usar el operador **
Ejemplo de salida:
Ingresa la base: 3
Ingresa el exponente: 4
El resultado de 3^4 es: 81'''
numero=int(input("Digite un numero"))
potencia=int(input("Digite la potencia"))
resut_1=numero**potencia
print(f"el resultado 1 es {resut_1}")
mult=numero
p=1
for p in range(potencia-1):
    mult=mult*numero
print(mult)