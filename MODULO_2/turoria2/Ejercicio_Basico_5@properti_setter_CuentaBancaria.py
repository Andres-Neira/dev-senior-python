class CuentaBancaria:

    def __init__(self,saldo):
        self.__saldo= saldo
# property sirve para acceder a atributos privados de manera sencilla
    @property
    def saldo(self):
        return self.saldo
# el metodo setter funicona para actualizar directamente las variables privadas
    @saldo.setter
    def saldo(self, deposito):
        if deposito > 0:
            self.__saldo = deposito
        else:
            print("La cantidad no es valida")

    def depositar(self,deposito):
        self.__saldo+=deposito
        print( f'Se deposito ${deposito}   SALDO : ${self.__saldo}')

    def retirar(self,retiro):
        if self.__saldo >= retiro:
            self.__saldo-=retiro
            print( f' Se retito ${retiro} SALDO : ${self.__saldo}')
        else:
            print(f' saldo insuficiente para su retiro ${retiro}')
    def __calcularInteres(self):
        interes=self.__saldo*0.05
        return f'el interes de 5% es ${interes} con un saldo de ${self.__saldo}'

    def mostrarInteres(self):
        return self.__calcularInteres()

cuenta=CuentaBancaria(0)
cuenta.depositar(1000)
cuenta.saldo=1000
cuenta.retirar(500)
print(cuenta.mostrarInteres())