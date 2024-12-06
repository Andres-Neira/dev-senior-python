from abc import ABC, abstractmethod

class ProcesoPago:

    @abstractmethod
    def procesoPago(self,cantidad: float)-> None:
        pass

    @abstractmethod
    def reembolsoPago(self,transaccionId: str) -> None:
        pass

class Paypal(ProcesoPago):

    def procesoPago(self, cantidad: float) -> None:
        print(F'Procesando pago de ${cantidad} por paypal')

    def reembolsoPago(self, transaccionId:str) -> None:
        print (f'Reembolsando Id transacción numero {transaccionId}')

class Stripe(ProcesoPago):

    def procesoPago(self, cantidad: float) -> None:
        print(F'Procesando pago de ${cantidad} por stripe')

    def reembolsoPago(self, transaccionId:str) -> None:
        print (f'Reembolsando Id transacción numero {transaccionId}')


if __name__=='__main__':

    procesoPaypal1 = Paypal()
    procesoStripe1 = Stripe()

    procesoPaypal1.procesoPago(500.0)
    procesoPaypal1.reembolsoPago('FEDSDA3D')

    procesoStripe1.procesoPago(200.0)
    procesoStripe1.reembolsoPago('FEDSDA3D')