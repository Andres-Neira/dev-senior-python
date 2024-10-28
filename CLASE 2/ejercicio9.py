'''5. Ejercicio: Verificación de Año Bisiesto 📅
Escribe un programa que solicite un año al usuario y
determine si es un año bisiesto. Un año es bisiesto
si es divisible por 4 pero no por 100,
a menos que también sea divisible por 400.

Instrucciones:
Solicita el año al usuario.
Usa operadores aritméticos y lógicos para verificar las condiciones de un año bisiesto.
Muestra un mensaje indicando si el año es o no bisiesto.
Ejemplo de salida:
Ingresa un año: 2024
El año 2024 es bisiesto.'''

año=float(input("Ingrese año = "))
dato=año/4
dato2=año/100
Mod=año%4
Mod1=año%100
mod2=año%400
print(f"dato 1 {dato} dato 2 {dato2}")
print(f"modulo1 {Mod} modulo 2 {Mod1}")

if(Mod==0 and Mod1!=0):
    print(f"el año {año} es bisiesto")
elif(mod2==0):
    print(f"el año {año} es bisiesto")
else:
    print(f" El año {año} no es bisiesto")