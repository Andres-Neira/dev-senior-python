# App que permita dividir dos numeros

def division_cero(numero1,numero2):
    try:
        resultado=numero1/numero2
        print(f' el resultado es {resultado}')
    except ZeroDivisionError as e:
        print('La division entre cero no se puede lograr')
        return None

division_cero(2,0)


def division_cero(numero1,numero2):

        resultado=numero1/numero2
        print(f' el resultado es {resultado}')


division_cero(2,0)