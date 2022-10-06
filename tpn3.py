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
        self.cod_rub = 0
        self.nom_rub = ""
        
class rubrop:
    def __init__(self):
        self.cod_prod = 0
        self.cod_rub = 0
        self.min = 0.0
        self.max = 0.0

##### FORMATEADORES #####

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
   vrProd.cod_prod = vrProd.cod_prod.ljust(2)
   vrProd.nom_prod = vrProd.nom_prod.ljust(15)
   # vrProd.est = vrProd.est.ljust(1) No es necesario. Asignación Interna
   # Y siempre va a ser una sola letra

def formatRub(vrRub):
    vrRub.cod_rub = str(vrRub.cod_rub)
    vrRub.cod_rub = vrRub.cod_rub.ljust(2)
    vrRub.nom_rub = vrRub.nom_rub.ljust(15)

def formatRxP(vrRxP):
    vrRxP.cod_prod = str(vrRxP.cod_prod)
    vrRxP.cod_prod = vrRxP.cod_prod.ljust(2)
    vrRxP.cod_rub = str(vrRxP.cod_rub)
    vrRxP.cod_rub = vrRxP.cod_rub.ljust(2)
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

##########################################################

def validaRangoEntero(nro, min,max):
    try:              
        nro = int(nro)      
        if nro >= min and nro <= max:
            return False 
        else:
            return True  
    except:
        return True  

def cant_prod():
    t=os.path.getsize(AF_PROD)
    if t==0:
        return 0
    else:
        AL_PROD.seek(0)
        pickle.load(AL_PROD)
        aux=AL_PROD.tell()
        cant_reg=t//aux
        return cant_reg

def alta_productos():
    os.system('cls')
    print(" OPCION A - Alta de Productos ")
    print(" -----------------------------\n ")
    rta='S'
    while rta=='S':
        os.system('cls')
        pro=input("ingrese el producto [hasta 15 carcateres] :  ")
        while len(pro)<3 or len(pro)>=15:
            pro=input("ERROR. Ingrese el producto [hasta 15 carcateres] :  ")
        pro=pro.upper()
        RegProd=prod()
        if buscaProducto(pro) == -1:
            RegProd.cod_prod=cant_prod()+1
            RegProd.nom_prod=pro
            RegProd.est="A"
            AL_PROD.seek(0,2)
            formatProd(RegProd)
            pickle.dump(RegProd,AL_PROD)
            AL_PROD.flush()
            print(f"El producto {pro} fue registrado con éxito... \n ")
        else:
            print("El producto ya se encuentra registrado. Verifique el estado\n")
        
        rta= input("Desea ingresar otro producto? S-si   N-no: ").upper()
        while rta != "S" and rta != "N":
            rta = input("Por favor, solo S para Si o N para No:").upper()
        
def buscaProducto(pro):
    t = os.path.getsize(AF_PROD)
    AL_PROD.seek(0)
    ban=False
    while AL_PROD.tell()<t and ban== False:
        pos = AL_PROD.tell()
        rProd = pickle.load(AL_PROD)
        if rProd.nom_prod.strip() == pro:
            return pos
    return -1

def buscaProducto_cod(cod):
    t = os.path.getsize(AF_PROD)
    AL_PROD.seek(0)
    ban=False
    while AL_PROD.tell()<t and ban== False:
        pos = AL_PROD.tell()
        rProd = pickle.load(AL_PROD)
        if int(rProd.cod_prod) == int(cod):
            return pos
    return -1

def busco_prod_cam(x):
    fin= os.path.getsize(AF_OP)
    if fin==0:
        return False
    else:
        ban=False
        Regop= op()
        Regop=pickle.load(AL_OP)
        
        AL_OP.seek(0)
        while AL_OP.tell() < fin and ban==False:
            Regop=pickle.load(AL_OP)
            if int(Regop.cod_prod)==int(x):
                ban=True
                return ban
        return False

def baja_prod():
    global AF_PROD, AL_PROD
    os.system('cls')
    t=os.path.getsize(AF_PROD)
    if t==0:
        print("No hay productos para Borrar")
        os.system('pause')
    else:
        rta='S'
        while rta=='S':
            mostrar_productos_all()
            cantp=cant_prod()
            cod=input(f"Ingrese el codigo de producto a borrar o 0 para no modificar nada -> ")
            while validaRangoEntero(cod,0,cantp):
                cod=input(f"Ingrese el codigo de producto a borrar o 0 para no modificar nada -> ")
            cod=int(cod)
            if cod!=0:
                #Busco si ya ingresó un camión con ese producto
                if busco_prod_cam(cod):
                    print("Un camion ya ha ingresado con este producto, por lo tanto no se puede borrar.")
                else:

                    pos=buscaProducto_cod(cod)
                    rPro=prod()
                    AL_PROD.seek(pos,0)
                    rPro=pickle.load(AL_PROD)
                    rPro.est="B"
                    AL_PROD.seek(pos)
                    pickle.dump(rPro,AL_PROD)
                    AL_PROD.flush()
                    print("Baja existosa.")
            
                rta= input("Desea eliminar otro producto? S-si   N-no: ").upper()
                while rta != "S" and rta != "N":
                    rta = input("Por favor, solo S para Si o N para No:").upper()
            else:
                rta="N"

def modifica_prod():
    global AF_PROD, AL_PROD
    os.system('cls')
    t=os.path.getsize(AF_PROD)
    if t==0:
        print("No hay productos para Modificar")
        os.system('pause')
    else:
        rta='S'
        while rta=='S':
            mostrar_productos_all()
            cantp=cant_prod()
            cod=input(f"Ingrese el codigo de producto a Modificar o 0 para salir sin hacer cambios -> ")
            while validaRangoEntero(cod,0,cantp):
                cod=input(f"ERROR. Ingrese el codigo de producto a Modificar o 0 para salir sin hacer cambios  -> ")
            cod=int(cod)
            if cod!=0:
                #Busco si ya ingresó un camión con ese producto
                if busco_prod_cam(cod):
                    print("Un camion ya ha ingresado con este producto, por lo tanto no se puede Modificar.")
                else:
                    pos=buscaProducto_cod(cod)
                    rPro=prod()
                    AL_PROD.seek(pos,0)
                    rPro=pickle.load(AL_PROD)
                    cambia_nom=input("Desea Cambiar el nombre? [S = cambia] [N = No cambia] ").upper()
                    while cambia_nom!="S" and cambia_nom!="N":
                        cambia_nom=input("Desea Cambiar el nombre? [S = cambia] [N = No cambia] ").upper()
                    if cambia_nom=="S":
                        nom=input("Modifique el nombre del producto: ").upper()
                        while len(nom)<3 or len(nom)>15:
                            nom=input("ERROR. Nombre de Producto entre 3 y 15 caracteres").upper()
                        rPro.nom_prod=nom.ljust(15)
                        
                    cambia_est=input("Desea Cambiar el Estado? [S = cambia] [N = No cambia] ").upper()
                    while cambia_est!="S" and cambia_est!="N":
                        cambia_est=input("Desea Cambiar el Estado? [S = cambia] [N = No cambia] ").upper()
                    if cambia_est=="S":
                        if rPro.est=="A":
                            rPro.est="B"
                        else:
                            rPro.est="A"
                    AL_PROD.seek(pos)
                    pickle.dump(rPro,AL_PROD)
                    AL_PROD.flush()
                    print("Modificación existosa.")
                    mostrarProd(rPro)

                rta= input("Desea Modificar otro producto? S-si   N-no: ").upper()
                while rta != "S" and rta != "N":
                    rta = input("Por favor, solo S para Si o N para No:").upper()
            else:
                rta="N" 

def mostrar_productos_all(): # MUESTRA TODOS LOS PRODUCTOS
    global AF_PROD, AL_PROD
    os.system('cls')
    t=os.path.getsize(AF_PROD)
    if t==0:
        print("No hay productos para mostrar")
        os.system('pause')
    else:
        rProd=prod()
        print("-----------------------------------------")
        print(" CodPro - Producto  - Estado ")
        AL_PROD.seek(0)
        while AL_PROD.tell()<t:
            rProd=pickle.load(AL_PROD)
            mostrarProd(rProd)
    
def mostrar_productos(): # MUESTRA PRODUCTOS ACTIVOS
    global AF_PROD, AL_PROD
    os.system('cls')
    t=os.path.getsize(AF_PROD)
    if t==0:
        print("No hay productos para mostrar")
        os.system('pause')
    else:
        rProd=prod()
        print("-----------------------------------------")
        print(" CodPro - Producto  - Estado ")
        AL_PROD.seek(0)
        while AL_PROD.tell()<t:
            rProd=pickle.load(AL_PROD)
            if rProd.est=="A":
                mostrarProd(rProd)
    os.system('pause')

############### ALTA DE RUBROS ###############

def cant_rub():
    t=os.path.getsize(AF_RUBRO)
    if t==0:
        return 0
    else:
        AL_RUBRO.seek(0)
        pickle.load(AL_RUBRO)
        aux=AL_RUBRO.tell()
        cant_reg=t//aux
        return cant_reg

def alta_rubros():
    os.system('cls')
    print(" OPCION A - Alta de RUBROS ")
    print(" -----------------------------\n ")
    rta='S'
    while rta=='S':
        os.system('cls')
        rub=input("ingrese el Rubro [hasta 15 carcateres] :  ")
        while len(rub)<3 or len(rub)>=15:
            rub=input("ERROR. Ingrese el Rubro [hasta 15 carcateres] :  ")
        rub=rub.upper()
        rRub=rubro()
        if buscaRubro(rub) == -1:
            rRub.cod_rub=cant_rub()+1
            rRub.nom_rub=rub
            AL_RUBRO.seek(0,2)
            formatRub(rRub)
            pickle.dump(rRub,AL_RUBRO)
            AL_RUBRO.flush()
            print(f"El Rubro {rub} fue registrado con éxito... \n ")
        else:
            print("El Rubro ya se encuentra registrado.\n")
        
        rta= input("Desea ingresar otro Rubro? S-si   N-no: ").upper()
        while rta != "S" and rta != "N":
            rta = input("Por favor, solo S para Si o N para No:").upper()

def buscaRubro(rub):
    t = os.path.getsize(AF_RUBRO)
    AL_RUBRO.seek(0)
    ban=False
    while AL_RUBRO.tell()<t and ban== False:
        pos = AL_RUBRO.tell()
        rRub = pickle.load(AL_RUBRO)
        if rRub.nom_rub.strip() == rub:
            return pos
    return -1

def buscaRubro_cod(cod):
    t = os.path.getsize(AF_RUBRO)
    AL_RUBRO.seek(0)
    ban=False
    while AL_RUBRO.tell()<t and ban== False:
        pos = AL_RUBRO.tell()
        rRub = pickle.load(AL_RUBRO)
        if int(rRub.cod_rub) == int(cod):
            return pos
    return -1

##########################################################

############### ALTA DE SILOS ###############

def cant_silos():
    t=os.path.getsize(AF_SILOS)
    if t==0:
        return 0
    else:
        AL_SILOS.seek(0)
        pickle.load(AL_SILOS)
        aux=AL_SILOS.tell()
        cant_reg=t//aux
        return cant_reg

def alta_silos():
    os.system('cls')
    print(" OPCION A - Alta de SILOS ")
    print(" -----------------------------\n ")
    rta='S'
    while rta=='S':
        os.system('cls')
        sil=input("ingrese el Nombre del Silo [hasta 15 carcateres] :  ")
        while len(sil)<3 or len(sil)>=15:
            sil=input("ERROR. Ingrese el nombre del SILO [hasta 15 carcateres] :  ")
        sil=sil.upper()
        rSilo=silo()
        if buscaSilo(sil) == -1:
            rSilo.cod_silo=cant_silos()+1
            rSilo.nom_silo=sil
            
            print(f"Elija el producto que desea asociar al silo {sil} ")
            mostrar_productos()
            print()
            cantp=cant_prod()
            cod=input(f"Ingrese el codigo de producto a Asociar con Silo {sil} -> ")
            while validaRangoEntero(cod,1,cantp):
                cod=input(f"ERROR. Ingrese el codigo a Asociar -> ")
            cod=int(cod)

            rSilo.cod_prod=cod
            AL_SILOS.seek(0,2)
            formatSilo(rSilo)
            pickle.dump(rSilo,AL_SILOS)
            AL_SILOS.flush()
            print(f"El Silo {sil} fue registrado con éxito... \n ")
        else:
            print("Ya existe un Silo con ese nombre.\n")
        
        rta= input("Desea ingresar otro Silo? S-si   N-no: ").upper()
        while rta != "S" and rta != "N":
            rta = input("Por favor, solo S para Si o N para No:").upper()

def buscaSilo(silo):
    t = os.path.getsize(AF_SILOS)
    AL_SILOS.seek(0)
    ban=False
    while AL_SILOS.tell()<t and ban== False:
        pos = AL_SILOS.tell()
        rSilo = pickle.load(AL_SILOS)
        if rSilo.nom_silo.strip() == silo:
            return pos
    return -1

def buscaSilo_cod(cod):
    t = os.path.getsize(AF_SILOS)
    AL_SILOS.seek(0)
    ban=False
    while AL_SILOS.tell()<t and ban== False:
        pos = AL_SILOS.tell()
        rSilo = pickle.load(AL_SILOS)
        if int(rSilo.cod_silo) == int(cod):
            return pos
    return -1

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
    print("                         # 6 - ARCHIVOS")
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

def menu_crud_rubro():
    print( "")
    print("                         ##################################")
    print("                         |   MENU ALTA DE RUBROS          |")
    print("                         ##################################")
    print("                         # A - ALTA")
    print("                         # V - Volver al Menu Anterior")
    print("                         ----------------------------------")
    print("                         ##################################")
    print("" )

def menu_crud_silos():
    print( "")
    print("                         ##################################")
    print("                         |   MENU ALTA DE SILOS           |")
    print("                         ##################################")
    print("                         # A - ALTA")
    print("                         # V - Volver al Menu Anterior")
    print("                         ----------------------------------")
    print("                         ##################################")
    print("" )

def menu_Archivos():
    print( "")
    print("                         ##################################")
    print("                         | 6- MENU TEMP PARA VER ARCHIVOS |")
    print("                         ##################################")
    print("                         # 1 - Operaciones")
    print("                         # 2 - Productos")
    print("                         # 3 - Rubros")
    print("                         # 4 - Rubros x Productos")
    print("                         # 5 - Silos")
    print("                         # 0 - Volver al Menu Anterior")
    print("                         ----------------------------------")
    print("                         ##################################")
    print("" )

def mostrarOp(x):
    print(x.pat," - ",x.cod_prod," - ",x.fecha," - ",x.est," - ",x.pesob," - ",x.tara)

def mostrarProd(x):
    print(x.cod_prod," - ",x.nom_prod," - ",x.est)

def mostrarRub(x):
    print(x.cod_rub," - ",x.nom_rub)

def mostrarRxP(x):
    print(x.cod_prod," - ",x.cod_rub," - ",x.min," - ",x.max)

def mostrarSilo(x):
    print(x.cod_silo," - ",x.nom_silo," - ",x.cod_prod," - ",x.stock)

def archivos():
    flag=True
    while flag==True:
        
        menu_Archivos()
        opcion=input( "\n--> Ingrese la opción que desea usar, o 0 para volver al menú anterior: \n--> " )
        while opcion<"0" and opcion>"5":
            opcion=input( "\n--> Ingrese la opción que desea usar, o 0 para volver al menú anterior: \n--> " )
        
        if opcion == "1":
            global AF_OP, AL_OP
            os.system('cls')
            print(" OPCION 1 - MOSTRAR ARCHIVO OPERACIONES ")
            print(" ------------------------------------\n ")
            t=os.path.getsize(AF_OP)
            if t==0:
                print("El archivo está vacío")
                os.system('pause')
            else:
                print("-------------------------------------------------")
                print(" Patente CodPro Fecha     Est  PesoB   Tara   ")
                AL_OP.seek(0)
                while AL_OP.tell()<t:
                    rOp=pickle.load(AL_OP)
                    mostrarOp(rOp)
                AL_OP.seek(0)
                rOp=pickle.load(AL_OP)
                aux=AL_OP.tell()
                cant_reg=t//aux
                print("\nTamaño de registro = ",aux," - Cantidad de Registros = ", cant_reg)
                os.system('pause')
                      
        elif opcion == "2":
            global AF_PROD, AL_PROD
            os.system('cls')
            print(" OPCION 2 - MOSTRAR ARCHIVO PRODUCTOS ")
            print(" ------------------------------------\n ")
            t=os.path.getsize(AF_PROD)
            if t==0:
                print("El archivo está vacío")
                os.system('pause')
            else:
                print("-----------------------------------------")
                print(" CodPro - Producto  - Estado ")
                AL_PROD.seek(0)
                while AL_PROD.tell()<t:
                    rProd=pickle.load(AL_PROD)
                    mostrarProd(rProd)
                AL_PROD.seek(0)
                pickle.load(AL_PROD)
                aux=AL_PROD.tell()
                cant_reg=t//aux
                print("\nTamaño de registro = ",aux," - Cantidad de Registros = ", cant_reg)
                os.system('pause')

        elif opcion == "3":
            global AF_RUBRO, AL_RUBRO
            os.system('cls')
            print(" OPCION 3 - MOSTRAR ARCHIVO RUBROS ")
            print(" ------------------------------------\n ")
            t=os.path.getsize(AF_RUBRO)
            if t==0:
                print("El archivo está vacío")
                os.system('pause')
            else:
                print("-----------------------------------------")
                print(" CodPro - Producto ")
                AL_RUBRO.seek(0)
                while AL_RUBRO.tell()<t:
                    rRub=pickle.load(AL_RUBRO)
                    mostrarRub(rRub)
                AL_RUBRO.seek(0)
                pickle.load(AL_RUBRO)
                aux=AL_RUBRO.tell()
                cant_reg=t//aux
                print("\nTamaño de registro = ",aux," - Cantidad de Registros = ", cant_reg)
                os.system('pause')

        elif opcion == "4":
            global AF_RUBROP, AL_RUBROP
            os.system('cls')
            print(" OPCION 4 - MOSTRAR ARCHIVO RUBROS x PRODCUTOS ")
            print(" ------------------------------------\n ")
            t=os.path.getsize(AF_RUBROP)
            if t==0:
                print("El archivo está vacío")
                os.system('pause')
            else:
                print("-----------------------------------------")
                print(" CodPro - CodRub - Val Min - Val Max ")
                AL_RUBROP.seek(0)
                while AL_RUBROP.tell()<t:
                    rRxP=pickle.load(AL_RUBROP)
                    mostrarRxP(rRxP)
                AL_RUBROP.seek(0)
                pickle.load(AL_RUBROP)
                aux=AL_RUBROP.tell()
                cant_reg=t//aux
                print("\nTamaño de registro = ",aux," - Cantidad de Registros = ", cant_reg)
                os.system('pause')

        elif opcion == "5":
            global AF_SILOS, AL_SILOS
            os.system('cls')
            print(" OPCION 5 - MOSTRAR ARCHIVO SILOS ")
            print(" ------------------------------------\n ")
            t=os.path.getsize(AF_SILOS)
            if t==0:
                print("El archivo está vacío")
                os.system('pause')
            else:
                print("-----------------------------------------")
                print(" Codigo - Nombre - Producto - Stock ")
                AL_SILOS.seek(0)
                while AL_SILOS.tell()<t:
                    rSilo=pickle.load(AL_SILOS)
                    mostrarSilo(rSilo)
                AL_SILOS.seek(0)
                pickle.load(AL_SILOS)
                aux=AL_SILOS.tell()
                cant_reg=t//aux
                print("\nTamaño de registro = ",aux," - Cantidad de Registros = ", cant_reg)
                os.system('pause')

        elif opcion == "0":
            flag=False

def crud():
    flag=True
    while flag==True:
        
        menu_crud()
        opcion=input( "\n--> Ingrese la opción que desea usar, o V para volver al menú anterior: \n--> " )
            
        if opcion == "A" or opcion == "a":
            
            print( "")
            print("                          #####################################################")
            print("                          #####################################################")
            print("                          ##                                                 ##")
            print("                          ##                 ALTA DE PRODUCTO                ##")
            print("                          ##                                                 ##")
            print("                          #####################################################")
            print("                          #####################################################")
            

        elif opcion == "B" or opcion == "b":
            
            print("                         #####################################################")
            print("                         #####################################################")
            print("                         ##                                                 ##")
            print("                         ##                 BAJA DE PRODUCTO                ##")
            print("                         ##                                                 ##")
            print("                         #####################################################")
            print("                         #####################################################")
            

        elif opcion == "C" or opcion == "c":
            
            print( "                        #####################################################")
            print("                        #####################################################")
            print("                        ##                                                 ##")
            print("                        ##             CONSULTA DE PRODUCTO                ##")
            print("                        ##                                                 ##")
            print("                        #####################################################")
            print("                        #####################################################" )
            

        elif opcion == "M" or opcion == "m":
            
            print( "                        #####################################################")
            print("                        #####################################################")
            print("                        ##                                                 ##")
            print("                        ##           MODIFICACION DE PRODUCTO              ##")
            print("                        ##                                                 ##")
            print("                        #####################################################")
            print("                        #####################################################")
            
            
        elif opcion == "V" or opcion == "v":
            flag=False

def crud_productos():
    flag=True
    while flag==True:
        
        menu_crud()
        opcion=input( "\n--> Ingrese la opción que desea usar, o V para volver al menú anterior: \n--> " )
        
        if opcion == "A" or opcion == "a":
            
            alta_productos()
                              
        elif opcion == "B" or opcion == "b":
           
            baja_prod()
        
        elif opcion == "C" or opcion == "c":
          
            mostrar_productos()
        
        elif opcion == "M" or opcion == "m":
           
            modifica_prod()
        
        elif opcion == "V" or opcion == "v":
            flag=False

def crud_rubros():
    flag=True
    while flag==True:
        
        menu_crud_rubro()
        opcion=input( "\n--> Ingrese la opción que desea usar, o V para volver al menú anterior: \n--> " )
        
        if opcion == "A" or opcion == "a":
            
            alta_rubros()
                              
        elif opcion == "V" or opcion == "v":
            flag=False

def crud_silos():
    flag=True
    while flag==True:
        
        menu_crud_silos()
        opcion=input( "\n--> Ingrese la opción que desea usar, o V para volver al menú anterior: \n--> " )
        
        if opcion == "A" or opcion == "a":
            
            alta_silos()
                              
        elif opcion == "V" or opcion == "v":
            flag=False

def administraciones():
    flag=True
    while flag==True:
        os.system('cls')
        menu_01_administraciones()
        opcion=input( "\n--> Ingrese de la A a la G según la opción que desea usar, o V para volver al menú anterior: \n--> " )
        if opcion == "A" or opcion == "a":
            crud()
            
        elif opcion == "B" or opcion == "b":
            crud_productos()

        elif opcion == "C" or opcion == "c":
            crud_rubros()

        elif opcion == "D" or opcion == "d":
            crud()

        elif opcion == "E" or opcion == "e":
            crud_silos()

        elif opcion == "F" or opcion == "f":
            crud()

        elif opcion == "G" or opcion == "g":
            crud()

        elif opcion == "V" or opcion == "v":
            flag=False


################ PROGRAMA PRINCIPAL #######################

AF_OP = "tpn3\\TP3F\\OPERACIONES.DAT"
AF_PROD = "tpn3\\TP3F\\PRODUCTOS.DAT"
AF_RUBRO = "tpn3\\TP3F\\RUBROS.DAT"
AF_RUBROP = "tpn3\\TP3F\\RUBXPROD.DAT"
AF_SILOS = "tpn3\\TP3F\\SILOS.DAT"

if not os.path.exists('tpn3\\TP3F'):
    os.makedirs('tpn3\\TP3F')

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
    os.system('cls')    
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
        archivos()
    elif op == "7":
        peso_tara()
    elif op == "8":
        reportes()
    elif op == "9":
        silos()
        
    elif op =="0":
        flag=False

print("see you later, aligator...")