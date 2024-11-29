'''5. Ejercicio: Calcular la Hipotenusa de un Triángulo Rectángulo 📐
Usa el Teorema de Pitágoras para calcular la hipotenusa de un triángulo rectángulo. La fórmula es:

[ c = \sqrt{a^2 + b^2} ]

donde ( a ) y ( b ) son los catetos del triángulo, y ( c ) es la hipotenusa.

Instrucciones:
Solicita al usuario los valores de los catetos.
Calcula la hipotenusa usando la fórmula.
Muestra el resultado en pantalla.
Usa la funcion sqrt de la libreria math de python como en el ejemplo para importar librerias.
Ejemplo de salida:
Ingresa el valor del primer cateto: 3
Ingresa el valor del segundo cateto: 4
La hipotenusa del triángulo es: 5.0'''

import math as mt

cata=float(input("digite cateto a"))
catb=float(input("digite cateto b"))
hipo=mt.sqrt((cata**2+catb**2))
print(f" la hipotenusa es : {hipo}")