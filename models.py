
from abc import  ABC, abstractmethod
class Transaction:
    pass

class MetodoPago(ABC):

    @abstractmethod()
    def calcular_monto_final(self):
        pass

class Imprimible:

    def imprimir_comprobante(self):
        pass

class TarjetaCredito(MetodoPago,Imprimible):
    pass

class Paypal(MetodoPago,Imprimible):
    pass

class TransferenciaBancaria(MetodoPago,Imprimible):
    pass

