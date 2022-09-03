from cuenta import cuenta  # importa la clase cuenta, la cual es la clase madre

class ahorro(cuenta):          # Aquí hacemos la herencia    

     # se hace la construccion de la clase ahorro y solo se le agrega la tasa de interes y el total de intereses
    def __init__(self, numeroCuenta, nombre, apellido, tasaInteres): 
        super().__init__(numeroCuenta, nombre, apellido)     
        self.tasaInteres = float(tasaInteres/100)
        self.totalIntereses = 0
        
    # ------------------------------------------------------------------
    #     Funcion que asigna los intereses a la cuenta
    # ------------------------------------------------------------------
    # como nos dice actualizara los interese acumulados en cada cuenta, entonces 
    # se les actualiza a todos, asi lo interpretamos
    
    def asignarInteres(self):               
        self.totalIntereses = round(self.saldo*self.tasaInteres + self.totalIntereses,2) # Lo unico  que suma es lo que tenga de saldo por la tasa de interes
        self.depositar(self.saldo*self.tasaInteres)        # realiza el deposito, llamando a la funcion depositos de la clase cuenta
 
    def __str__(self):
        cadena = "Numero de cuenta: {}\nNombre: {}\nApellido: {}\nSaldo: L.{}\nTasa de Interes: {}\nTotal de Depositos: {}\nTotal de Retiros: {}\nTotal de Intereses: {}".format(self.numeroCuenta,self.nombre,self.apellido,round(self.saldo,2),self.tasaInteres,self.depositos,self.retiros,round(self.totalIntereses,2))
        return cadena