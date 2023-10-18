## Ejercicio Práctico: Sistema de Pago


#### Descripción:

El objetivo del sistema de pago es permitir crear transacciones que reflejen la realización de un pago. Cada transacción se puede encontrar en varios estados:
1. En proceso: Es el estado por defecto cuando se inicia un pago
2. Pagada: Cuando el proceso de pago se realiza satisfactoriamente
3. Rechazada: Si durante el proceso de pago, algo no funciona correctamente, el proceso de la transacción pasa a ser rechazada.

La transacción, además puede realizarse a través de diferentes métodos de pago (tarjeta de crédito, transferencia bancaria y PayPal). Cada método de pago debe calcular el monto final a pagar aplicando ciertos descuentos y reglas específicas.

El proceso de pago, se realiza en un sistema diferente, y por ende debe generar un comprobante de pago específico por cada uno de los tipos de método de pago.

Además, luego de que la transacción se encuentre en un estado definitivo (Pagada o rechazada) debe poder imprimirse un comprobante de transacción.

#### Requisitos:
1. Utiliza herencia para crear una clase base llamada `MetodoPago`.
2. Crea subclases para cada método de pago: `TarjetaCredito`, `TransferenciaBancaria` y `PayPal`.
3. Usa clases abstractas y métodos abstractos para definir un método `calcular_monto_final()` que debe ser implementado en cada subclase.
4. Implementa polimorfismo para que cada método de pago tenga su propia forma de calcular el monto final y generar un comprobante.
5. Define una interfaz `Imprimible` con un método `imprimir_comprobante()`, que debe ser implementada en transaccion y en metodo pago.
6. Se debe crear un menú que permita la creación de transacciones y además que permita la visualización de las transacciones realizadas en el pasado

#### Pautas para la Implementación:
- Cada método de pago debe tener una tasa de descuento diferente. (Paypal: 5%, Tarjeta de Credito: 0%, transferencia Bancaria: 7%)
- El monto inicial será una propiedad de la clase transaccion.
- El método `imprimir_comprobante()` de la clase `transacción` debe mostrar: 
  - En caso de estar aprobada: el monto inicial, el descuento aplicado, el nombre del método de pago utilizado, el monto final y el estado de la transacción.
  - En caso de estar rechazada: El método de pago que se utilizó para hacer el pago y el motivo por el cuál se rechazó. 
- El método `imprimir_comprobante()` de la clase `MetodoPago` debe mostrar el nombre del método de pago, el porcentaje de descuento que aplica y el estado de la transacción.
- Cada transacción debe tener un identificador único, consecutivo, que debe ser aumentado luego de crear una transacción
