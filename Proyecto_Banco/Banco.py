from tkinter import *
from tkinter import messagebox

#-----------------------------------------------------------
#           llamado de las clases construidas
#-----------------------------------------------------------
from cuenta import cuenta
from ahorro import ahorro
from cheques import cheque
from saldoFijo import saldoFijo

#-----------------------------------------------------------
#                Clase de ventana principal
#-----------------------------------------------------------
# ventana que se mostrara al ejecutar el codigo
class VentanaPrincipal:
    # cuentas: es para el llamado de cada ventana
    def __init__(self,cuentas):
        self.cuentas = cuentas
        self.root = Tk()
        self.root.geometry("620x450")
        self.root.resizable(0,0)        # mantiene fija la pantalla, sin estar sujeta a modificaciones
        self.root.title("Banco don Baratón")
        
        self.f1 = Frame(self.root,width=620,height=450)
        self.f1.grid(row=0,column=0)
        foto = PhotoImage(file="b2.png")
        Label(self.f1,image=foto).place(x=0,y=0)
        # Etiquetas de la ventana 
        self.lab1 = Label(self.f1,fg="white",text="Banco Don Baratón",bg="black", padx=10, pady=5, font=("Times New Roman", 20))
        self.lab1.place(x=220,y=5)
        self.lab3 = Label(self.f1,fg="white",text="Donde más obtiene el que menos tiene    ",bg="black",padx=9,pady=3,font=("Times New Roman", 11))
        self.lab3.place(x=200,y=40)
        self.lab2 = Label(self.f1,fg = 'white' ,text= "Menu Principal",bg = "black", padx=45, pady=10, font=("Times New Roman", 14))
        self.lab2.place(x=222,y=55)
        
        # Botones de selección
        self.b1 = Button(self.f1, text = "Apertura de Cuenta",command=self.crearCuenta,padx=5, pady=5)
        self.b2 = Button(self.f1, text = "Inhabilitar Cuenta",command=self.deshabilitarCuenta,padx=5, pady=5)
        self.b3 = Button(self.f1, text = "Realizar Deposito" ,command=self.realizarDeposito,padx=5, pady=5)
        self.b4 = Button(self.f1, text = "Realizar Retiro" ,command=self.realizarRetiro,padx=5, pady=5)
        self.b5 = Button(self.f1, text = "Informe General de Cuentas",command=self.InformeCuentas,padx=5, pady=5)
        self.b6 = Button(self.f1, text = "Cuentas Inactivas",command=self.cuentasInactivas,padx=5, pady=5)
        self.b7 = Button(self.f1, text = "Cuentas Activas" ,command=self.cuentasActivas,padx=5, pady=5)
        self.b8 = Button(self.f1, text = "Actualizar Intereses en Cuentas de Ahorro",command=self.actualizarInteresesCuentaAhorro,padx=5, pady=5)
        self.b9 = Button(self.f1, text = "Actualizar Intereses en cuentas de Saldo Fijo",command=self.actualizarInteresesSaldoFijo,padx=5, pady=5)
        self.b10 = Button(self.f1, text = "Nuevo Paquete de cheques",command=self.paqueteCheques,padx=5, pady=5)
        self.b1.place(x=240,y=97)
        self.b2.place(x=247,y=133)
        self.b3.place(x=247,y=170)
        self.b4.place(x=257,y=205)
        self.b5.place(x=215,y=240)
        self.b6.place(x=247,y=276)
        self.b7.place(x=253,y=315)
        self.b8.place(x=170,y=352)
        self.b9.place(x=160,y=387)
        self.b10.place(x=220,y=422)

        self.root.mainloop()
    # Todas estas funciones lo unico que hacen es llamar a las otras ventanas y cierran la ventana principal
    def crearCuenta(self):
        self.root.destroy()
        impresion = seleccionVentanaCrearCuenta(self.cuentas) # como una ventana no tiene conocimiento de las cuentas de la otra
                                                     # se le pasa como argumento, para que cada una las pueda tener

    def InformeCuentas(self):
        self.root.destroy()
        impresion = VentanaInformeCuentas(self.cuentas)

    def deshabilitarCuenta(self):
        self.root.destroy()
        impresion = VentanaDeshabilitarCuenta(self.cuentas)

    def realizarDeposito(self):
        self.root.destroy()
        impresion = VentanaGeneraDepositos(self.cuentas)

    def realizarRetiro(self):
        self.root.destroy()
        impresion = SeleccionarRetirarSaldo(self.cuentas)

    def paqueteCheques(self):
        self.root.destroy()
        impresion = VentanaPaqueteCheques(self.cuentas)

    def cuentasActivas(self):
        self.root.destroy()
        impresion = ventanaCuentasActivas(self.cuentas)

    def cuentasInactivas(self):
        self.root.destroy()
        impresion = ventanaCuentasInactivas(self.cuentas)
    
    def actualizarInteresesCuentaAhorro(self):
        for i in self.cuentas[0]:
            if (i.habilitada):
                i.asignarInteres()
        messagebox.showinfo(title="Exito",message="Se actualizaron los intereses de las Cuentas de ahorro")
    
    def actualizarInteresesSaldoFijo(self):
        for i in self.cuentas[2]:
            if(i.habilitada):
                i.asignarInteres()
        messagebox.showinfo(title="Exito",message="Se actualizaron los intereses de las Cuentas de Saldo Fijo")
#--------------------------------------------------------------------------------------------------------
#                            Clase para pedir opción de creación de cuenta 
#--------------------------------------------------------------------------------------------------------
class seleccionVentanaCrearCuenta:
    def __init__(self,cuentas):
        self.cuentas = cuentas
        self.root = Tk()
        self.root.resizable(0,0)
        self.root.title("Banco don Baratón")
        self.f1 = Frame(self.root,width=450,height=300,bg = 'black')
        self.f1.grid(row=0,column=0)
        foto = PhotoImage(file="b3.png")
        Label(self.f1,image=foto).place(x=0,y=0)
        self.l1= Label(self.f1,fg = "white" ,text= "Seleccione la cuenta a Crear:",bg = "black", padx=10, pady=10,font=("Times New Roman", 16))
        self.l1.place(x=140,y=20)
        self.b1 = Button(self.f1, text = "Cuenta de Ahorro",command=self.crearCuentaAhorro,padx=5, pady=5)
        self.b2 = Button(self.f1, text = "Cuenta de Cheques",command=self.crearCuentaCheques,padx=5, pady=5)
        self.b3 = Button(self.f1, text = "Cuenta de Saldo Fijo",command=self.crearCuentaSaldoFijos,padx=5, pady=5)
        self.b4 = Button(self.f1, text = "Regresar al Menu Principal",command=self.regresarVentanaPrincipal,padx=5, pady=5)
        self.b1.place(x=180,y=80)
        self.b2.place(x=173,y=120)
        self.b3.place(x=170,y=160)
        self.b4.place(x=150,y=210)
        self.root.mainloop()

    def crearCuentaAhorro(self):
        self.root.destroy()
        impresion = VentanaCrearCuentaAhorro(self.cuentas)

    def crearCuentaCheques(self):
        self.root.destroy()
        impresion = VentanaCrearCuentaCheques(self.cuentas)

    def crearCuentaSaldoFijos(self):
        self.root.destroy()
        impresion = VentanaCrearCuentaSaldoFijo(self.cuentas)



    def regresarVentanaPrincipal(self):
        self.root.destroy()
        impresion = VentanaPrincipal(self.cuentas)

##########################################################################################################
#--------------------------------------------------------------------------------------------------------
#                            Clase que genera ventana para crear cuenta de ahorro
#--------------------------------------------------------------------------------------------------------

class VentanaCrearCuentaAhorro:
    def __init__(self,cuentas):
        self.cuentas = cuentas
        self.root = Tk()
        self.root.resizable(0,0)
        self.root.title("Banco don Baratón")
        self.f1 = Frame(self.root,width=679,height=413)
        self.f1.grid(row=0,column=0)
        foto = PhotoImage(file="oro.png")
        Label(self.f1,image=foto).place(x=0,y=0)
        self.l1= Label(self.f1,fg = 'black' ,text= "Ingrese los datos del nuevo afiliado:",bg = "#cda434", padx=10, pady=10,font=("Times New Roman", 16))
        self.l1.place(x=226,y=40)
        self.n = Label(self.f1,fg = 'black' ,text= "                               Nombre: ",bg = "#cda434", padx=8, pady=8, font=("Times New Roman", 14))
        self.a = Label(self.f1,fg = 'black' ,text= "                             Apellido: ",bg = "#cda434", padx=10, pady=10, font=("Times New Roman", 14))
        self.i = Label(self.f1,fg = 'black' ,text= "                 %Tasa de interes:",bg = "#cda434", padx=10, pady=10, font=("Times New Roman", 14))
        self.n.place(x=100,y=100)
        self.a.place(x=100,y=137)
        self.i.place(x=100,y=174)
        # variables con las que se accede a cada caja de texto 
        self.varn = StringVar()
        self.vara = StringVar()
        self.vari = StringVar()
        self.cuadron = Entry(self.f1, textvariable=self.varn,width = 30)
        self.cuadroa = Entry(self.f1, textvariable=self.vara,width = 30)
        self.cuadroi = Entry(self.f1,textvariable=self.vari,width=30)  
        self.cuadron.place(x=307,y=100)
        self.cuadroa.place(x=307,y=139)
        self.cuadroi.place(x=307,y=179)
        self.cuadron.config(background="#cda434", fg="black")
        self.cuadroa.config(background="#cda434", fg="black")
        self.cuadroi.config(background="#cda434", fg="black")

        self.b1 = Button(self.f1, text = "Cancelar",padx=5, pady=5,command=self.regresarVentanaPrincipal)
        self.b2 = Button(self.f1, text = "Guardar" ,padx=5, pady=5,command=self.guardarDatos)
        self.b1.place(x=250,y=270)
        self.b2.place(x=410,y=270)
        self.root.mainloop()

    def regresarVentanaPrincipal(self):
        self.root.destroy()
        impresion = VentanaPrincipal(self.cuentas)

    def guardarDatos(self):
        try:                             #try: bloque le permite probar un bloque de código en busca de errores.
            nom = self.cuadron.get()
            ap  = self.cuadroa.get()
            ti  = float(self.cuadroi.get())

            if (nom=="" or ap==""):
                messagebox.showwarning(title="Error",message="No pueden quedar campos vacios")
            else:
                 campos = ahorro(len(self.cuentas[0]) + len(self.cuentas[1]) + len(self.cuentas[2]) +1,nom,ap,ti)
                 self.cuentas[0].append(campos)
                 messagebox.showinfo(title="Exito",message="Cuenta Creada con Exito, Su numero de cuenta es: {}".format(len(self.cuentas[0]) + len(self.cuentas[1]) + len(self.cuentas[2])))
                 self.regresarVentanaPrincipal()
        except:                        #except: bloque le permite manejar el error.
            messagebox.showwarning(title="Error",message="Ingrese un número")

#--------------------------------------------------------------------------------------------------------
#                            Clase que genera ventana para crear cuenta de cheques
#--------------------------------------------------------------------------------------------------------

class VentanaCrearCuentaCheques:
    def __init__(self,cuentas):
        self.cuentas = cuentas
        self.root = Tk()
        self.root.resizable(0,0)
        self.root.title("Banco don Baratón")
        self.f1 = Frame(self.root,width=679,height=413,bg = 'black')
        self.f1.grid(row=0,column=0)
        foto = PhotoImage(file="oro.png")
        Label(self.f1,image=foto).place(x=0,y=0)
        self.l1= Label(self.f1,fg = 'black' ,text= "Ingrese los datos del nuevo afiliado:",bg = "#cda434", padx=10, pady=10,font=("Times New Roman", 16))
        self.l1.place(x=226,y=40)
        self.n = Label(self.f1,fg = 'black' ,text= "                               Nombre: ",bg = "#cda434", padx=8, pady=8, font=("Times New Roman", 14))
        self.a = Label(self.f1,fg = 'black' ,text= "                             Apellido: ",bg = "#cda434", padx=10, pady=10, font=("Times New Roman", 14))
        self.montoMax = Label(self.f1,fg = 'black' ,text= "    Monto mínimo por retiro :",bg = "#cda434", padx=10, pady=10, font=("Times New Roman", 14))
        self.montoMin = Label(self.f1,fg = 'black' ,text= "   Monto máximo por retiro :",bg = "#cda434", padx=10, pady=10, font=("Times New Roman", 14))
        self.porcentretiro = Label(self.f1,fg = 'black' ,text= "           %Recargo por retiro :",bg = "#cda434", padx=10, pady=10, font=("Times New Roman", 14))
        self.Ncheques = Label(self.f1,fg = 'black' ,text= "            Número de cheques :",bg = "#cda434", padx=10, pady=10, font=("Times New Roman", 14))
        self.n.place(x=100,y=100)
        self.a.place(x=100,y=137)
        self.montoMax.place(x=100,y=174)
        self.montoMin.place(x=100,y=215)
        self.porcentretiro.place(x=100,y=256)
        self.Ncheques.place(x=100,y=297)
        self.varn = StringVar()
        self.vara = StringVar()
        self.varmax = StringVar()
        self.varmin = StringVar()
        self.varpret = StringVar()
        self.varNcheq = StringVar()
        self.cuadron = Entry(self.f1, textvariable=self.varn,width = 30)
        self.cuadroa = Entry(self.f1, textvariable=self.vara,width = 30)
        self.cuadroMax = Entry(self.f1,textvariable=self.varmax,width=5)
        self.cuadroMin = Entry(self.f1,textvariable=self.varmin,width=5)
        self.cuadroPretiro = Entry(self.f1,textvariable=self.varpret,width=5)
        self.cuadroNcheq = Entry(self.f1,textvariable=self.varNcheq,width=5)
        self.cuadron.place(x=307,y=105)
        self.cuadroa.place(x=307,y=143)
        self.cuadroMax.place(x=420,y=179)
        self.cuadroMin.place(x=420,y=220)
        self.cuadroPretiro.place(x=420,y=261)
        self.cuadroNcheq.place(x=420,y=302)
        self.cuadron.config(background="#cda434", fg="black")
        self.cuadroa.config(background="#cda434", fg="black")
        self.cuadroMax.config(background="#cda434", fg="black")
        self.cuadroMin.config(background="#cda434", fg="black")
        self.cuadroPretiro.config(background="#cda434", fg="black")
        self.cuadroNcheq.config(background="#cda434", fg="black")

        self.b1 = Button(self.f1, text = "Cancelar",command=self.regresarVentanaPrincipal,padx=5, pady=5)
        self.b2 = Button(self.f1, text = "Guardar",command=self.guardarDatos,padx=5, pady=5)
        self.b1.place(x=240,y=350)
        self.b2.place(x=410,y=350)

        self.root.mainloop()

    def regresarVentanaPrincipal(self):
        self.root.destroy()
        impresion = VentanaPrincipal(self.cuentas)

    def guardarDatos(self):
        try:
            nom = self.cuadron.get()
            ap  = self.cuadroa.get()
            max = float( self.cuadroMax.get())
            min = float( self.cuadroMin.get())
            pr  = float( self.cuadroPretiro.get())
            nc  = float( self.cuadroNcheq.get())
            if (nom=="" or ap==""):
                messagebox.showwarning(title="Error", message="Tiene campos vacios")    
            else:  
                camp = cheque(len(self.cuentas[0]) + len(self.cuentas[1]) + len(self.cuentas[2]) + 1, nom, ap, nc, max, min, pr)  
                self.cuentas[1].append(camp)
                messagebox.showinfo(title="Exito", message="Cuenta Creada con Exito, Su numero de cuenta es: {}".format(len(self.cuentas[0]) + len(self.cuentas[1]) + len(self.cuentas[2])))
                self.regresarVentanaPrincipal()
        except:
            messagebox.showwarning(title="Error", message="Ingrese un numero")
#--------------------------------------------------------------------------------------------------------
#                      Clase que genera ventana para crear cuenta de Saldo fijos
#--------------------------------------------------------------------------------------------------------

class VentanaCrearCuentaSaldoFijo:
    def __init__(self,cuentas):
        self.cuentas = cuentas
        self.root = Tk()
        self.root.resizable(0,0)
        self.root.title("Banco don Baratón")
        self.f1 = Frame(self.root,width=679,height=413,bg = 'black')
        self.f1.grid(row=0,column=0)
        foto = PhotoImage(file="oro.png")
        Label(self.f1,image=foto).place(x=0,y=0)
        self.l1= Label(self.f1,fg = 'black' ,text= "Ingrese los datos del nuevo afiliado:",bg = "#cda434", padx=10, pady=10,font=("Times New Roman", 16))
        self.l1.place(x=226,y=40)
        self.n = Label(self.f1,fg = 'black' ,text= "                               Nombre: ",bg = "#cda434", padx=8, pady=8, font=("Times New Roman", 14))
        self.a = Label(self.f1,fg = 'black' ,text= "                             Apellido: ",bg = "#cda434", padx=10, pady=10, font=("Times New Roman", 14))
        self.montoIn = Label(self.f1,fg = 'black' ,text= "                     Monto Inicial :",bg = "#cda434", padx=10, pady=10, font=("Times New Roman", 14))
        self.n.place(x=100,y=100)
        self.a.place(x=100,y=137)
        self.montoIn.place(x=100,y=174)
        self.varn = StringVar()
        self.vara = StringVar()
        self.varMontI = StringVar()
        self.cuadron = Entry(self.f1, textvariable=self.varn,width = 30)
        self.cuadroa = Entry(self.f1, textvariable=self.vara,width = 30)
        self.cuadroMonInic = Entry(self.f1,textvariable=self.varMontI,width=20)
        self.cuadron.place(x=307,y=105)
        self.cuadroa.place(x=307,y=143)
        self.cuadroMonInic.place(x=350,y=179)
        self.cuadron.config(background="#cda434", fg="black")
        self.cuadroa.config(background="#cda434", fg="black")
        self.cuadroMonInic.config(background="#cda434", fg="black")

        self.b1 = Button(self.f1, text = "Cancelar",command=self.regresarVentanaPrincipal,padx=5, pady=5)
        self.b2 = Button(self.f1, text = "Guardar",command=self.guardarDatos,padx=5, pady=5)
        self.b1.place(x=240,y=250)
        self.b2.place(x=410,y=250)
        self.root.mainloop()

    def regresarVentanaPrincipal(self):
        self.root.destroy()
        impresion = VentanaPrincipal(self.cuentas)

    def guardarDatos(self):
        try:
            nom = self.cuadron.get()
            ap  = self.cuadroa.get()
            mi = float( self.cuadroMonInic.get())
            
            if (nom=="" or ap==""):
                messagebox.showwarning(title="Error", message="Tiene campos vacios")    
            else:  
                camp = saldoFijo(len(self.cuentas[0]) + len(self.cuentas[1]) + len(self.cuentas[2]) + 1, nom, ap,mi)  
                self.cuentas[2].append(camp)
                messagebox.showinfo(title="Exito", message="Cuenta Creada con Exito, Su numero de cuenta es: {}".format(len(self.cuentas[0]) + len(self.cuentas[1]) + len(self.cuentas[2])))
                self.regresarVentanaPrincipal()
        except:
            messagebox.showwarning(title="Error", message="Ingrese un numero")
    
#--------------------------------------------------------------------------------------------------------
#                        Clase que genera ventana para ver informe de cuentas
#--------------------------------------------------------------------------------------------------------
##########################################################################################################
class VentanaInformeCuentas:
    def __init__(self,cuentas):
        self.cuentas = cuentas
        self.root = Tk()
        self.root.resizable(0,0)
        self.root.title("Banco Don Baratón")
        self.f1 = Frame(self.root, width = 500, height = 500, bg = "gray",padx=5)
        self.f1.grid(row = 0, column = 0)
        foto = PhotoImage(file="im5.png")
        Label(self.f1,image=foto).place(x=0,y=0)
        self.b1 = Button(self.f1, text = "Volver al Menu Principal"  , command = self.regresar, padx=5, pady=5)
        self.b1.grid(row=0, column=2,pady=(10, 0))
        self.l1= Label(self.f1,fg = 'white' ,text= "Cuentas de Ahorro",bg = "gray", padx=10, pady=10,font=("Times New Roman", 16))
        self.l1.grid(row=1,column=0)
        self.l2= Label(self.f1,fg = 'white' ,text= "|",bg = "gray", padx=10, pady=10,font=("Times New Roman", 16))
        self.l2.grid(row=1,column=1)
        self.lbs1 = []
        for i in range(len(self.cuentas[0])):
            self.lbs1.append(Label(self.f1,fg = 'white' ,text= cuentas[0][i].__str__(),bg = "gray", padx=10, pady=10,font=("Times New Roman", 12)))
            self.lbs1[i].grid(row=i+2,column=0)
        self.l3= Label(self.f1,fg = 'white' ,text= "Cuentas de Cheques",bg = "gray", padx=10, pady=10,font=("Times New Roman", 16))
        self.l3.grid(row=1,column=2)
        self.lbs2 = []
        for i in range(len(self.cuentas[1])):
            self.lbs2.append(Label(self.f1,fg = 'white' ,text= cuentas[1][i].__str__(),bg = "gray", padx=10, pady=10,font=("Times New Roman", 12)))
            self.lbs2[i].grid(row=i+2,column=2)
        self.l4= Label(self.f1,fg = 'white' ,text= "|",bg = "gray", padx=10, pady=10,font=("Times New Roman", 16))
        self.l4.grid(row=1,column=3)
        self.l5= Label(self.f1,fg = 'white' ,text= "Cuentas de Saldo Fijo",bg = "gray", padx=10, pady=10,font=("Times New Roman", 16))
        self.l5.grid(row=1,column=4)
        self.lbs3 = []
        for i in range(len(self.cuentas[2])):
            self.lbs3.append(Label(self.f1,fg = 'white' ,text= cuentas[2][i].__str__(),bg = "gray", padx=10, pady=10,font=("Times New Roman", 12)))
            self.lbs3[i].grid(row=i+2,column=4)
        
        self.root.mainloop()

    def regresar(self):
        self.root.destroy()
        mpresion= VentanaPrincipal(self.cuentas)

#--------------------------------------------------------------------------------------------------------
#                        Clase que genera ventana para inhabilitar cuenta
#--------------------------------------------------------------------------------------------------------

class VentanaDeshabilitarCuenta:
    def __init__(self,cuentas):
        self.cuentas = cuentas
        self.root = Tk()
        self.root.resizable(0,0)
        self.root.title("Banco don Baraton")
        self.f1 = Frame(self.root,width=500,height=300,bg = 'gray')
        self.f1.grid(row=0,column=0)
        self.lab1 = Label(self.f1,fg = 'white' ,text= "Procederemos a Inhabilitar Cuenta",bg = "gray", padx=10, pady=10, font=("Times New Roman", 20))
        self.ln = Label(self.f1,fg = 'white' ,text= "Por favor ingrese Numero de Cuenta a inhabilitar: ",bg = "gray", padx=10, pady=10, font=("Times New Roman", 14))
        self.lab1.place(x=100,y=20)
        self.ln.place(x=50,y=80)
        self.varln = StringVar()
        self.cuadron = Entry(self.f1, textvariable=self.varln,width = 5)
        self.cuadron.place(x=370,y=88)
        self.cuadron.config(background="gray", fg="black")
        self.b1 = Button(self.f1, text = "Cancelar"  , command = self.regresarVentanaPrincipal, padx=5, pady=5)
        self.b2 = Button(self.f1, text = "Inhabilitar",command=self.inhabilitar ,padx=5, pady=5)
        self.b1.place(x=150,y=150)
        self.b2.place(x=270,y=150)

        self.root.mainloop()

    def regresarVentanaPrincipal(self):
        self.root.destroy()
        impresion = VentanaPrincipal(self.cuentas)

    def inhabilitar(self):
        try:
            n=float(self.cuadron.get())
            encontrada = False     # si no la encuentra es por que no existe
            for i in self.cuentas:  # filas 
                for j in i:         # columnas
                    if (j.numeroCuenta == n):
                        encontrada = True
                        if(j.habilitada):
                            j.habilitada = False 
                            messagebox.showinfo(title="Exito", message="Cuenta Inhabilitada con Exito")
                            self.regresarVentanaPrincipal()
                        else:
                            messagebox.showwarning(title="Error", message="La Cuenta ya esta inhabilitada")

            if (not encontrada):                
                messagebox.showwarning(title="Error", message="Numero de cuenta no Existe")    
        except:
            messagebox.showwarning(title="Error", message="Ingrese un numero")

#--------------------------------------------------------------------------------------------------------
#                    Clase que genera ventana para realizar depositos a la  cuenta
#--------------------------------------------------------------------------------------------------------

class VentanaGeneraDepositos:
    def __init__(self,cuentas):
        self.cuentas = cuentas
        self.root = Tk()
        self.root.resizable(0,0)
        self.root.title("Banco don Baraton")
        self.f1 = Frame(self.root,width=500,height=300,bg = 'gray')
        self.f1.grid(row=0,column=0)
        foto = PhotoImage(file="im4.png")
        Label(self.f1,image=foto).place(x=0,y=0)
        self.lab1 = Label(self.f1,fg = 'white' ,text= "Realizar Deposito en Cuenta",bg = "black", padx=10, pady=10, font=("Times New Roman", 20))
        self.nc = Label(self.f1,fg = 'white' ,text= "Numero de Cuenta: ",bg = "black", padx=10, pady=10, font=("Times New Roman", 14))
        self.mont = Label(self.f1,fg = 'white' ,text= "Monto a Depositar: ",bg = "black", padx=10, pady=10, font=("Times New Roman", 14))
        self.lab1.place(x=110,y=20)
        self.nc.place(x=100,y=70)
        self.mont.place(x=100,y=100)
        self.varn = StringVar()
        self.varmon = StringVar()
        self.cuadron = Entry(self.f1, textvariable=self.varn,width = 5)
        self.cuadromon = Entry(self.f1, textvariable=self.varmon,width = 10)
        self.cuadron.place(x=240,y=77)
        self.cuadromon.place(x=240,y=107)
        self.cuadron.config(background="black", fg="#03f943")
        self.cuadromon.config(background="black", fg="#03f943")

        self.b1 = Button(self.f1, text = "Cancelar"  , command = self.regresarVentanaPrincipal, padx=5, pady=5)
        self.b2 = Button(self.f1, text = "Depositar",command=self.depositar ,padx=5, pady=5)
        self.b1.place(x=150,y=150)
        self.b2.place(x=250,y=150)

        self.root.mainloop()

    def regresarVentanaPrincipal(self):
        self.root.destroy()
        impresion = VentanaPrincipal(self.cuentas)

    def depositar(self):
        try:
            n=float(self.cuadron.get())   # numero de cuenta
            m=float(self.cuadromon.get()) # monto
            encontrada = False
            for i in self.cuentas:
                for j in i:
                    if (j.numeroCuenta == n):
                        encontrada = True
                        if(j.habilitada):  
                            j.depositar(m)
                            messagebox.showinfo(title="Exito", message="saldo depositado con Exito")
                            self.regresarVentanaPrincipal()
                        else:
                            messagebox.showwarning(title="Error", message="La Cuenta esta inhabilitada")

            if (not encontrada):                
                messagebox.showwarning(title="Error", message="Numero de cuenta no Existe")    
        except:
            messagebox.showwarning(title="Error", message="Ingrese un numero")
#--------------------------------------------------------------------------------------------------------
#         Clase que genera ventana donde seleccionare el tipo de cuenta de la cual retirare saldo
#--------------------------------------------------------------------------------------------------------

class SeleccionarRetirarSaldo:
    def __init__(self,cuentas):
        self.cuentas = cuentas
        self.root = Tk()
        self.root.resizable(0,0)
        self.root.title("Banco don Baratón")
        self.f1 = Frame(self.root,width=450,height=300,bg = 'black')
        self.f1.grid(row=0,column=0)
        foto = PhotoImage(file="b3.png")
        Label(self.f1,image=foto).place(x=0,y=0)
        self.l1= Label(self.f1,fg = 'white' ,text= "Seleccione el tipo de Retiro",bg = "black", padx=10, pady=10,font=("Times New Roman", 16))
        self.l1.place(x=130,y=20)
        self.b1 = Button(self.f1, text = "Retiro Ahorro",command=self.retirarCuentaAhorro,padx=5, pady=5)
        self.b2 = Button(self.f1, text = "Retiro de Cheques",command=self.retirarCheque,padx=5, pady=5)
        self.b3 = Button(self.f1, text = "Retiro de intereses de Saldo Fijo",command=self.retiroIntereses,padx=5, pady=5)
        self.b4 = Button(self.f1, text = "Regresar al Menu Principal",command=self.regresarVentanaPrincipal,padx=5, pady=5)
        self.b1.place(x=170,y=80)
        self.b2.place(x=150,y=120)
        self.b3.place(x=100,y=160)
        self.b4.place(x=120,y=200)

        self.root.mainloop()

    def regresarVentanaPrincipal(self):
        self.root.destroy()
        impresion = VentanaPrincipal(self.cuentas)

    def retirarCuentaAhorro(self):
        self.root.destroy()
        impresion = VentanaRetiroSaldoAhorro(self.cuentas)

    def retirarCheque(self):
        self.root.destroy()
        impresion = VentanaRetiroCheque(self.cuentas)

    def retiroIntereses(self):
        self.root.destroy()
        impresion = VentanaRetiroIntereses(self.cuentas)
        

#--------------------------------------------------------------------------------------------------------
#                       Clase que genera ventana Para realizar retiro cuenta ahorros
#--------------------------------------------------------------------------------------------------------
class VentanaRetiroSaldoAhorro:
    def __init__(self,cuentas):
        self.cuentas = cuentas
        self.root = Tk()
        self.root.resizable(0,0)
        self.root.title("Banco don Baratón")
        self.f1 = Frame(self.root,width=450,height=300,bg = 'black')
        self.f1.grid(row=0,column=0)
        foto = PhotoImage(file="im4.png")
        Label(self.f1,image=foto).place(x=0,y=0)
        self.lab1 = Label(self.f1,fg = 'white' ,text= "Retiro de saldo",bg = "black", padx=10, pady=10, font=("Times New Roman", 20))
        self.ln = Label(self.f1,fg = 'white' ,text= "Numero de Cuenta: ",bg = "black", padx=10, pady=10, font=("Times New Roman", 14))
        self.lm = Label(self.f1,fg = 'white' ,text= "    Monto a Retirar: ",bg = "black", padx=10, pady=10, font=("Times New Roman", 14))
        self.lab1.place(x=140,y=20)
        self.ln.place(x=100,y=60)
        self.lm.place(x=100,y=100)
        self.varln = StringVar()
        self.varlm = StringVar()
        self.cuadroln = Entry(self.f1, textvariable=self.varln,width = 5)
        self.cuadrolm = Entry(self.f1, textvariable=self.varlm,width = 10)
        self.cuadroln.place(x=235,y=70)
        self.cuadrolm.place(x=235,y=110)
        self.cuadroln.config(background="black", fg="#03f943")
        self.cuadrolm.config(background="black", fg="#03f943")
        self.b1 = Button(self.f1, text = "Cancelar" ,command=self.regresarVentanaPrincipal, padx=5, pady=5)
        self.b2 = Button(self.f1, text = "Retirar"  ,command=self.retirarSaldo, padx=5, pady=5)
        self.b1.place(x=130,y=170)
        self.b2.place(x=290,y=170)

        self.root.mainloop()

    def regresarVentanaPrincipal(self):
        self.root.destroy()
        impresion= VentanaPrincipal(self.cuentas)

    def retirarSaldo(self):
        try:
            n=float(self.cuadroln.get())
            m=float(self.cuadrolm.get())
            encontrada = False
            for i in self.cuentas[:2]:   # omitimos la tercer cuenta ya que no podemos sacar dinero de ahí
                for j in i:
                    if (j.numeroCuenta == n):
                        encontrada = True
                        if(j.habilitada):
                            if(j.retirar(m)):
                                messagebox.showinfo(title="Exito", message="saldo retirado con Exito")
                                self.regresarVentanaPrincipal()
                            else:
                                messagebox.showwarning(title="Error", message="Monto a retirar mayor que saldo disponible")
                        else:
                            messagebox.showwarning(title="Error", message="La Cuenta esta inhabilitada")
            if (not encontrada):                
                messagebox.showwarning(title="Error", message="Numero de cuenta no Existe")    
        except:
            messagebox.showwarning(title="Error", message="Ingrese un numero")
#--------------------------------------------------------------------------------------------------------
#                       Clase que genera ventana Para realizar retiro en cuenta cheques
#--------------------------------------------------------------------------------------------------------
class VentanaRetiroCheque:
    def __init__(self, cuentas):
        self.cuentas = cuentas
        self.root = Tk()
        self.root.resizable(0,0)
        self.root.title("Banco")
        self.f1 = Frame(self.root, width = 500, height = 500, bg = 'black',padx=25, pady=25)
        self.f1.grid(row = 0, column = 0)
        self.lab1 = Label(self.f1,fg = 'white' ,text= "Retiro de Cheques",bg = "black", padx=10, pady=10, font=("Times New Roman", 20))
        self.lab1.grid(row=0,column = 0, columnspan = 2)
        self.lab1 = Label(self.f1,fg = 'white' ,text= "Cheques Disponibles \n(Si la cantidad disponible es menor al minimo, se retira toda de un solo)",bg = "black", padx=10, pady=10, font=("Times New Roman", 16))
        self.lab1.grid(row=1,column = 0, columnspan = 2)
        c=0
        self.labs = []
        for i in range(len(self.cuentas[1])):
            if(self.cuentas[1][i].chequesPorCobrar>0):
                temp = ""
                for j in range(len(self.cuentas[1][i].cheques)):
                    temp += "Numero de cheque: {} **** Dinero en Cheque: {} \n".format(j, self.cuentas[1][i].cheques[j])
                self.labs.append(Label(self.f1,fg = 'white' ,text= "Numero de Cuenta: {} ; Monto Minimo: {} ; Monto Maximo: {}\n{}".format(self.cuentas[1][i].numeroCuenta, self.cuentas[1][i].maxRetiro,self.cuentas[1][i].minRetiro,  temp) ,bg = "black", padx=10, pady=10, font=("Times New Roman", 14)))
                self.labs[c].grid(row=c+2,column = 0)
                c+=1

        if c==0:
            self.lab1 = Label(self.f1,fg = 'white' ,text= "No hay Cheques para retirar",bg = "black", padx=10, pady=10, font=("Times New Roman", 16))
            self.lab1.grid(row=2,column = 0, columnspan = 2)
        else:
            self.ln = Label(self.f1,fg = 'white' ,text= "Numero de Cuenta a retirar: ",bg = "black", padx=10, pady=10, font=("Times New Roman", 14))
            self.lc = Label(self.f1,fg = 'white' ,text= "Numero de Cheque a Retirar: ",bg = "black", padx=10, pady=10, font=("Times New Roman", 14))
            self.lm = Label(self.f1,fg = 'white' ,text= "Monto a Retirar: ",bg = "black", padx=10, pady=10, font=("Times New Roman", 14))
            self.ln.grid(row=c+2,column=0)
            self.lc.grid(row=c+3,column=0)
            self.lm.grid(row=c+4,column=0)
            self.varln = StringVar()
            self.varlc = StringVar()
            self.varlm = StringVar()
            self.txtln = Entry(self.f1, textvariable=self.varln,width = 5)
            self.txtlc = Entry(self.f1, textvariable=self.varlc,width = 5)
            self.txtlm = Entry(self.f1, textvariable=self.varlm,width = 10)
            self.txtln.grid(row=c+2,column=1)
            self.txtlc.grid(row=c+3,column=1)
            self.txtlm.grid(row=c+4,column=1)
            self.b2 = Button(self.f1, text = "Retirar"  , command = self.retirar, padx=5, pady=5)
            self.b2.grid(row=c+5,column=1, padx=(10, 0),pady=(10, 0))
        self.b1 = Button(self.f1, text = "Cancelar"  , command = self.regresar, padx=5, pady=5)
        self.b1.grid(row=c+5,column=0, padx=(10, 0),pady=(10, 0))
        self.root.mainloop()

    def regresar(self):
        self.root.destroy()
        impresion= VentanaPrincipal(self.cuentas)

    def retirar(self):
        try:
            n=float(self.txtln.get())
            c=int(self.txtlc.get())
            m=float(self.txtlm.get())
            encontrada = False
            for i in self.cuentas[1]:
                if (i.numeroCuenta == n):
                    encontrada = True
                    if(i.habilitada):
                        if c<len(i.cheques):
                            if(i.cheques[c]<i.minRetiro and i.cheques[c]==m):
                                i.retirarCheque(c,m)
                                messagebox.showinfo(title="Exito", message="Monto de cheque retirado con Exito")
                                self.regresar()
                            elif(i.cheques[c]>=i.minRetiro and m>=i.minRetiro and m <=i.maxRetiro):
                                i.retirarCheque(c,m)
                                messagebox.showinfo(title="Exito", message="Monto de cheque retirado con Exito")
                                self.regresar()
                            else:
                                messagebox.showwarning(title="Error", message="Monto Invalido")    
                        else:
                            messagebox.showwarning(title="Error", message="Cheque no Existe")
                    else:
                        messagebox.showwarning(title="Error", message="La Cuenta esta inhabilitada")
            if (not encontrada):                
                messagebox.showwarning(title="Error", message="Numero de cuenta no Existe")    
        except Exception as e:
            print(e)
            messagebox.showwarning(title="Error", message="Ingrese un numero")

#--------------------------------------------------------------------------------------------------------
#                       Clase que genera ventana Para realizar retiro en cuenta cheques
#--------------------------------------------------------------------------------------------------------
class VentanaPaqueteCheques:
    def __init__(self, cuentas):
        self.cuentas = cuentas
        self.root = Tk()
        self.root.resizable(0,0)
        self.root.title("Banco")
        self.f1 = Frame(self.root, width = 500, height = 500, bg = "gray",padx=25,pady=25)
        self.f1.grid(row = 0, column = 0)
        self.lab1 = Label(self.f1,fg = 'white' ,text= "Nuevo Paquete de Cheques",bg = "gray", padx=10, pady=10, font=("Times New Roman", 20))
        self.lab1.grid(row=0,column = 0, columnspan = 2)
        self.ln = Label(self.f1,fg = 'white' ,text= "Numero de Cuenta: ",bg = "gray", padx=10, pady=10, font=("Times New Roman", 14))
        self.ln.grid(row=1,column=0)
        self.varln = StringVar()
        self.txtln = Entry(self.f1, textvariable=self.varln,width = 5)
        self.txtln.grid(row=1,column=1)
        self.b1 = Button(self.f1, text = "Cancelar"  , command = self.regresar, padx=5, pady=5)
        self.b2 = Button(self.f1, text = "Depositar"  , command = self.depositar, padx=5, pady=5)
        self.b1.grid(row=3,column=0, padx=(10, 0),pady=(10, 0))
        self.b2.grid(row=3,column=1, padx=(10, 0),pady=(10, 0))
        self.root.mainloop()

    def regresar(self):
        self.root.destroy()
        impresion= VentanaPrincipal(self.cuentas)

    def depositar(self):
        try:
            n=int(self.txtln.get())
            encontrada = False
            for i in self.cuentas[1]:
                if (i.numeroCuenta == n):
                    encontrada = True
                    if(i.habilitada):
                        if (i.chequesPorCobrar == 0): # no puede agregar mas paquetes si aun hay cheques por cobrar
                            self.root.destroy()
                            impresion = ventanaIngresarPaquete(self.cuentas,n) # n: numero de cuenta 
                        else:
                            messagebox.showwarning(title="Error", message="La Cuenta todavia tiene cheques por cobrar")    
                    else:
                        messagebox.showwarning(title="Error", message="La Cuenta esta inhabilitada")

            if (not encontrada):                
                messagebox.showwarning(title="Error", message="Numero de cuenta no Existe")    
        except Exception as e:
            print(e)
            messagebox.showwarning(title="Error", message="Ingrese un numero")
#--------------------------------------------------------------------------------------------------------
#                       Clase que genera ventana Para realizar paquete en cuenta cheques
#--------------------------------------------------------------------------------------------------------
class ventanaIngresarPaquete:
    def __init__(self, cuentas, n):
        self.n = n
        self.cuentas = cuentas
        self.root = Tk()
        self.root.resizable(0,0)
        self.root.title("Banco")
        self.f1 = Frame(self.root, width = 500, height = 500, bg = 'black',padx=25, pady=25)
        self.f1.grid(row = 0, column = 0)
        self.lab1 = Label(self.f1,fg = 'white' ,text= "Nuevo Paquete de Cheques",bg = "black", padx=10, pady=10, font=("Times New Roman", 20))
        self.lab1.grid(row=0,column = 0, columnspan = 2)
        # cajas de textos
        self.labs=[]
        self.vars=[]
        self.txts=[]
        for i in self.cuentas[1]:
            if (i.numeroCuenta == n):
                for j in range((i.numCheques)):
                    self.labs.append(Label(self.f1,fg = 'white' ,text= "Monto de cheque {}: ".format(j+1),bg = "black", padx=10, pady=10, font=("Times New Roman", 14)))
                    self.labs[j].grid(row=j+1,column=0)
                    self.vars.append(StringVar())
                    self.txts.append(Entry(self.f1, textvariable=self.vars[j],width = 10))
                    self.txts[j].grid(row=j+1,column=1)
                break
        self.b1 = Button(self.f1, text = "Cancelar"  , command = self.regresar, padx=5, pady=5)
        self.b2 = Button(self.f1, text = "Depositar"  , command = self.depositar, padx=5, pady=5)
        self.b1.grid(row=len(self.labs)+1,column=0, padx=(10, 0),pady=(10, 0))
        self.b2.grid(row=len(self.labs)+1,column=1, padx=(10, 0),pady=(10, 0))
        self.root.mainloop()

    def regresar(self):
        self.root.destroy()
        impresion= VentanaPrincipal(self.cuentas)

    def depositar(self):
        try:
            c = []
            for i in range(len(self.labs)):
                c.append(float(self.txts[i].get())) # obtenemos el valor de cada una de las cajas
            for i in self.cuentas[1]:
                if (i.numeroCuenta == self.n):
                    i.asignarCheques(c)
                    messagebox.showinfo(title="Exito", message="Cheques asignados con Exito")
                    self.root.destroy()
                    impresion = VentanaPrincipal(self.cuentas)
        except:
            messagebox.showwarning(title="Error", message="Ingrese un numero")
#--------------------------------------------------------------------------------------------------------
#                 Clase que genera ventana retirar los interese de la cuenta saldo fijo
#--------------------------------------------------------------------------------------------------------
class VentanaRetiroIntereses:
    def __init__(self,cuentas):
        self.cuentas = cuentas
        self.root = Tk()
        self.root.resizable(0,0)
        self.root.title("Banco don Baratón")
        self.f1 = Frame(self.root,width=450,height=300,bg = 'black')
        self.f1.grid(row=0,column=0)
        foto = PhotoImage(file="im4.png")
        Label(self.f1,image=foto).place(x=0,y=0)
        self.lab1 = Label(self.f1,fg = 'white' ,text= "Retiro de intereses",bg = "black", padx=10, pady=10, font=("Times New Roman", 20))
        self.ln = Label(self.f1,fg = 'white' ,text= "Numero de Cuenta a retirar: ",bg = "black", padx=10, pady=10, font=("Times New Roman", 14))
        self.lm = Label(self.f1,fg = 'white' ,text= "                 Monto a Retirar: ",bg = "black", padx=10, pady=10, font=("Times New Roman", 14))
        self.lab1.place(x=150,y=20)
        self.ln.place(x=70,y=70)
        self.lm.place(x=70,y=100)
        self.varln = StringVar()
        self.varlm = StringVar()
        self.cuadroln = Entry(self.f1, textvariable=self.varln,width = 5)
        self.cuadrolm = Entry(self.f1, textvariable=self.varlm,width = 10)
        self.cuadroln.place(x=260,y=77)
        self.cuadrolm.place(x=260,y=110)
        self.cuadroln.config(background="black", fg="#03f943")
        self.cuadrolm.config(background="black", fg="#03f943")
        self.b1 = Button(self.f1, text = "Cancelar" ,command=self.regresarVentanaPrincipal , padx=5, pady=5)
        self.b2 = Button(self.f1, text = "Retirar" ,command=self.retirarIntereses , padx=5, pady=5)
        self.b1.place(x=120,y=160)
        self.b2.place(x=250,y=160)
        self.root.mainloop()

    def regresarVentanaPrincipal(self):
        self.root.destroy()
        impresion = VentanaPrincipal(self.cuentas)

    def retirarIntereses(self):
        try:
            n=float(self.cuadroln.get())
            m=float(self.cuadrolm.get())
            encontrada = False
            for i in self.cuentas[2]:
                if (i.numeroCuenta == n):
                    encontrada = True
                    if(i.habilitada):
                        if(i.retirarIntereses(m)):
                            messagebox.showinfo(title="Exito", message="saldo retirado con Exito")
                            self.regresarVentanaPrincipal()
                        else:
                            messagebox.showwarning(title="Error", message="Monto a retirar mayor que intereses disponible")
                    else:
                        messagebox.showwarning(title="Error", message="La Cuenta esta inhabilitada")
            if (not encontrada):                
                messagebox.showwarning(title="Error", message="Numero de cuenta no Existe")    
        except:
            messagebox.showwarning(title="Error", message="Ingrese un numero")    
#--------------------------------------------------------------------------------------------------------
#                 Clase que genera ventana con cuentas activas
#--------------------------------------------------------------------------------------------------------
class ventanaCuentasActivas:
    def __init__(self, cuentas):
        self.cuentas = cuentas
        self.root = Tk()
        self.root.resizable(0,0)
        self.root.title("Banco")
        self.f1 = Frame(self.root, width = 500, height = 500, bg = 'black',padx=5)
        self.f1.grid(row = 0, column = 0)
        foto = PhotoImage(file="im5.png")
        Label(self.f1,image=foto).place(x=0,y=0)
        self.b1 = Button(self.f1, text = "Regresar al Menu Principal"  , command = self.regresar, padx=5, pady=5)
        self.b1.grid(row=0, column=2,pady=(10, 0))
        self.l1= Label(self.f1,fg = 'white' ,text= "Cuentas de Ahorro Activas",bg = "gray", padx=10, pady=10,font=("Times New Roman", 16))
        self.l1.grid(row=1,column=0)
        self.l2= Label(self.f1,fg = 'white' ,text= "|",bg = "gray", padx=10, pady=10,font=("Times New Roman", 16))
        self.l2.grid(row=1,column=1)
        self.lbs1 = []                # 
        c1 = 0
        for i in range(len(self.cuentas[0])):
            if (cuentas[0][i].habilitada):    
                self.lbs1.append(Label(self.f1,fg = 'white' ,text= cuentas[0][i].__str__(),bg = "gray", padx=10, pady=10,font=("Times New Roman", 12)))
                self.lbs1[c1].grid(row=c1+2,column=0)
                c1 +=1
        self.l3= Label(self.f1,fg = 'white' ,text= "Cuentas de Cheques Activas",bg = "gray", padx=10, pady=10,font=("Times New Roman", 16))
        self.l3.grid(row=1,column=2)
        self.lbs2 = []
        c2 = 0
        for i in range(len(self.cuentas[1])):
            if (cuentas[1][i].habilitada):
                self.lbs2.append(Label(self.f1,fg = 'white' ,text= cuentas[1][i].__str__(),bg = "gray", padx=10, pady=10,font=("Times New Roman", 12)))
                self.lbs2[c2].grid(row=c2+2,column=2)
                c2 +=1
        self.l4= Label(self.f1,fg = 'white' ,text= "|",bg = "gray", padx=10, pady=10,font=("Times New Roman", 16))
        self.l4.grid(row=1,column=3)
        self.l5= Label(self.f1,fg = 'white' ,text= "Cuentas de Saldo Fijo Activas",bg = "gray", padx=10, pady=10,font=("Times New Roman", 16))
        self.l5.grid(row=1,column=4)
        self.lbs3 = []
        c3 = 0
        for i in range(len(self.cuentas[2])):
            if (cuentas[2][i].habilitada):
                self.lbs3.append(Label(self.f1,fg = 'white' ,text= cuentas[2][i].__str__(),bg = "gray", padx=10, pady=10,font=("Times New Roman", 12)))
                self.lbs3[i].grid(row=i+2,column=4)
                c3+=1

        self.root.mainloop()

    def regresar(self):
        self.root.destroy()
        impresion= VentanaPrincipal(self.cuentas)
#--------------------------------------------------------------------------------------------------------
#                 Clase que genera ventana con cuentas inactivas
#--------------------------------------------------------------------------------------------------------
class ventanaCuentasInactivas:
    def __init__(self, cuentas):
        self.cuentas = cuentas
        self.root = Tk()
        self.root.resizable(0,0)
        self.root.title("Banco")
        self.f1 = Frame(self.root, width = 500, height = 500, bg = 'black',padx=5)
        self.f1.grid(row = 0, column = 0)
        foto = PhotoImage(file="im5.png")
        Label(self.f1,image=foto).place(x=0,y=0)
        self.b1 = Button(self.f1, text = "Regresar al Menu Principal"  , command = self.regresar, padx=5, pady=5)
        self.b1.grid(row=0, column=2,pady=(10, 0))
        self.l1= Label(self.f1,fg = 'white' ,text= "Cuentas de Ahorro Inactivas",bg = "gray", padx=10, pady=10,font=("Times New Roman", 16))
        self.l1.grid(row=1,column=0)
        self.l2= Label(self.f1,fg = 'white' ,text= "|",bg = "gray", padx=10, pady=10,font=("Times New Roman", 16))
        self.l2.grid(row=1,column=1)
        self.lbs1 = []
        c1 = 0
        for i in range(len(self.cuentas[0])):
            if (not cuentas[0][i].habilitada):    
                self.lbs1.append(Label(self.f1,fg = 'white' ,text= cuentas[0][i].__str__(),bg = "gray", padx=10, pady=10,font=("Times New Roman", 12)))
                self.lbs1[c1].grid(row=c1+2,column=0)
                c1 +=1
        self.l3= Label(self.f1,fg = 'white' ,text= "Cuentas de Cheques Inactivas",bg = "gray", padx=10, pady=10,font=("Times New Roman", 16))
        self.l3.grid(row=1,column=2)
        self.lbs2 = []
        c2 = 0
        for i in range(len(self.cuentas[1])):
            if (not cuentas[1][i].habilitada):
                self.lbs2.append(Label(self.f1,fg = 'white' ,text= cuentas[1][i].__str__(),bg = "gray", padx=10, pady=10,font=("Times New Roman", 12)))
                self.lbs2[c2].grid(row=c2+2,column=2)
                c2 +=1
        self.l4= Label(self.f1,fg = 'white' ,text= "|",bg = "gray", padx=10, pady=10,font=("Times New Roman", 16))
        self.l4.grid(row=1,column=3)
        self.l5= Label(self.f1,fg = 'white' ,text= "Cuentas de Saldo Fijo Inactivas",bg = "gray", padx=10, pady=10,font=("Times New Roman", 16))
        self.l5.grid(row=1,column=4)
        self.lbs3 = []
        c3 = 0
        for i in range(len(self.cuentas[2])):
            if (not cuentas[2][i].habilitada):
                self.lbs3.append(Label(self.f1,fg = 'white' ,text= cuentas[2][i].__str__(),bg = "gray", padx=10, pady=10,font=("Times New Roman", 12)))
                self.lbs3[i].grid(row=i+2,column=4)
                c3+=1

        self.root.mainloop()

    def regresar(self):
        self.root.destroy()
        impresion= VentanaPrincipal(self.cuentas)


# Llamado a la clase principal

impresion = VentanaPrincipal([[],[],[]])  

# lista con tres item
[] # cuantas de ahorro: cada cuenta de ahorro se guardara en esta lista
[], # cuentas de cheques: cada cuenta de cheques se guardara en esta lista
[], # cuenta de saldo fijo: cada cuenta de saldo fijos se guardara en esta

#¿Porqué esto?
#R//= 
# porque al pasar las distintas ventanas, una ventana no sabe lo que tiene la otra, entonces se 
# se le va pasando como argumento, entonces cuando se va agregando o modificando una cuenta esta se va
# pasando a traves de cada ventana para que cada ventana pueda acceder a la informacion