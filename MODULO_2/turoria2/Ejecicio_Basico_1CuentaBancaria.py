'''1. Definir una clase básica con encapsulamiento

- Ejercicio: Crea una clase `CuentaBancaria` con un atributo privado `_saldo`.
Agrega métodos para depositar y retirar dinero,
asegurándote de que no se permita un saldo negativo.  '''

class CuentaBancaria:

    def __init__(self,saldo):
        self.__saldo= saldo

    def depositar(self,deposito):
        self.__saldo+=deposito
        print( f'Se deposito ${deposito}   SALDO : ${self.__saldo}')

    def retirar(self,retiro):
        if self.__saldo >= retiro:
            self.__saldo-=retiro
            print( f' Se retito ${retiro} SALDO : ${self.__saldo}')
        else:
            print(f' saldo insuficiente para su retiro ${retiro}')

cuenta=CuentaBancaria(0)
cuenta.depositar(1000)
cuenta.retirar(500)

