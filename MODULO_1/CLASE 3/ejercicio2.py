'''Ejercicio 2: Calculadora de Notas
Crea un programa que pida al usuario su calificación (entre 0 y 100)
Dependiendo del valor ingresado, el programa debe mostrar si el estudiante ha aprobado
(60 o más) o ha reprobado (menos de 60). Usa condicionales para determinar el resultado.'''

calif=int(input("Digete la nota entre 0-100 : "))
aprobado=False
if calif >= 60:
    print(f"felicidades aporbo su nota {calif} es mayor o igual a 60")
    aprobado=True
else:
    print(f"Reprobo su nota {calif} es menor a 60")
    aprobado=False
