'''Ejercicio 3: Comparador de Números
Escribe un programa que solicite dos números al usuario
y determine si el primer número es mayor, menor o igual
al segundo. Muestra el resultado en pantalla usando operadores relacionales.'''

number1=float(input("Escriba un numero a comparar"))
number2=float(input("escriba el segundo numero a comparar"))

if(number1>number2):
    print(f"el numero  {number1} es mayor que {number2}")
elif(number1<number2):
    print(f" El numero {number1} es menor que {number2}")
else:
    print(" los numeros son iguales")

    