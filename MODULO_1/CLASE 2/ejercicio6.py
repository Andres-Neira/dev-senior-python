'''2. Ejercicio: Verificación de Edad y País 🌏
Escribe un programa que solicite al usuario su edad y su país de residencia. El programa debe verificar si el usuario tiene al menos 18 años y si vive en un país específico (por ejemplo, "España") para determinar si puede votar en las elecciones nacionales.

Instrucciones:
Solicita la edad y el país del usuario.
Usa operadores relacionales para verificar si la edad es mayor o igual a 18.
Utiliza operadores lógicos (and, or) para combinar condiciones y validar la elegibilidad.

EJEMPLO DE SALIDA
Ingresa tu edad: 20
Ingresa tu país: España
Puedes votar en las elecciones nacionales.'''

age=int(input("Ingresa tu edad"))
country=input("ingresa tu país")
if(age<18):
    print(f"su edad es {age} por lo tanto es menor de edad, no puede votar")
else:
    print(f"se edad es {age} es mayor de edad , usted puede votar")
