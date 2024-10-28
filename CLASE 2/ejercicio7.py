'''Ejercicio: Comparador de Números 🔍
Escribe un programa que pida al usuario tres números.
El programa debe determinar e imprimir cuál de
los tres números es el mayor y cuál es el menor usando operadores relacionales.

Instrucciones:
Solicita tres números al usuario.
Usa operadores relacionales (>, <) para comparar los números y determinar cuál es el mayor y cuál el menor.
Muestra el resultado en pantalla.

Ejemplo de salida:
Ingresa el primer número: 7
Ingresa el segundo número: 3
Ingresa el tercer número: 10
El número mayor es: 10
El número menor es: 3'''

num1=int(input("ingrese el 1 numero"))
num2=int(input("ingrese el 2 numero"))
num3=int(input("ingrese el 3 numero"))
mayor=0
menor=0
if(num1<num2):
    mayor=num2
    menor=num1
    if(num3<mayor):
        mayor=num2
        if(menor<num3):
            menor=num1
        else:
            menor=num3
    else:
        mayor=num3

elif(num2<num1):
    mayor=num1
    menor=num2
    if(num3<mayor):
        mayor=num1
        if(menor<num3):
            menor=num1
        else:
            menor=num3
    else:
        mayor=num3

print(f"el numero mayor es {mayor}")
print(f"el numero menor es {menor}")