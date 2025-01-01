'''4. Clase `CuentaBancaria`: Implementa una clase `CuentaBancaria`
con: Atributos: `saldo`.
Métodos: `depositar(cantidad)` y `retirar(cantidad)`
con validaciones. Si intentas retirar más del saldo disponible, debe imprimir: `"Fondos insuficientes."`  '''

class CuentaBancaria:
    def __init__(self, Saldo):
        self.saldo = Saldo

    def depositar(self,monto):
        self.saldo=self.saldo+monto
        print('Deposito exitoso')

    def retirar(self, retiro):
        if retiro > self.saldo:
            print('Saldo insuficiente')
        else:
            self.saldo-=retiro
            print(f'Retiro exitoso {retiro} saldo disponible {self.saldo}')

cuenta=CuentaBancaria(0)
print(f' El saldo actual de la cuenta bancaria es {cuenta.saldo}')
cuenta.depositar(1000000)
print(f' El saldo actual de la cuenta bancaria es {cuenta.saldo}')
cuenta.retirar(5000000)
cuenta.retirar(50000)