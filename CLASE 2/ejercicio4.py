'''Ejercicio 4: Verificación de Edad
Crea un programa que pida la edad del usuario y
verifique si es mayor de edad (18 años o más).
Usa operadores lógicos para determinar si la persona puede votar o no.'''

age=int(input("Digite su edad"))
if(age<18):
    print(f"su edad es {age} por lo tanto es menor de edad, no puede votar")
else:
    print(f"se edad es {age} es mayor de edad , usted puede votar")
