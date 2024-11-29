'''Ejercicio 1: Adivina el Número
Escribe un programa que elija un número aleatorio entre 1 y 10.
El programa debe permitir al usuario adivinar el número y
darle pistas si su respuesta es mayor o menor al número secreto.
El programa se detiene cuando el usuario acierta.'''

import random
# Generar un número aleatorio entre 1 y 10
numero_secreto = random.randint(1, 10)
adivinado = False

while not adivinado:
    adivinanza = int(input("Adivina el número (entre 1 y 10): "))
    if adivinanza == numero_secreto:
        print("¡Felicidades! Has adivinado el número 🎉")
        adivinado = True
    elif adivinanza < numero_secreto:
        print("El número es mayor 📈")
    else:
        print("El número es menor 📉")