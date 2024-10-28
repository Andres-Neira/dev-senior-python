'''4. Ejercicio: Cálculo de Descuento 💸
Crea un programa que calcule el precio final de un producto con descuento.
Solicita al usuario el precio original del producto y el porcentaje de descuento.
El programa debe calcular y mostrar el precio final utilizando operadores aritméticos.

Instrucciones:
Solicita el precio original y el porcentaje de descuento.
Usa operadores aritméticos para calcular el descuento y el precio final.
Muestra el resultado en pantalla.
Ejemplo de salida:
Ingresa el precio original del producto: 100
Ingresa el porcentaje de descuento: 20
El precio final después del descuento es: 80'''

price=float(input("Ingresa el precio original del producto: "))
desc=float(input("Ingresa el porcentaje de descuento: "))

price_end=price*(1-desc/100)
print(f"El precio final después del descuento es: {price_end}")