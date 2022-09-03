from cuenta import cuenta    # Importamos la clase madre

class cheque(cuenta):        # Se hereda
   # Se crea la clase, con los nuevos atributos 
    def __init__(self, numeroCuenta, nombre, apellido, numCheques, maxRetiro, minRetiro, recargoRetirto ):
        super().__init__(numeroCuenta, nombre, apellido)
        self.numCheques = int(numCheques)   # es porque cuando ingresemos los paquetes, nos aparecer n cajas de texto
        self.chequesPorCobrar = 0
        self.chequesEmitidos = 0
        self.cheques = []
        self.maxRetiro = maxRetiro
        self.minRetiro = minRetiro
        self.recargoRetiro = recargoRetirto/100
        self.totalRecargos = 0
      
    #----------------------------------------------------------------
    #              Funcion que me asigna los cheques
    #----------------------------------------------------------------

    def asignarCheques(self, cheques):    # cheques es un atributo lista
        self.cheques = cheques
        self.chequesPorCobrar = len(cheques)  # Es la cantidad de cheques existente en chequera

    
    def retirarCheque(self, numeroCheque, cantidad):
        self.totalRecargos += cantidad*self.recargoRetiro  
        self.saldo -= cantidad*self.recargoRetiro          # el recargo se lo descontamos al atributo saldo
        self.cheques[numeroCheque] -= cantidad
        if (self.cheques[numeroCheque]==0):
            self.cheques.remove(0)
            self.chequesEmitidos +=1
            self.chequesPorCobrar -=1 

    def __str__(self):  # imprimimos los atributos de la clase (informe general)
        cadena = "Numero de cuenta: {}\nNombre: {}\nApellido: {}\nSaldo: L.{}\nRango de Retiro por cheque: [ {} , {} ]\nCheques por Cobrar: {}\nRecargo por Retiro: {}%\nTotal Recargo por retiros: {}\nCheques Emitidos: {}".format(self.numeroCuenta,self.nombre,self.apellido,round(self.saldo,2),self.maxRetiro,self.minRetiro,self.cheques,self.recargoRetiro*100,round(self.totalRecargos,2),self.chequesEmitidos)
        return cadena