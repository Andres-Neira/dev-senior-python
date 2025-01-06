'''3. Método protegido en una clase

- Ejercicio: Agrega un método protegido __calcular_interes` en la clase `CuentaBancaria`
que calcule un 5% de interés sobre el saldo actual.'''

class CuentaBancaria:

    def __init__(self,saldo):
        self._saldo= saldo

    def depositar(self,deposito):
        self._saldo+=deposito
        print( f'Se deposito ${deposito}   SALDO : ${self._saldo}')

    def retirar(self,retiro):
        if self._saldo >= retiro:
            self._saldo-=retiro
            print( f' Se retito ${retiro} SALDO : ${self._saldo}')
        else:
            print(f' saldo insuficiente para su retiro ${retiro}')
    def __calcularInteres(self):
        interes=self._saldo*0.05
        return f'el interes de 5% es ${interes} con un saldo de ${self._saldo}'

    def mostrarInteres(self):
        return self.__calcularInteres()

cuenta=CuentaBancaria(0)
cuenta.depositar(1000)
cuenta.retirar(500)
print(cuenta.mostrarInteres())