import os
import os.path
import pickle

# V 1 
# 26/09/2022. Se definieron todas las clases

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

#  MUESTRA EL CLASICO MENSAJE DE ESPERA
def pulse_Tecla():
    print("\nPulse cualquier tecla para continuar, por favor.\n")
    os.system("pause")
    

############## MODULOS DEL PROGRAMA ################

def verificar(op):
    while op!="0" and op!="1" and op!="2" and op!="3" and op!="4" and op!="5" and op!="6" and op!="7" and op!="8":
        op=input( "ingrese un valor entre 1 y 8, o 0 para salir -> ")
    return op


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
            print("Fecha valida")
            flag = False
        except ValueError:
            print("Fecha invalida")
    return fecha

#### CREAMOS LOS ARCHIVOS ####

class OPERACIONES:
    def __init__(self):
        self.patente = " "
        self.codprod = 0
        self.fechacupo = " "
        self.estado = " "
        self.bruto = 0
        self.tara = 0

class prod:
    def __init__(self):
        self.codprod = 0
        self.nomprod = " "
        self.estado = "A" # A=ALTA - B=BAJA

class RUBROS:
    def __init__(self):
        self.codrub = 0
        self.nomrub = " "

class RUBxPROD:
    def __init__(self):
        self.codrub = 0
        self.codprod = 0
        self.rubro1 = 0
        self.rubro2 = 0
        self.rubro3 = 0

class SILOS:
    def __init__(self):
        self.codsilo = 0
        self.nomsilo = " "
        self.codprod = 0
        self.stock = 0

#####################################################

def validar_Rango_Entero(opc,desde,hasta):
    try:
        int(opc)
        if int(opc) >= desde and int(opc) <= hasta:
            return False
        else:
            return True
    except: 
        return True
    
afOperaciones = "files\\OPERACIONES.DAT"
afProductos = "files\\PRODUCTOS.DAT"
afRubros = "files\\RUBROS.DAT"
afProdxRub = "files\\PRODxRUB.DAT"
afSilos = "files\\SILOS.DAT"

def open_productos():
    if not os.path.exists(afProductos): 
        alProductos = open(afProductos,"w+b")
        return alProductos
    else:
        alProductos = open(afProductos,"r+b")
        return alProductos

def carga_Productos():
    pass

def primeraVez():
    print("\nBienvenidos a nuestro programa. Gracias por elegirnos. \nAntes de comenzar debemos realizar unos pequeños ajustes.\n")
#    open_productos()
#    carga_Productos()

if not os.path.exists("files"):
    os.makedirs("files")
    primeraVez()

######### AGREGO LA PARTE QUE HIZO RAMA #########

def alta_productos():
    Regpro = prod()
    rta='S'
    while rta=='S':
        pro= input("Ingrese un producto: ")
    while Regpro.nom=="" or Regpro.nom==" " or Regpro.nom==None:
        pro=input("Ingrese un producto: ")
        pro=pro.upper
#Busco si el producto ya se encuentra en el registro. Retorna bandera
    if busco_prod(pro,Regpro,Alp,Alf):
        print("El producto ya se encuentra ingresado, intente nuevamente")
    else:    
        tcod= input("Ingrese código de producto: ")
        Regpro.nom== pro
        Regpro.cod== cod
        Formatearprod(Regpro)
        Alp.seek(0,2)
        pickle.dump(Regpro, Alp)
        Alp.flush()
    rta= input("Desea ingresar otro Puntaje? S-si   N-no: ").upper()
    while rta != "S" and rta != "N":
        rta = input("Por favor, solo S para Si o N para No:").upper()
    
def busco_prod(x,reg,al,af):
    ban=False
    reg=producto()
    fin= os.path.getsize(af)
    al.seek(0)
    while al.tell() < fin y ban=False
        puntero=al.tell
        reg=pickle.load(al)
        if reg.nom=x
            Ban= True
        else:
            Ban= False
    return Busco_prod=Ban # acá debería ir úncamente la variable a retornar (Ban)

def baja_prod():
    mostrar_productos()
    rta='S'
    while rta=='S':
        cod=input("Ingrese el codigo de producto a borrar -> ")
#Busco si ya ingresó un camión con ese producto
        if busco_prod(cod,Regop,Alo,Afo) :
            print("Un camion ya ha ingresado con este producto, por lo tanto no se puede borrar.")
        else:
            Regpro.nom==""
            Regpro.cod==""
            print("Un camion ya ha ingresado con este producto, por lo tanto no se puede borrar.")
            rta= input("Desea eliminar un producto? S-si   N-no: ").upper()
            while rta != "S" and rta != "N":
                rta = input("Por favor, solo S para Si o N para No:").upper()

def busco_prod_cam (x,reg,al,af):
    ban=False
    reg=producto()
    fin= os.path.getsize(af)
    al.seek(0)
    while al.tell() < fin y ban=False
        puntero=al.tell
        reg=pickle.load(al)
        if reg.cod=x
        Ban= True
    else:
        Ban= False
    return Busco_prod=ban


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
    print("                         # 9 - ALGOMAS...")
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
            pulse_Tecla()
                  
        elif opcion == "B" or opcion == "b":
            limpia_pant()
            baja_prod()
            pulse_Tecla()

        elif opcion == "C" or opcion == "c":
            limpia_pant()
            mostrar_productos()
            pulse_Tecla()

        elif opcion == "M" or opcion == "m":
            limpia_pant()
            modifica_prod()
            pulse_Tecla()
            
        elif opcion == "V" or opcion == "v":
            flag=False

def alta_productos():
    print("#################### A. ALTA DE PRODUCTOS ####################")
    print("")
    print("PRODUCTOS EXISTENTES")
    mostrar_productos()
    
    
    i=0
    while i<2 and productos[i]!=" ":
        i+=1
    if productos[i]==" ":
        print("")
        print("PRODUCTOS QUE SE PUEDEN CARGAR")
        print("")
        mostrar_pac(pac)
        print("")
        print("")
        prod=input(f"Ingrese el numero correspondiente al Producto que desee cargar. -> ")
        while prod!="1" and prod!="2" and prod!="3" and prod!="4" and prod!="5":
            print("")
            mostrar_pac(pac)
            print("")
            prod=input(f"Ingrese el numero correspondiente al Producto que desee cargar. -> ")

        alta_prod(prod)
    else:
        if i<=2 and productos[i]!=" ":
            print("")
            print("LISTA DE PRODUCTOS LLENA. BORRE ALGUN PRODUCTO O INTENTE MAÑANA :) ")
            

    
def alta_prod(prod):
    prod=int(prod)
    prod=prod-1
    i=0
    while pac[prod]!=productos[i] and i<2:
        i+=1
    if pac[prod]!=productos[i]:
        i=0
        while productos[i]!=" ":
            i+=1
        productos[i]=pac[prod] 
        print(f"El producto {pac[prod]} se ha agregado correctamente")
    else:
        print(f"El producto {pac[prod]} ya se encuentra registrado")
    
    
def mostrar_productos():
    if productos[0]==" " and productos[1]==" " and productos[2]==" ":
        print("No hay productos para Mostrar. ")
    else:
        for i in range (3):
            if productos[i]!=" ":
                print(f" {i+1} - {productos[i]} ")

def baja_prod():
    if productos[0]==" " and productos[1]==" " and productos[2]==" ":
        print("No hay productos para borrar. ")
    else:
        mostrar_productos()
        print(" 0 - SALIR SIN BORRAR ")
        print("")
        print("")
        prod=input("Ingrese el número del producto a borrar, o 0 para no borrar nada -> ")
        while prod!="1" and prod!="2" and prod!="3" and prod!="0" or prod=="" or prod==" ":
            mostrar_productos()
            print(" 0 - SALIR SIN BORRAR ")
            print("")
            print("")
            prod=input("Ingrese un valor igual o mayor que 1 y menor o igual que 3. Use 0 para no borrar nada")
        
        if prod!="0":
            i=0
            prod=int(prod)
            # verificacion producto asignado a camion RECIBIDO
            while i<7 and productos[prod-1]!=cupos[i][2]:
                i+=1
            if productos[prod-1]!=cupos[i][2]:
                i=0
                while prod!=i+1:
                    i+=1
                print(f"El producto {productos[i]} fue removido con éxito ")
                productos[i]=" "
            else:
                print(f"El producto {productos[prod-1]} NO puede ser borrado debido a que está asignado a, al menos, un camión en la lista de CUPOS. ")
            
        else:
            print("NO SE HA BORRADO NINGUN PRODUCTO DE LA LISTA")
    
def modifica_prod():
    if productos[0]==" " and productos[1]==" " and productos[2]==" ":
        print("No hay productos para Modificar. ")
    else:
        mostrar_productos()
        print(" 0 - SALIR SIN MODIFICAR ")
        print("")
        print("")
        prod=input("Ingrese el número del producto a Modificar, o 0 para no hacer nada -> ")
        while prod!="1" and prod!="2" and prod!="3" and prod!="0":
            mostrar_productos()
            print(" 0 - SALIR SIN MODIFICAR ")
            print("")
            print("")
        
        if prod!="0":
            i=0
            prod=int(prod)
            while i<7 and productos[prod-1]!=cupos[i][2]:
                i+=1
            if productos[prod-1]==cupos[i][2]:
                print(f"El producto {productos[prod-1]} NO puede ser Modificado debido a que está asignado a, al menos, un camión en la lista de CUPOS. ")
            else:
                i=0
                while prod!=i+1:
                    i+=1
                modif=input(f"Ingrese la modificación que quiera realizar en {productos[i]} -> ")
                modif=modif.upper()
                while modif=="" or modif==" " or modif==None or len(modif)>7:
                    modif=input("INGRESE UN PRODUCTO VALIDO :-> ")
                    modif=modif.upper()
                print(f"El producto {productos[i]} fue modificado por con éxito por {modif} ")
                productos[i]=modif
                mostrar_productos()
        else:
            print("")
            print("NO SE HA MODIFICADO NINGUN PRODUCTO DE LA LISTA")
    
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

#################### INICIO 2. ENTREGA DE CUPOS ####################

def mostrar_pac(pac):
    for i in range(5):
        print(f" {i+1} - {pac[i]} ")

def entrega_cupos():
    print("#################### 2. ENTREGA DE CUPOS ####################")
    print("")
    
    i=0
    while i<7 and cupos[i][0]!=" ":
        i+=1
    if cupos[i][0]==" ":
        # VALIDACION PATENTE
        cupo=input("INGRESE UNA PATENTE :-> ")
        while len(cupo)<6 or len(cupo)>7:
            cupo=input("INGRESE UNA PATENTE VALIDA :-> ")
        cupo=cupo.upper() # CONVIERTO LO INGRESADO EN MAYUSCULAS
        ########################################

        alta_cupo(cupo)
    else:
        if i<=7 and cupos[i][0]!=" ":
            print("LISTA DE CUPOS LLENA. INTENTE MAÑANA :) ")

    ########################################

    
    
def alta_cupo(cupo):
    i=0
    while cupo!=cupos[i][0] and i<7:
        i+=1
    if cupo!=cupos[i][0]:

        ###### agrego carga de productos
        mostrar_pac(pac) # Muestro productos habilitados para la carga
        print("")
        print("")

        # VALIDO INGRESO PARA SELECCION DEL PRODUCTO
        prod=input(f"Ingrese el numero correspondiente al tipo de carga a asignar a {cupo}.")
        while prod!="1" and prod!="2" and prod!="3" and prod!="4" and prod!="5":
            mostrar_pac(pac)
            print("")
            print("")
            prod=input(f"Ingrese el numero correspondiente al tipo de carga a asignar a {cupo}.")
        
        # Convierto la variable prod input que es STR a INT para poder usarlo como índice. Para usar como indice hay que restarle 1.
        prod=int(prod)
        
        # RECORRO EL ARRAY DE PRODUCTOS PARA VER SI EL PRODUCTO SELECCIONADO YA ESTÁ CARGADO
        i=0
        while pac[prod-1]!=pr[i] and i<2:
            i+=1
        prt=i
        # SI EL PRODUCTO INGRESADO EXISTE ENTRE LOS PRODUCTOS REGISTRADOS, PROCEDO A DARLE UN CUPO alta_cupo
        if pac[prod-1]==pr[i]: 
            c=0
            while cupos[c][0]!=" ":
                c+=1
            cupos[c][0]=cupo # AGrego la patente al array cupos en la fila i columna 0 
            cupos[c][1]="P" # Cambio el estado a P de Pendiente
            cupos[c][2]=productos[prt] # Insertor de producto asociado al camión
            print(f"El Cupo para descargar {pr[prt]} del Camión {cupo} se ha agregado correctamente.")
            print(f"Y se ha asignado al Camión {cupo} el estado de P = Pendiente ")
            
        # SI NO, procedo a intentar cargarlo
        else:
            
            # Recorro el array de productos para buscar un lugar vacío
            i=0
            while i<2 and productos[i]!=" ":
                i+=1
            
            # Si hay lugar lo registro
            if productos[i]==" ":
                c=0
                while cupos[c][0]!=" ":
                    c+=1
                alta_prod(prod)
                cupos[c][0]=cupo # AGrego la patente al array cupos en la fila i columna 0 
                cupos[c][1]="P" # Cambio el estado a P de Pendiente
                cupos[c][2]=productos[i] # Insertor de producto asociado al camión
                print(f"El Cupo para descargar {pr[i]} del Camión {cupo} se ha agregado correctamente.")
                print(f"Y se ha asignado al Camión {cupo} el estado de P = Pendiente ")
            else:
                if i<=2 and productos[i]!=" ":
                    print(f"El producto {pac[prod-1]} no se encuentra registrado entre los productos habilitados, y no queda más espacio para productos nuevos. ")
                    for i in range(3):
                        print(f" {i+1} - {productos[i]} ")


            
    else:
        print(f"El Cupo para {cupo} ya se encuentra registrado")    


#################### INICIO 3. RECEPCION ####################

def recepcion():
    flag=True
    while flag==True:
        limpia_pant()
        print("")
        patente=input("INGRESE LA PATENTE DEL CAMION A RECIBIR :-> ")
        while len(patente)<6 or len(patente)>7:
            patente=input("INGRESE UNA PATENTE VALIDA (minimo 6 caracteres. máximo 7 caracteres. ):-> ")
        patente=patente.upper()
        i=0
        while i<7 and patente!=cupos[i][0]:
            i+=1
        if patente==cupos[i][0]:
            if cupos[i][1]=="P":
                
                ##### CAMBIO EL ESTADO
                cupos[i][1]="E"
                

                ## Contador Camiones por Producto ##
                for p in range (3):
                    if cupos[i][2]==pr[p]:
                        peso[p][3]+=1
                                
                print(f"Se ha Recibido el Camión {patente} y se ha cambiado su estado a 'E: En-Proceso' ")
                

            elif cupos[i][1]=="E":
                print(f"El Camión {patente} ya se ha Recibido y su estado es EN PROCESO. Proceda a cargar datos.")
            elif cupos[i][1]=="C":
                print(f"El Camión {patente} ya se ha Recibido y su estado es CUMPLIDO.")
        else:
            print(f"El Camión {patente} no se encuentra en la lista de Cupos registrados para el día de hoy. ")
        
        pulse_Tecla()
        limpia_pant()
        print("")

        go_on=input("Desea Recibir otro camión? 'S' para Seguir - 'N' para terminar la recepción -> ")
        while go_on!="S" and go_on!="s" and go_on!="N" and go_on!="n":
            go_on=input("Desea Recibir otro camión? 'S' para Seguir - 'N' para terminar la recepción -> ")
        if go_on=="N" or go_on=="n":
            flag=False
        else:
            flag=True
    
##############################################################

#################### INICIO 4. REGISTRAR CALIDAD ##################
###################################################################

########### INICIO 5. REGISTRAR PESO BRUTO ########################

def peso_bruto():
    flag=True
    while flag==True:
        limpia_pant()
        print("")
        patente=input("INGRESE LA PATENTE DEL CAMION A REGISTRAR EL PESO BRUTO :-> ")
        while len(patente)<6 or len(patente)>7:
            patente=input("INGRESE UNA PATENTE VALIDA (minimo 6 caracteres. máximo 7 caracteres. ):-> ")
        patente=patente.upper()
        i=0
        while i<7 and patente!=cupos[i][0]:
            i+=1
        if patente==cupos[i][0]:
            if cupos[i][1]=="E":
                if datos[i][0]==0:
                    bruto=int(input("Ingrese las toneladas -sin decimales- |-> "))
                    while bruto<10 and bruto>56:
                        bruto=int(input("Ingrese las toneladas -sin decimales- |-> "))
                    datos[i][0]=bruto
                else:
                    print(f"El camión {patente} ya tiene registrado un peso bruto de {datos[i][0]} ")
            
            elif cupos[i][1]=="P":
                print(f"El camión {patente} todavía no ha pasado por RECEPCION. Vaya a RECEPCION y vuelva a cargar. ")
            
            elif cupos[i][1]=="C":
                print(f"El camión {patente} ya ha COMPLETADO el proceso de cargas. Vaya a REPORTES.")
            
        else:
            print(f"El Camión {patente} no se encuentra en la lista de Cupos registrados para el día de hoy. ")
        
        go_on=input("Desea Recibir otro camión? 'S' para Seguir - 'N' para terminar la recepción -> ")
        while go_on!="S" and go_on!="s" and go_on!="N" and go_on!="n":
            go_on=input("Desea Recibir otro camión? 'S' para Seguir - 'N' para terminar la recepción -> ")
        if go_on=="N" or go_on=="n":
            flag=False
        else:
            flag=True

###################################################################

################ INICIO 6. REGISTRAR DESCARGA #####################
# #################################################################

################ INICIO 7. REGISTRAR TARA  ########################

def peso_tara():
    flag=True
    while flag==True:
        limpia_pant()
        print("")
        patente=input("INGRESE LA PATENTE DEL CAMION A REGISTRAR LA TARA :-> ")
        while len(patente)<6 or len(patente)>7:
            patente=input("INGRESE UNA PATENTE VALIDA (minimo 6 caracteres. máximo 7 caracteres. ):-> ")
        patente=patente.upper()
        i=0
        while i<7 and patente!=cupos[i][0]:
            i+=1
        if patente==cupos[i][0]:
            if cupos[i][1]=="E":
                if datos[i][0]!=0:
                    if datos[i][1]==0:
                        print(f"el camión {patente} se ha encontrado y su peso bruto es de {datos[i][0]} ")
                        tara=int(input("Ingrese las toneladas | Sin Decimales y Tara < P.Bruto |-> "))
                        while tara<10 or tara>56 or tara>datos[i][0]:
                            tara=int(input("Verifique el dato ingresado. TARA debe ser menor que PESO BRUTO |-> "))
                        datos[i][1]=tara
                        
                        #### PESO NETO #####
                        # al tener la tara y el p.bruto, ya puedo calcular el peso neto
                        datos[i][2]=datos[i][0]-datos[i][1]
                        ###################################
                    else:
                        print(f"El camión {patente} ya tiene registrado una TARA de {datos[i][1]} ")
                else:
                    print(f"El camión {patente} no registra PESO BRUTO. Cargue el P.Bruto y vuelva. Gracias.  ")
                
            elif cupos[i][1]=="P":
                print(f"El camión {patente} todavía no ha pasado por RECEPCION. Vaya a RECEPCION y vuelva a cargar. ")
            
            elif cupos[i][1]=="C":
                print(f"El camión {patente} ya ha COMPLETADO el proceso de cargas. Vaya a REPORTES.")
            
        else:
            print(f"El Camión {patente} no se encuentra en la lista de Cupos registrados para el día de hoy. ")
        
        go_on=input("Desea Recibir otro camión? 'S' para Seguir - 'N' para terminar la recepción -> ")
        while go_on!="S" and go_on!="s" and go_on!="N" and go_on!="n":
            go_on=input("Desea Recibir otro camión? 'S' para Seguir - 'N' para terminar la recepción -> ")
        if go_on=="N" or go_on=="n":
            flag=False
        else:
            flag=True

###################################################################


############### INICIO 8. REPORTES ################################

def cant_cupos():
    i=0
    while i<=7 and cupos[i][0]!=" ":
        i+=1
    cant_cupos=i
    return cant_cupos

def cam_recib():
    i=0
    while i<=7 and cupos[i][1]!="P" and cupos[i][1]!=" ":
        i+=1
    tot_cam_recibidos=i
    return tot_cam_recibidos

def calculos_productos(peso,pat):
    # inicializo peso menor en 60
    for x in range (3):
        peso[x][2]=60
    
    i=0
    while i<=7 and cupos[i][2]!=" ": # Es menor o igual que 7 y Producto asociado a cupo es diferente de vacío
        
        for x in range (3): # recorro el array de productos
            if cupos[i][2]==productos[x]: # si el producto asociado es igual al producto

                peso[x][0]+=datos[i][2]  # Acumulo el peso neto del camión en el array peso, columna 0: neto total por producto

                if datos[i][2]>peso[x][1]: # si el peso del camión es mayor al peso del mayor peso existente
                    peso[x][1]=datos[i][2] # lo pongo en el array peso columna 1
                    pat[x][0]=cupos[i][0] # asigno el valor de la patente a Mayor Patente.
 
                if datos[i][2]<peso[x][2]: # si el peso del camión es menor al peso del menor peso existente
                    peso[x][2]=datos[i][2] # lo pongo en el array peso columna 2
                    pat[x][1]=cupos[i][0] # asigno el valor de la patente a Menor Patente.


        i+=1   # Incremento en 1 para verificar el siguiente camión. 
                       
def ordenar(datos,cupos): # ARRAYS CON ARRASTRE
    for i in range (cant_cupos()-1):
        for j in range (i+1,cant_cupos()):
            if datos[i][2] <= datos[j][2]:
                for d in range (3):
                    #ordeno array datos
                    aux=datos[i][d]
                    datos[i][d]=datos[j][d]
                    datos[j][d]=aux
                    #ordeno array cupos
                    aux1=cupos[i][d]
                    cupos[i][d]=cupos[j][d]
                    cupos[j][d]=aux1
                
def reportes():
    
    if cant_cupos()==0:
        print("")
        print("NO SE HAN PROGRAMADO CAMIONES HASTA EL MOMENTO")
    else:
        print(f"Cantidad de Cupos : {cant_cupos()}")
        
        if cam_recib()==0:
            print("")
            print("Todavía NO se han RECIBIDO camiones.")
        else:
            calculos_productos(peso,pat)
            print(f"Camiones Recibidos: {cam_recib()}")

            for m in range (3):
                if productos[m]!=" ":
                    if peso[m][3]==0:
                        print(f"No se han recibido camiones de {productos[m]} ")
                    else:
                        print(f"Cantidad de Camiones de {productos[m]}: {peso[m][3]}")
                        print(f"Peso Neto Total de {productos[m]}: {peso[m][0]} ")
                        print(f"Promedio del Peso Neto de {productos[m]}: {peso[m][0]/peso[m][3]} ")
                        print(f"Patente del Camión de {productos[m]} con MAYOR carga: {pat[m][0]} ")
                        print(f"Patente del Camión de {productos[m]} con MENOR carga: {pat[m][1]} ")
                        print(".......................................................................")
                
            pulse_Tecla()

            print("********************************************")
            print("  PATENTES       PRODUCTO     PESO NETO     ")
            for i in range (8):
                if cupos[i][0]!=" ":
                    print(f"   {cupos[i][0]}         {cupos[i][2]}          {datos[i][2]}       ")
            print("********************************************")

            # ORDENAMOS LA TABLA
            ordenar(datos,cupos)           
            print("********************************************")
            print("    ORDENADO DESCENDENTE POR PESO NETO     *")
            print("********************************************")
            print("  PATENTES       PRODUCTO     PESO NETO     ")
            for i in range (8):
                if cupos[i][0]!=" ":
                    print(f"   {cupos[i][0]}         {cupos[i][2]}          {datos[i][2]}       ")
            print("********************************************")

def produ(pr):
    if pr[0]==" " and pr[1]==" " and pr[2]==" ":
        True
              
################ PROGRAMA PRINCIPAL #######################

flag=True
while flag==True:
    limpia_pant()    
    menu_princ()
        
    opc=input("Ingrese un valor entre 1 y 9, o 0 -> ")
    while validar_Rango_Entero(opc,0,9):
        opc=input("Opción inválida, ingrese un valor entre 1 y 9, o 0 -> ")
  
    if opc == "1":
        administraciones()
    elif opc =="2":
        entrega_cupos()
        pulse_Tecla()
    elif opc =="3":
        recepcion()
    elif opc =="4":
        print("FUNCIONALIDAD EN CONSTRUCCION")
    elif opc =="5":
        peso_bruto()
        pulse_Tecla()
    elif opc =="6":
        print("Funcionalidad en CONSTRUCCION")
    elif opc =="7":
        peso_tara()
        pulse_Tecla()
    elif opc =="8":
        reportes()
        pulse_Tecla()
    elif opc =="9":
        print("Funcionalidad en CONSTRUCCION")
    elif opc =="0":
        flag=False

print("see you later, aligator...")