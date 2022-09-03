from cuenta import cuenta   # importamos la clase madre

class saldoFijo(cuenta):     # Se hereda
    # Creamos la clase con sus atributos 
    def __init__(self, numeroCuenta, nombre, apellido, monto):
        super().__init__(numeroCuenta, nombre, apellido)
        self.saldo = monto
        # Como el enunciado nos dice que es en funcion a la cantidad, por eso lo tomamos asi con estas condiciones
        # dichas tasas son mensuales
        if(monto<10000):       
            self.tasaInteres = 0.02
        elif monto<100000:
            self.tasaInteres = 0.04
        elif monto<1000000:
            self.tasaInteres = 0.06
        else:
            self.tasaInteres = 0.1
        self.interesDisponible = 0
        self.interesGenerado = 0
        self.interesRetirado = 0 
    # Actualizara todos los intereses de todas las cuentas de saldo fijo que haya.
    def asignarInteres(self):
        self.interesGenerado = (self.saldo + self.interesDisponible)*self.tasaInteres 
        self.interesDisponible += self.interesGenerado
        self.depositos += 1
    # Como el saldo no se puede retirar, ya que es una cuenta a saldo fijo, entonces:
    # lo que se retirara es lo que haya en el atributo interes disponible
    def retirarIntereses(self, cantidad):
        if cantidad>self.interesDisponible:
            return False
        else:
            self.interesDisponible -= cantidad
            self.interesRetirado += cantidad
            self.retiros += 1
            return True

    def __str__(self):
        cadena = "Numero de cuenta: {}\nNombre: {}\nApellido: {}\nSaldo Fijo: L.{}\nPorcentaje de Interes: {}%\nInteres Disponible: {}\nInteres Retirado: {}".format(self.numeroCuenta,self.nombre,self.apellido,round(self.saldo,2),self.tasaInteres*100,round(self.interesDisponible,2),self.interesRetirado)
        return cadena