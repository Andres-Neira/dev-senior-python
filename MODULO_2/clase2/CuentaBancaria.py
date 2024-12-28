class CuentaBancaria:

   def __init__(self,titular,saldo,clave):
      self.titutar=titular
      self._saldo=saldo
      self.__clave=clave

   def depositor(self,cantidadDeposito):
      self._saldo+=cantidadDeposito
      return f'Deposito Exitoso. Saldo actual {self._saldo}'

   def retirar(self,cantidadRetiro):
      if cantidadRetiro>self._saldo:
         return ' Fondos insuficientes'
      self._saldo -= cantidadRetiro
      return f'Retiro exitoso  el saldo actual es {self._saldo}'

   def modificarClave(self,nuevaClave):
      self.__clave=nuevaClave
      return f'Clave modificada de forma exitosa. La nueva clave es : {self.__clave}'

CuentaBancaria1=CuentaBancaria('Andres Neira',1000000,1234)

print(CuentaBancaria1.titutar)
print(CuentaBancaria1._saldo)

print(CuentaBancaria1.depositor(500000))
print(CuentaBancaria1.depositor(500000))

print(CuentaBancaria1.retirar(100000))

print(CuentaBancaria1.modificarClave(10000000))
