#Ejercicio explicando las excepciones multiples
def division_segura():
    try:
        numerador=int(input('Ingrese el valor del numerador'))
        denominador=int(input('Ingrese el valor del denominador'))
        resultado=numerador/denominador
        print(f'El resultado del division entre { numerador} y {denominador} es igual a {resultado}')

    except (ZeroDivisionError,ValueError) as e:
        print(f' Error : {e}')

division_segura()
division_segura()