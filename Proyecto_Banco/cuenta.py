# ./    CLASE CUENTA CON SUS RESPECTIVOS ATRIBUTOS Y CLASE QUE SE HEREDA (clase madre) # ./

class cuenta:

    def __init__(self,numeroCuenta, nombre, apellido,saldo = 1000,depositos=0,retiros=0):
        self.numeroCuenta = numeroCuenta
        self.nombre = nombre
        self.apellido = apellido
        self.saldo = saldo
        self.depositos = depositos
        self.retiros = retiros
        self.habilitada = True
    # ---------------------------------------------------   
    #       Funcion que me deshabilita la cuenta
    # ---------------------------------------------------  
    # Lo único que hace es que si esta habilitada la desabilita
    def inhabilitar(self):
        if (self.habilitada):
            self.habilitada = not self.habilitada
            
    # ---------------------------------------------------  
    #          Funcion que hace depositos
    # ---------------------------------------------------  
    # Recibe la cantidad, aumenta el saldo y el deposito
    def depositar(self, cantidad):
        self.saldo += cantidad
        self.depositos += 1
    # ---------------------------------------------------  
    #          Funcion que retira saldo
    # ---------------------------------------------------  
    # verifica que la cantidad no sea mayor que el saldo y hace el retiro
    def retirar(self, cantidad):
        if(cantidad > self.saldo):
            return False           # si retorna falso, no hace el retiro entonces muestra el msj de error
        else:
            self.saldo -= cantidad
            self.retiros += 1
            return True            # si retorna verdadero, realiza el retiro

        