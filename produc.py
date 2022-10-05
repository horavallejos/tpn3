import os
import os.path
import pickle
import datetime

#### CREAMOS LOS CONSTRUCTORES ####

class op:
    def __init__(self):
        self.pat = ""
        self.cod_prod = 0
        self.fecha = ""
        self.est = ""
        self.pesob = 0
        self.tara = 0

class prod:
    def _init__(self):
        self.cod_prod = 0
        self.nom_prod = ""
        self.est = ""

class silo:
    def __init__(self):
        self.cod_silo = 0
        self.nom_silo = ""
        self.cod_prod = 0
        self.stock = 0

class rubro:
    def __init__(self):
        self.nom_rub = ""
        self.cod_rub = 0

class rubrop:
    def __init__(self):
        self.cod_rub = 0
        self.cod_prod = 0
        self.min = 0.0
        self.max = 0.0

##################### EMBELLECEDORES ####################

#  VARIABLES COLORES
BLUE = '\033[94m'
WHITE = '\033[0m'
RED = '\033[91m'

#  LIMPIAR PANTALLA
def limpia_pant():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")     

############## MODULOS DEL PROGRAMA ################

def validaRangoEntero(nro, min,max):
    try:              
        nro = int(nro)      
        if nro >= min and nro <= max:
            return False 
        else:
            return True  
    except:
        return True  

def validarChar(min, max):
    letra = input("Ingrese opcion ['a'-'f']: ").lower()
    while letra >max or letra <min:
        letra = input("Ingrese opcion ['a'-'f']: ").lower()
    return letra

def validarFecha():
    flag = True
    while flag:
        try:
            fecha = input("Ingresa una fecha en el formato DD/MM/AAAA: ")
            datetime.datetime.strptime(fecha, '%d/%m/%Y')

            #### De paso también formateo la fecha
            mes,anio = fecha.split('/') # separo en día,mes,anio
            if len(dia)==1: # si la longitud ingresada es igual a 1...
                dia=dia.rjust(2,'0') # ... justifico a la derecha y le agrego cero
            if len(mes)==1:
                mes=mes.rjust(2,'0')
            fecha=[dia,mes,anio] # pongo dentro de una lista para pasarla al comando Join
            fecha='/'.join(fecha) # uso el comando Join para unir con una barra de separador
            print("Fecha valida") # de esta manera la fecha siempre tendrá longitud 10
        
            flag = False
        
        except ValueError:
            print("Fecha invalida")
    return fecha

def formatOp(vrOp):
    vrOp.pat= vrOp.pat.ljust(7)
    vrOp.cod_prod = str(vrOp.cod_prod)
    vrOp.cod_prod = vrOp.cod_prod.ljust(2)
    vrOp.fecha = vrOp.fecha.ljust(10)
    vrOp.est = vrOp.est.ljust(1)
    vrOp.pesob = str(vrOp.pesob)
    vrOp.pesob = vrOp.pesob.ljust(5)
    vrOp.tara = str(vrOp.tara)
    vrOp.tara = vrOp.tara.ljust(5)

def formatProd(vrProd):
   vrProd.cod_prod = str(vrProd.cod_prod)
   vrProd.cod_prod = vrProd.cod_prod.ljust(2, ' ')
   vrProd.nom_prod = vrProd.nom_prod.ljust(15, ' ')
   vrProd.est = vrProd.est.ljust(2, ' ')

def formatRub(vrRub):
    vrRub.nom_rub = vrRub.nom_rubro.ljust(20)
    vrRub.cod_rub = str(vrRub.cod_rubro)
    vrRub.cod_rub = vrRub.cod_rubro.ljust(2)

def formatRxP(vrRxP):
    vrRxP.cod_rub = str(vrRxP.cod_rub)
    vrRxP.cod_rub = vrRxP.cod_rub.ljust(2)
    vrRxP.cod_prod = str(vrRxP.cod_prod)
    vrRxP.cod_prod = vrRxP.cod_prod.ljust(2)
    vrRxP.min = str(vrRxP.min)
    vrRxP.min = vrRxP.min.ljust(3)
    vrRxP.max = str(vrRxP.max)
    vrRxP.max = vrRxP.max.ljust(3)
    
def formatSilo(vrSilo):
    vrSilo.cod_silo = str(vrSilo.cod_silo)
    vrSilo.cod_silo = vrSilo.cod_silo.ljust(2)
    vrSilo.nom_silo = vrSilo.nom_silo.ljust(15)
    vrSilo.cod_prod = str(vrSilo.cod_prod)
    vrSilo.cod_prod = vrSilo.cod_prod.ljust(2)
    vrSilo.stock = str(vrSilo.stock)
    vrSilo.stock = vrSilo.stock.ljust(5)

############### RAMA #################

Regpro= prod()
#afProductos alProductos

def Formatearprod(prod):
    prod.cod_prod = str(prod.cod_prod)
    prod.cod_prod = prod.cod_prod.ljust(2)
    prod.nom_prod = prod.nom_prod.ljust(20)
    prod.est = prod.est.ljust(1)
# Inicio contador en 0 para luego asignarlo como codigo incrementandolo antes de asignarlo al campo, hago alta y busco si este ya fue ingresado. En caso de que no: Asigno el input...
# Asigno contador, cambio bandera del campo estado a verdadero para tener un alta logica y empujo el puntero al proximo registro para cuando tenga que registrar otro.
Con = 0

def siono(x):
    if x == " " or "" or None:
        return True
    if x== 'S' or 's' or 'N' or 'n':
        return False


def alta_productos():
    global AF_PROD,AL_PROD
    os.system('cls')
    Regpro=prod()
    rta='S'
    while rta=='S':
        pro= input("ingrese un producto: ")
        while pro=="" or pro==" " or pro==None:
            pro=input("Ingrese un producto: ")
            pro=pro.upper
        #Busco si el producto ya se encuentra en el registro. Retorna bandera
        if busco_prod(pro)== -1:
            global Con, AF_PROD, AL_PROD
            Regpro=prod()
            Regpro.cod_prod = str(int(Con+1)).ljust(2)
            Regpro.nom_prod = pro
            Regpro.est = "A"
            formatProd(Regpro)
            AL_PROD.seek(0,2)
            pickle.dump(Regpro, AL_PROD)
            AL_PROD.flush()
            print(f"Se ha agregado correctamente el producto {pro}. ")
            os.system('pause')

        else:
            if Regpro.est == "B":
                    print(f"El producto {Regpro.nom_prod} se encuentra registrado, pero dado de BAJA\n")
                    estado=input(f'Desea volver poner a {Regpro.nom_prod} como ACTIVO? S para SI. N para NO. ->  ')
                    while siono(estado):
                        estado=input("Ingrese una opción válida, S para ACTIVAR. N para Seguir de BAJA ->  ")
                    estado=estado.upper
                    if estado=="S":
                        pos=busco_prod(pro)
                        AL_PROD.seek(pos,0)
                        Regpro = pickle.load(AL_PROD)
                        Regpro.est="A"
                        AL_PROD.seek(pos,0)
                        pickle.dump(Regpro,AL_PROD)
                        AL_PROD.flush()
                    else:
                        print(f"El producto {Regpro.nom_prod} quedó con estado= BAJA. \n")
            else:
                print(f"El producto {Regpro.nom_prod} ya se encuentra registrado. ")



        rta= input("desea ingresar otro Producto? S-si   N-no: ").upper()
        while rta != "S" and rta != "N":
            rta = input("Por favor, solo S para Si o N para No:").upper()


    


def busco_prod(x):
    global AF_PROD, AL_PROD
    fin= os.path.getsize(AF_PROD) 
    ban=False
    RegProd= prod()
    AL_PROD.seek(0,0)
    while AL_PROD.tell() < fin and ban==False:
        pos=AL_PROD.tell()
        RegProd = pickle.load(AL_PROD)
        if RegProd.nom_prod==x:
            ban= True
    if ban:
        return pos
    else:
        return -1


##############################################################
### BORARRARRRRRRRRRRRRRRRRRR
def buscaAve(nA):
    global ArcFisiAves, ArcLogAves 
    t = os.path.getsize(ArcFisiAves)
    rAve = Ave()
    band = False
    ArcLogAves.seek(0) 
    while ArcLogAves.tell()<t and band== False:
        pos = ArcLogAves.tell()
        rAve = pickle.load(ArcLogAves)
        if int(rAve.nro) == nA:
            band = True
    if band:
        return pos
    else:
        return -1
###RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR

def baja_prod():
    #mostrar_productos()
    rta='S'
    while rta=='S':
        cod=input("Ingrese el codigo de producto a borrar -> ")
    #Busco si ya ingresó un camión con ese producto
        if busco_prod_cam (cod) == 1:
            print("Un camion ya ha ingresado con este producto, por lo tanto no se puede borrar.")
        else:
            Regpro.es== False
    rta= input("Desea eliminar un producto? S-si   N-no: ").upper()
    while rta != "S" and rta != "N":
        rta = input("Por favor, solo S para Si o N para No:").upper()

    def busco_prod_cam (x):
        ban=False
        Regop= op()
        fin= os.path.getsize(afOperaciones)
        alOperaciones.seek(0)
        while alOperaciones.tell() < fin and ban==False:
            puntero=alOperaciones.tell
            Regop=pickle.load(alOperaciones)
            if Regop.cod_prod==x:
                ban== True
        if ban:
            return 1
        else:
            return 0

Regrub= rubro()
#afRubros alRubros
def Formatearrub(rub):
    rubro.cod_rub = (prod.cod).ljust(2)
    rubro.nom_rub = str(prod.nom).ljust(20, ' ')
# Inicio contador en 0 para luego asignarlo como codigo incrementandolo antes de asignarlo al campo, hago alta y busco si este ya fue ingresado. En caso de que no: Asigno el input...
# Asigno contador, cambio bandera del campo estado a verdadero para tener un alta logica y empujo el puntero al proximo registro para cuando tenga que registrar otro.
Con1 = 0
def alta_rubros():
    rta="S"
    while rta=='S':
            rub= input("ingrese un producto: ")
            while Regrub.nom_rub=="" or Regrub.nom_rub==" " or Regrub.nom_rub==None:
                rub=input("Ingrese un producto: ")
                rub=rub.upper
#Busco si el producto ya se encuentra en el registro. Retorna bandera
                if busco_rub(rub)== 1:
                    print("El producto ya se encuentra ingresado, intente nuevamente")
                else:    
                    Regrub.nom_rub == rub
                    Con1 == Con1 +1
                    Regpro.cod_prod == Con1
                Formatearrub(Regrub)
                alRubros.seek(0,2)
                pickle.dump(Regrub, alRubros)
                alRubros.flush()
            rta= input("desea ingresar otro Puntaje? S-si   N-no: ").upper()
            while rta != "S" and rta != "N":
                rta = input("Por favor, solo S para Si o N para No:").upper()
    
def busco_rub(x):
    global afRubros, alRubros
    fin= os.path.getsize(afRubros) 
    ban=False
    Regrub= rub()
    alRubros.seek(0)
    pun== alRubros.tell
    while pun < fin and ban==False:
        Regpro = pickle.load(alRubros)
        if Regrub.nom_rub==x:
            Ban= True
    if ban:
        return 1
    else:
        return 0

##########################################################

def menu_princ():
    print( "")
    print("                         ##################################")
    print("                         |   MENU PRINCIPAL EL ACOPIO     |")
    print("                         ##################################")
    print("                         # 1 - ADMININISTRACIONES")
    print("                         # 2 - ENTREGA DE CUPOS")
    print("                         # 3 - RECEPCION")
    print("                         # 4 - REGISTRAR CALIDAD")
    print("                         # 5 - REGISTRAR PESO BRUTO")
    print("                         # 6 - REGISTRAR DESCARGA")
    print("                         # 7 - REGISTRAR TARA")
    print("                         # 8 - REPORTES")
    print("                         # 9 - SILOS")
    print("                         # 0 - FIN DEL PROGRAMA")
    print("                         ----------------------------------")
    print("                         ##################################")
    print("" )

def menu_01_administraciones():
    print( "")
    print("                         ##################################")
    print("                         |     MENU ADMINISTRACIONES      |")
    print("                         ##################################")
    print("                         # A - TITULARES")
    print("                         # B - PRODUCTOS")
    print("                         # C - RUBROS")
    print("                         # D - RUBROS x PRODUCTO")
    print("                         # E - SILOS")
    print("                         # F - SUCURSALES")
    print("                         # G - PRODUCTO POR TITULAR")
    print("                         # V - Volver al Menu Principal")
    print("                         ----------------------------------")
    print("                         ##################################")
    print("" )

def menu_crud():
    print( "")
    print("                         ##################################")
    print("                         |   MENU ALTA-BAJA-CONS-MODIF    |")
    print("                         ##################################")
    print("                         # A - ALTA")
    print("                         # B - BAJA")
    print("                         # C - CONSULTA")
    print("                         # M - MODIFICACION")
    print("                         # V - Volver al Menu Anterior")
    print("                         ----------------------------------")
    print("                         ##################################")
    print("" )

def crud():
    flag2=True
    while flag2==True:
        limpia_pant()
        menu_crud()
        opcion=input( "\n--> Ingrese la opción que desea usar, o V para volver al menú anterior: \n--> " )
            
        if opcion == "A" or opcion == "a":
            limpia_pant()
            print( "")
            print("                          #####################################################")
            print("                          #####################################################")
            print("                          ##                                                 ##")
            print("                          ##                 ALTA DE PRODUCTO                ##")
            print("                          ##                                                 ##")
            print("                          #####################################################")
            print("                          #####################################################")
            pulse_Tecla()

        elif opcion == "B" or opcion == "b":
            limpia_pant()
            print("                         #####################################################")
            print("                         #####################################################")
            print("                         ##                                                 ##")
            print("                         ##                 BAJA DE PRODUCTO                ##")
            print("                         ##                                                 ##")
            print("                         #####################################################")
            print("                         #####################################################")
            pulse_Tecla()

        elif opcion == "C" or opcion == "c":
            limpia_pant()
            print( "                        #####################################################")
            print("                        #####################################################")
            print("                        ##                                                 ##")
            print("                        ##             CONSULTA DE PRODUCTO                ##")
            print("                        ##                                                 ##")
            print("                        #####################################################")
            print("                        #####################################################" )
            pulse_Tecla()

        elif opcion == "M" or opcion == "m":
            limpia_pant()
            print( "                        #####################################################")
            print("                        #####################################################")
            print("                        ##                                                 ##")
            print("                        ##           MODIFICACION DE PRODUCTO              ##")
            print("                        ##                                                 ##")
            print("                        #####################################################")
            print("                        #####################################################")
            pulse_Tecla()
            
        elif opcion == "V" or opcion == "v":
            flag2=False

def crud_productos():
    flag=True
    while flag==True:
        limpia_pant()
        menu_crud()
        opcion=input( "\n--> Ingrese la opción que desea usar, o V para volver al menú anterior: \n--> " )
        
        if opcion == "A" or opcion == "a":
            limpia_pant()
            alta_productos()
            os.system('pause')
                  
        elif opcion == "B" or opcion == "b":
            limpia_pant()
            baja_prod()
        
        elif opcion == "C" or opcion == "c":
            limpia_pant()
            mostrar_productos()
        
        elif opcion == "M" or opcion == "m":
            limpia_pant()
            modifica_prod()
        
        elif opcion == "V" or opcion == "v":
            flag=False

def administraciones():
    flag=True
    while flag==True:
        limpia_pant()
        menu_01_administraciones()
        opcion=input( "\n--> Ingrese de la A a la G según la opción que desea usar, o V para volver al menú anterior: \n--> " )
        if opcion == "A" or opcion == "a":
            crud()
            
        elif opcion == "B" or opcion == "b":
            crud_productos()

        elif opcion == "C" or opcion == "c":
            crud()

        elif opcion == "D" or opcion == "d":
            crud()

        elif opcion == "E" or opcion == "e":
            crud()
        elif opcion == "F" or opcion == "f":
            crud()

        elif opcion == "G" or opcion == "g":
            crud()

        elif opcion == "V" or opcion == "v":
            flag=False


################ PROGRAMA PRINCIPAL #######################

AF_OP = "TP3\\OPERACIONES.DAT"
AF_PROD = "TP3\\PRODUCTOS.DAT"
AF_RUBRO = "TP3\\RUBROS.DAT"
AF_RUBROP = "TP3\\RUBXPROD.DAT"
AF_SILOS = "TP3\\SILOS.DAT"

if not os.path.exists('TP3'):
    os.makedirs('TP3')

#####estoy probando,me falta todavia#####

if not os.path.exists(AF_OP):   
    AL_OP = open(AF_OP, "w+b")   
else:
    AL_OP = open(AF_OP, "r+b")

if not os.path.exists(AF_PROD):   
    AL_PROD = open(AF_PROD, "w+b")   
else:
    AL_PROD = open(AF_PROD, "r+b")

if not os.path.exists(AF_RUBRO):   
    AL_RUBRO = open(AF_RUBRO, "w+b")   
else:
    AL_RUBRO = open(AF_RUBRO, "r+b")

if not os.path.exists(AF_RUBROP):   
    AL_RUBROP = open(AF_RUBROP, "w+b")   
else:
    AL_RUBROP = open(AF_RUBROP, "r+b")

if not os.path.exists(AF_SILOS):   
    AL_SILOS = open(AF_SILOS, "w+b")   
else:
    AL_SILOS = open(AF_SILOS, "r+b")

flag=True
while flag==True:
    limpia_pant()    
    menu_princ()
    
    op=input("ingrese un valor entre 1 y 9, o 0 -> ")
    while validaRangoEntero(op, 0,9):
        op=input("ingrese un valor entre 1 y 9, o 0 -> ")
  
    if op == "1":
        administraciones()
    elif op == "2":
        entrega_cupos()
    elif op == "3":
        recepcion()
    elif op == "4":
        print("FUNCIONALIDAD EN CONSTRUCCION")
    elif op == "5":
        peso_bruto()
    elif op == "6":
        print("Funcionalidad en CONSTRUCCION")
    elif op == "7":
        peso_tara()
    elif op == "8":
        reportes()
    elif op == "9":
        silos()
        
    elif op =="0":
        flag=False

print("see you later, aligator...")