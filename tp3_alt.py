# -*- coding: utf-8 -*-
import os
import os.path
import pickle
from datetime import datetime
import re

patente6=re.compile("[A-Z]{3}[0-9]{3}")
patente7=re.compile("[A-Z]{2}[0-9]{3}[A-Z]{2}")

#### COLORES ####
class c:
    verde = '\033[92m'
    amarillo = '\033[93m'
    rojo = '\033[91m'
    resetear = '\033[0m'
    bold = '\033[1m'

#### CREAMOS LOS CONSTRUCTORES ####

class oper:
    def __init__(self):
        self.pat = ""
        self.cod_prod = 0
        self.fecha = ""
        self.est = ""
        self.pesob = 0
        self.tara = 0
        self.neto = 0

class prod:
    def __init__(self):
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
    vrOp.pesob = vrOp.pesob.ljust(8)
    vrOp.tara = str(vrOp.tara)
    vrOp.tara = vrOp.tara.ljust(8)
    vrOp.neto = str(vrOp.neto)
    vrOp.neto = vrOp.neto.ljust(8)

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
    vrRxP.min = vrRxP.min.ljust(5)
    vrRxP.max = str(vrRxP.max)
    vrRxP.max = vrRxP.max.ljust(5)
    
def formatSilo(vrSilo):
    vrSilo.cod_silo = str(vrSilo.cod_silo)
    vrSilo.cod_silo = vrSilo.cod_silo.ljust(2)
    vrSilo.nom_silo = vrSilo.nom_silo.ljust(15)
    vrSilo.cod_prod = str(vrSilo.cod_prod)
    vrSilo.cod_prod = vrSilo.cod_prod.ljust(2)
    vrSilo.stock = str(vrSilo.stock)
    vrSilo.stock = vrSilo.stock.ljust(8)

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

def validaRangoReal(nro, min,max):
    try:              
        nro = float(nro)
        min = float(min)      
        if nro >= min and nro <= max:
            return False 
        else:
            return True  
    except:
        return True 
def ApruebaRangoReal(nro, min,max):
        nro = float(nro)
        min = float(min)
        max = float(max)      
        if nro >= min and nro <= max:
            return True 
        else:
            return False  
    
def validarFecha():
  actual=datetime.today()
  actuall=datetime.strftime(actual, '%d/%m/%Y')
  flag = True
  fla = True
  print("La fecha a ingresar podra ser mayor o igual a la fecha de hoy")
  
  while flag:
    try:
      fech = input("Ingresa una fecha en el formato DD/MM/AAAA: ")
      fecha=datetime.strptime(fech, '%d/%m/%Y')
      fechaa=datetime.strftime(fecha, '%d/%m/%Y')
      fla = False
    except ValueError:
      print(c.rojo + "Fecha invalida" + c.resetear)
    if fla == False:
      if actual < fecha:
        flag = False
        return fechaa
      elif actuall == fechaa:
        flag = False
        return fechaa
      else:
        print(c.rojo + "Fecha invalida" + c.resetear)

def cant_prod_viejo():
    t=os.path.getsize(AF_PROD)
    if t==0:
        return 0
    else:
        AL_PROD.seek(0)
        pickle.load(AL_PROD)
        aux=AL_PROD.tell()
        cant_reg=t//aux
        return cant_reg

### SE CAMBIO DE LA VERSION ANTERIOR A ESTA PORQUE LA OTRA SOLIA DAR ERRONEO. 
### SUPONGO QUE POR LA DIVISION ENTERA

def cant_prod():
    t=os.path.getsize(AF_PROD)
    cont=0
    if t==0:
        return 0
    else:
        AL_PROD.seek(0)
        while AL_PROD.tell()<t:
            cont+=1
            pickle.load(AL_PROD)
        return cont

def alta_productos():
    os.system('cls')
    print(c.bold + "                           Opcion A - Alta de productos " + c.resetear)
    print("                         __________________________________\n")
    rta='S'
    while rta=='S':
        os.system('cls')
        pro=input("Ingrese el producto [hasta 15 caracteres] :  ")
        while len(pro)<3 or len(pro)>=15 or pro.isalpha()==False:
            print(c.rojo + "ERROR. Ingrese el producto [hasta 15 caracteres] :  " + c.resetear)
            pro=input()
        pro=pro.upper()
        RegProd=prod()
        if buscaProducto(pro) == -1:
            RegProd.cod_prod=cant_prod()+1
            RegProd.nom_prod=pro
            RegProd.est="B"
            AL_PROD.seek(0,2)
            formatProd(RegProd)
            pickle.dump(RegProd,AL_PROD)
            AL_PROD.flush()
            print(c.verde + f"El producto {pro} fue registrado con éxito... \n " + c.resetear)
        else:
            print("⚠ El producto ya se encuentra registrado. Verifique el estado\n")
        
        rta= input("Desea ingresar otro producto? S-si   N-no: ")
        while rta != "S" and rta != "N" and rta !="s" and rta != "n":
            print(c.rojo + "⚠ Por favor, solo S para Si o N para No:" + c.resetear)
            rta=input()
        
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
        Regop= oper()
        #Regop=pickle.load(AL_OP)
        
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
        print("⚠ No hay productos para Borrar")
        os.system('pause')
    else:
        rta='S'
        while rta=='S':
            mostrar_productos_all()
            cantp=cant_prod()
            cod=input(f"Ingrese el codigo de producto a borrar o 0 para no modificar nada → ")
            while validaRangoEntero(cod,0,cantp):
                cod=input(f"Ingrese el codigo de producto a borrar o 0 para no modificar nada → ")
            cod=int(cod)
            if cod!=0:
                #Busco si ya ingresó un camión con ese producto
                if busco_prod_cam(cod):
                    print("⚠ Un camion ya ha ingresado con este producto, por lo tanto no se puede borrar.")
                else:

                    pos=buscaProducto_cod(cod)
                    rPro=prod()
                    AL_PROD.seek(pos,0)
                    rPro=pickle.load(AL_PROD)
                    rPro.est="B"
                    AL_PROD.seek(pos)
                    pickle.dump(rPro,AL_PROD)
                    AL_PROD.flush()
                    print(c.verde + "Baja existosa." + c.resetear)
            
                rta= input("Desea eliminar otro producto? S-si   N-no: ").upper()
                while rta != "S" and rta != "N" and rta !="s" and rta != "n":
                    print(c.rojo + "⚠ Por favor, solo S para Si o N para No:" + c.resetear)
                    rta = input()
            else:
                rta="N"

def modifica_prod():
    global AF_PROD, AL_PROD
    os.system('cls')
    t=os.path.getsize(AF_PROD)
    if t==0:
        print( "⚠ No hay productos para modificar")
        os.system('pause')
    else:
        rta='S'
        while rta=='S':
            mostrar_productos_all()
            cantp=cant_prod()
            cod=input(f"Ingrese el codigo de producto a modificar o 0 para salir sin hacer cambios → ")
            while validaRangoEntero(cod,0,cantp):
                print(c.rojo + f"ERROR. Ingrese el codigo de producto a modificar o 0 para salir sin hacer cambios  → " + c.resetear)
                cod=input()
            cod=int(cod)
            if cod!=0:
                #Busco si ya ingresó un camión con ese producto
                if busco_prod_cam(cod):
                    print("⚠ Un camion ya ha ingresado con este producto, por lo tanto no se puede modificar.")
                else:
                    pos=buscaProducto_cod(cod)
                    rPro=prod()
                    AL_PROD.seek(pos,0)
                    rPro=pickle.load(AL_PROD)
                    cambia_nom=input("Desea cambiar el nombre? [S = cambia] [N = No cambia] ").upper()
                    while cambia_nom!="S" and cambia_nom!="N":
                        cambia_nom=input("Desea cambiar el nombre? [S = cambia] [N = No cambia] ").upper()
                    if cambia_nom=="S":
                        nom=input("Modifique el nombre del producto: ").upper()
                        while len(nom)<3 or len(nom)>15:
                            print(c.rojo + "ERROR. El nombre de producto debe tener entre 3 y 15 caracteres" + c.resetear).upper()
                            nom=input()
                        rPro.nom_prod=nom.ljust(15)
                        
                    cambia_est=input("Desea cambiar el estado? [S = cambia] [N = No cambia] ").upper()
                    while cambia_est!="S" and cambia_est!="N":
                        cambia_est=input("Desea cambiar el estado? [S = cambia] [N = No cambia] ").upper()
                    if cambia_est=="S":
                        if rPro.est=="A":
                            rPro.est="B"
                        else:
                            rPro.est="A"
                    AL_PROD.seek(pos)
                    pickle.dump(rPro,AL_PROD)
                    AL_PROD.flush()
                    print(c.verde + "Modificación existosa." + c.resetear)
                    mostrarProd(rPro)

                rta= input("Desea modificar otro producto? S-si   N-no: ").upper()
                while rta != "S" and rta != "N" and rta !="s" and rta != "n":
                    print(c.rojo + "⚠ Por favor, solo S para Si o N para No:" + c.resetear)
                    rta=input()
            else:
                rta="N" 

def mostrar_productos_all(): # MUESTRA TODOS LOS PRODUCTOS
    global AF_PROD, AL_PROD
    os.system('cls')
    t=os.path.getsize(AF_PROD)
    if t==0:
        print( "⚠ No hay productos para mostrar")
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
        print( "⚠ No hay productos para mostrar")
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
    cont=0
    if t==0:
        return 0
    else:
        AL_RUBRO.seek(0)
        while AL_RUBRO.tell()<t:
            cont+=1
            pickle.load(AL_RUBRO)
        return cont

def alta_rubros():
    os.system('cls')
    print(c.bold + "                            Opcion A - Alta de rubros " + c.resetear)
    print("                         __________________________________\n")
    rta='S'
    while rta=='S':
        os.system('cls')
        rub=input("Ingrese el rubro [hasta 15 caracteres] :  ")
        while len(rub)<3 or len(rub)>=15:
            print(c.rojo + "ERROR. Ingrese el Rubro [hasta 15 caracteres] :  " + c.resetear)
            rub=input()
        rub=rub.upper()
        rRub=rubro()
        if buscaRubro(rub) == -1:
            rRub.cod_rub=cant_rub()+1
            rRub.nom_rub=rub
            AL_RUBRO.seek(0,2)
            formatRub(rRub)
            pickle.dump(rRub,AL_RUBRO)
            AL_RUBRO.flush()
            print(c.verde + f"El Rubro {rub} fue registrado con éxito... \n " + c.resetear)
        else:
            print("El Rubro ya se encuentra registrado.\n")
        
        rta= input("Desea ingresar otro rubro? S-si   N-no: ").upper()
        while rta != "S" and rta != "N" and rta !="s" and rta != "n":
            print(c.rojo + "⚠ Por favor, solo S para Si o N para No:" + c.resetear)
            rta=input()

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

def mostrar_rubros_all(): # MUESTRA TODOS LOS RUBROS
    global AF_RUBRO, AL_RUBRO
    os.system('cls')
    t=os.path.getsize(AF_RUBRO)
    if t==0:
        print( "⚠ No hay Rubros para mostrar")
        os.system('pause')
    else:
        rRub=rubro()
        print("-----------------------------------------")
        print(" CodRub - Rubro  ")
        AL_RUBRO.seek(0)
        while AL_RUBRO.tell()<t:
            rRub=pickle.load(AL_RUBRO)
            mostrarRub(rRub)

############### ALTA DE RUBROS x PRODUCTO ###############

def buscaRxP_cod(pro,rub):
    t = os.path.getsize(AF_RUBROP)
    AL_RUBROP.seek(0)
    ban=False
    while AL_RUBROP.tell()<t and ban== False:
        rRxP = pickle.load(AL_RUBROP)
        if int(rRxP.cod_prod) == int(pro) and int(rRxP.cod_rub) == int(rub):
            ban=True
            return True
    return False

def alta_RxP():
    global AF_PROD,AF_RUBRO,AF_RUBROP,AL_PROD,AL_RUBRO,AL_RUBROP
    os.system('cls')
    print(c.bold + "                       Opcion A - Alta de rubros por producto " + c.resetear)  
    print("                         __________________________________\n")                       
    r=os.path.getsize(AF_RUBRO)
    p=os.path.getsize(AF_PROD)
    if r==0 and p==0:
        print("⚠ Productos y rubros deben contener datos para trabajar en esta carga ")
        os.system('pause')
    else:
        rta='S'
        while rta=='S':
            mostrar_productos_all()
            cantp=cant_prod()
            codp=input("Ingrese el código del producto con el que quiera trabajar o 0 para cancelar → ")
            while validaRangoEntero(codp,0,cantp):
                print(c.rojo + "ERROR. Ingrese el código del producto con el que quiera trabajar o 0 para cancelar → " + c.resetear)
                codp=input()
            codp=int(codp)
            if codp!=0:
                posp=buscaProducto_cod(codp)
                AL_PROD.seek(posp)
                rProd=pickle.load(AL_PROD)
                mostrar_rubros_all()
                cantr=cant_rub()
                codr=input(f"Ingrese el código del Rubro con el que quieras asociar a {rProd.nom_prod.strip()} → ")
                while validaRangoEntero(codr,0,cantr):
                    codr=input(f"Ingrese el código del Rubro con el que quieras asociar a {rProd.nom_prod.strip()} → ")
                codr=int(codr)
                if codr!=0:
                    posr=buscaRubro_cod(codr)
                    AL_RUBRO.seek(posr)
                    rRub=pickle.load(AL_RUBRO)
                    if buscaRxP_cod(codp,codr):
                        print(f"El rubro {rRub.nom_rub.strip()} ya se encuentra asociado al producto {rProd.nom_prod.strip()} ")
                    else:
                        rRxP=rubrop()
                        rRxP.cod_prod=codp
                        rRxP.cod_rub=codr
                        
                        rRxP.min=input(f"Ingrese el valor MINIMO para {rRub.nom_rub.strip()} [entre 0 y 100] → ")
                        while validaRangoReal(rRxP.min,0,100):
                            rRxP.min=input(f"Ingrese el valor MINIMO para {rRub.nom_rub.strip()} [entre 0 y 100] → ")
                        
                        rRxP.max=input(f"Ingrese un valor mayor a {rRxP.min}, para registrar el MAXIMO de {rRub.nom_rub.strip()} [entre {rRxP.min} y 100] → ")
                        while validaRangoReal(rRxP.max,rRxP.min,100):
                            rRxP.max=input(f"Ingrese un valor mayor a {rRxP.min}, para registrar el MAXIMO de {rRub.nom_rub.strip()} [entre {rRxP.min} y 100] → ")
                        
                        AL_RUBROP.seek(0,2)
                        formatRxP(rRxP)
                        pickle.dump(rRxP,AL_RUBROP)
                        AL_RUBROP.flush()
                        print(f"Asociado {rProd.nom_prod.strip()} y {rRub.nom_rub.strip()}, con un mínimo de {rRxP.min.strip()} y un máximo de {rRxP.max.strip()} ")
                        
            
            rta= input("Desea ingresar rubro por producto? S-si   N-no: ").upper()
            while rta != "S" and rta != "N" and rta !="s" and rta != "n":
                rta= input("Desea ingresar rubro por producto? S-si   N-no: ")
    
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
    print(c.bold + "                              Opcion A - Alta de Silos " + c.resetear)
    print("                         __________________________________\n")
    rta='S'
    while rta=='S':
        os.system('cls')
        sil=input("Ingrese el nombre del silo [hasta 15 caracteres] :  ")
        while len(sil)<3 or len(sil)>=15:
            print(c.rojo + "ERROR. Ingrese el nombre del silo [hasta 15 caracteres] :  " + c.resetear)
            sil=input()
        sil=sil.upper()
        rSilo=silo()
        if buscaSilo(sil) == -1:
            rSilo.cod_silo=cant_silos()+1
            rSilo.nom_silo=sil
            
            print(f"Elija el producto que desea asociar al silo {sil} ")
            mostrar_productos()
            print()
            cantp=cant_prod()
            cod=input(f"Ingrese el codigo de producto a asociar con silo {sil} → ")
            while validaRangoEntero(cod,1,cantp):
                print(c.rojo + f"ERROR. Ingrese el codigo a Asociar → " + c.resetear)
                cod=input()
            cod=int(cod)

            rSilo.cod_prod=cod
            AL_SILOS.seek(0,2)
            formatSilo(rSilo)
            pickle.dump(rSilo,AL_SILOS)
            AL_SILOS.flush()
            print(c.verde + f"El Silo {sil} fue registrado con éxito... \n " + c.resetear)
        else:
            print("⚠ Ya existe un Silo con ese nombre.\n")
        
        rta= input("Desea ingresar otro Silo? S-si   N-no: ").upper()
        while rta != "S" and rta != "N" and rta !="s" and rta != "n":
            print(c.rojo + "⚠ Por favor, solo S para Si o N para No:" + c.resetear)
            rta=input()

def buscaSilo(silo):
    t = os.path.getsize(AF_SILOS)
    AL_SILOS.seek(0)
    while AL_SILOS.tell()<t:
        pos = AL_SILOS.tell()
        rSilo = pickle.load(AL_SILOS)
        if rSilo.nom_silo.strip() == silo:
            return pos
    return -1

def buscaSilo_cod(cod):
    t = os.path.getsize(AF_SILOS)
    AL_SILOS.seek(0)
    while AL_SILOS.tell()<t:
        pos = AL_SILOS.tell()
        rSilo = pickle.load(AL_SILOS)
        if int(rSilo.cod_silo) == int(cod):
            return pos
    return -1

############# ENTREGA DE CUPOS ####################

################### PROVISORIO ###################
def entrega_cupos():
    global AF_OP, AL_OP
    rOp=oper()
    rOp.pat=validarPatente()
    e=Busco_patente(rOp.pat)
    if e!=-1:
        print("⚠ Cupo ya otorgado")
        os.system('pause')
        ### Acá seguiría la parte si quiero ofrecer agregar en otra fecha

    else:
        canp=cant_prod()
        mostrar_productos_all()
        print()
        rOp.cod_prod=input("Ingrese el código del producto → ")
        while rOp.cod_prod<"1" or rOp.cod_prod>str(canp):
            rOp.cod_prod=input("Ingrese el código del producto → ")
        rOp.fecha=validarFecha()
        rOp.est="P"
        AL_OP.seek(0,2)
        formatOp(rOp)
        pickle.dump(rOp,AL_OP)
        AL_OP.flush()
        print(c.verde + f"El cupo para {rOp.pat} fue registrado con éxito... \n " + c.resetear)
        os.system('pause')
############# TERMINA PROVISORIO #########################

def validarPatente():
  f=True
  while f==True:
    pat=str.upper(input("Ingrese patente en formato ABC123 o AB123CD:"))
    x=len(pat)
    if x==6:
      if patente6.match(pat):
        f=False
        return pat
    if x==7:
      if patente7.match(pat):
        f=False
        return pat

################# 3. RECEPCION ########################


def fecha_hoy(): # PARA OBTENER FECHA DE HOY
    hoy=datetime.now()
    hoy=hoy.strftime('%d/%m/%Y')
    return hoy

hoy=fecha_hoy() # VARIABLE GLOBAL PARA FECHA DE HOY

def Busco_patente(pat):
    global AF_OP, AL_OP
    t = os.path.getsize(AF_OP)
    AL_OP.seek(0)
    while AL_OP.tell()<t:
        pat_e = AL_OP.tell()
        RegOp = pickle.load(AL_OP)
        if RegOp.pat == pat.ljust(7):
            return pat_e
    return -1

def recepcion():
    global AF_OP, AL_OP
    os.system('cls')
    print(c.bold + "                                Opcion 3 - Recepcion " + c.resetear)
    print("                         __________________________________\n")
    t = os.path.getsize(AF_OP)
    if t==0:
        print("No se han otorgado cupos")
    else:
        rta='S'
        while rta=='S':
            os.system('cls')
            pat=validarPatente()
            pat=pat.upper()
            RegOp= oper()
            if Busco_patente(pat) != -1:
                pat_e = Busco_patente(pat)
                AL_OP.seek(pat_e,0)
                RegOp = pickle.load(AL_OP)
                if RegOp.fecha.strip()==hoy and RegOp.est.strip()=="P":
                    RegOp.est = "A"
                    AL_OP.seek(pat_e,0)
                    pickle.dump(RegOp, AL_OP)
                    AL_OP.flush()
                    print(c.verde + "El estado de su camion ha cambiado a arribado\n" + c.resetear)
                
                elif RegOp.fecha.strip()==hoy and RegOp.est.strip()=="A":
                    print(f"⚠ Su camion {RegOp.pat.strip()} ya se encuentra en estado de arribado")

                elif RegOp.fecha.strip()==hoy and RegOp.est.strip()!="P" and RegOp.est.strip()!="A":
                    print(f"⚠ El camion ingresado {pat} no se encuentra en pendientes")

                elif RegOp.fecha.strip()>hoy and RegOp.est.strip()=="P":
                    print(f"⚠ Su cupo está asignado para la fecha: {RegOp.fecha.strip()} ")
                
                elif RegOp.fecha.strip()<hoy and RegOp.est.strip()=="P":
                    print(f"⚠ Su cupo estaba asignado para la fecha: {RegOp.fecha.strip()}. Solicite un nuevo Cupo. ")

            else:
                print("⚠ La patente ingresada no tiene cupo")
                
            rta= input("Desea ingresar otra patente? S-si   N-no: ").upper()
            while rta != "S" and rta != "N" and rta !="s" and rta != "n":
                print(c.rojo + "⚠ Por favor, solo S para Si o N para No:" + c.resetear)
                rta=input()

################# 4. REGISTRAR CALIDAD ########################

def buscar_cupos_hoy():
    global AF_OP, AL_OP,AF_PROD,AL_PROD
    t = os.path.getsize(AF_OP)
    AL_OP.seek(0)
    print(" Camiones habilitados para el", hoy)
    while AL_OP.tell()<t:
        pos = AL_OP.tell()
        RegOp = pickle.load(AL_OP)
        if RegOp.fecha.strip() == hoy:
            cod=int(RegOp.cod_prod)
            posp=buscaProducto_cod(cod)
            AL_PROD.seek(posp)
            rProd=pickle.load(AL_PROD)
            print(f"Patente: {RegOp.pat.strip()} - Producto: {rProd.nom_prod.strip()} ")
            return pos
    return -1

def mostrar_RxP(prod):
    global AF_OP, AL_OP,AF_RUBROP,AL_RUBROP, AF_RUBRO,AL_RUBRO,AF_PROD,AL_PROD
    t = os.path.getsize(AF_RUBROP)
    AL_RUBROP.seek(0)
    print("Control de calidad por producto\n")
    cont=0
    print("\nIngrese valores para cada ítem → \n")
    while AL_RUBROP.tell()<t:
        posRxP = AL_RUBROP.tell()
        rRxP = pickle.load(AL_RUBROP)
        if int(rRxP.cod_prod) == int(prod):
            posp=buscaProducto_cod(prod)
            AL_PROD.seek(posp)
            rProd=pickle.load(AL_PROD)
            producto=rProd.nom_prod.strip()
            
            rub=int(rRxP.cod_rub)
            posrub=buscaRubro_cod(rub)
            AL_RUBRO.seek(posrub)
            rRub=pickle.load(AL_RUBRO)
            rubro=rRub.nom_rub.strip()
            
            min=float(rRxP.min)
            max=float(rRxP.max)
            
            print(f"Producto: {producto} - Rubro: {rubro} ")
            valor=input(f"Ingrese el valor para {rubro}. [Entre 0 y 100] ")
            while validaRangoReal(valor,0,100):
                print(c.rojo + f"ERROR. Ingrese el valor de {rubro}. [Entre 0 y 100] " + c.resetear)
                valor=input()
            if ApruebaRangoReal(valor,min,max):
                cont+=1
                print(c.verde + "Valor dentro del rango" + c.resetear)
                
            else:
                print(c.rojo + "Valor fuera del rango" + c.resetear)
    
    return cont
    
def registrar_calidad():
    global AF_OP, AL_OP,AF_PROD,AL_PROD,AF_RUBRO,AL_RUBRO,AF_RUBROP,AL_RUBROP
    os.system('cls')
    print(c.bold + "                            Opcion 3 - Registrar calidad " + c.resetear)
    print("                         __________________________________\n")
    t = os.path.getsize(AF_OP)
    if buscar_cupos_hoy()==-1:
        print( "⚠ No hay camiones para hoy")
    else:
        rta='S'
        while rta=='S':
            #buscar_cupos_hoy()
            #os.system('cls')
            pat=validarPatente()
            pat=pat.upper()
            RegOp= oper()
            if Busco_patente(pat) != -1:
                pat_e = Busco_patente(pat)
                AL_OP.seek(pat_e,0)
                RegOp = pickle.load(AL_OP)
                if RegOp.fecha.strip()==hoy and RegOp.est.strip()=="A":
                    producto=int(RegOp.cod_prod)
                    if mostrar_RxP(producto)>=2:
                        RegOp.est="C"
                        AL_OP.seek(pat_e,0)
                        pickle.dump(RegOp,AL_OP)
                        AL_OP.flush()
                        print(c.verde + "\nCamión APROBADO con calidad\n" + c.resetear)
                    else:
                        RegOp.est="R"
                        AL_OP.seek(pat_e,0)
                        pickle.dump(RegOp,AL_OP)
                        AL_OP.flush()
                        print(c.rojo + "\nCamión RECHAZADO por baja calidad\n" + c.resetear)
                
            rta= input("Desea ingresar otra patente? S-si   N-no: ").upper()
            while rta != "S" and rta != "N" and rta !="s" and rta != "n":
                rta = input(c.rojo + "⚠ Por favor, solo S para Si o N para No:" + c.resetear)
             
################# 5. REGISTRAR PESO BRUTO ########################

def bruto():
    global AF_OP, AL_OP
    os.system('cls')
    print(c.bold + "                          Opcion 5 - Registrar peso bruto " + c.resetear)
    print("                         __________________________________\n")
    rta='S'
    while rta=='S':
        pat=validarPatente()
        pat=pat.upper()
        RegOp= oper()
        if Busco_patente(pat) != -1:
            pat_e = Busco_patente(pat)
            AL_OP.seek(pat_e,0)
            RegOp = pickle.load(AL_OP)
            A= RegOp.est
            if A == "C":
                bru=input("Ingrese peso bruto: [Límite Legal Argentino = 45.000 Kg] tolerancia + 5000 Kg ")
                while validaRangoEntero(bru,8000,50000):
                    bru=int(bru)
                    if bru<8000:
                        print("⚠ El peso mínimo de un camión es de 8000 Kg ")
                    bru=input("Ingrese peso bruto: [Límite Legal Argentino = 45.000 Kg] tolerancia + 5000 Kg ")
                RegOp.pesob = bru
                RegOp.est = "B"
                AL_OP.seek(pat_e,0)
                formatOp(RegOp)
                pickle.dump(RegOp, AL_OP)
                AL_OP.flush()
                print(c.verde + f"El peso bruto ha sido registrado con exito para la patente {pat}" + c.resetear)

            elif Busco_patente(pat) != -1 and A == "R":
                print(c.rojo + f"⚠ El camion patente: {pat} se encuentra en estado de Rechazado." + c.resetear)
            
            elif Busco_patente(pat)!= -1 and A =="A":
                print("⚠ El camion se encuentra como: Arribado. Debe dirigirse a Registrar Calidad")

            elif Busco_patente(pat) != -1 and A == "P":
                print("⚠ Su camion se encuentra en pendientes. Debe recibirlo y registrar calidad")
        else:
            print(c.rojo + "⚠ La patente ingresada no ha sido encontrada\n" + c.resetear)
        rta= input("Desea ingresar otra patente? S-si   N-no: ").upper()
        while rta != "S" and rta != "N" and rta !="s" and rta != "n":
            print(c.rojo + "⚠ Por favor, solo S para Si o N para No:" + c.resetear)
            rta=input()

################# 6. MOSTRAR ARCHIVOS ########################

def archivos():
    flag=True
    while flag==True:
        os.system('cls')
        menu_Archivos()
        opcion=input( "\n → Ingrese la opción que desea usar, o 0 para volver al menú anterior: \n → " )
                
        if opcion == "1":
            global AF_OP, AL_OP
            os.system('cls')
            print(c.bold + "                           Opcion 1 - Archivo Operaciones " + c.resetear)
            print("                         __________________________________\n")
            t=os.path.getsize(AF_OP)
            if t==0:
                print("⚠ El archivo está vacío")
                os.system('pause')
            else:
                print("-------------------------------------------------")
                print(" Patente CodPro Fecha     Est  PesoB   Tara   PesoN ")
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
            print(c.bold + "                            Opcion 2 - Archivo Productos " + c.resetear)
            print("                         __________________________________\n")
            t=os.path.getsize(AF_PROD)
            if t==0:
                print("⚠ El archivo está vacío")
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
            print(c.bold + "                             Opcion 3 - Archivo Rubros " + c.resetear)
            print("                         __________________________________\n")
            t=os.path.getsize(AF_RUBRO)
            if t==0:
                print("⚠ El archivo está vacío")
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
            print(c.bold + "                       Opcion 4 - Archivo Rubros por Productos " + c.resetear)
            print("                         __________________________________\n")
            t=os.path.getsize(AF_RUBROP)
            if t==0:
                print("⚠ El archivo está vacío")
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
            print(c.bold + "                              Opcion 5 - Archivo Silos " + c.resetear)
            print("                         __________________________________\n")
            t=os.path.getsize(AF_SILOS)
            if t==0:
                print("⚠ El archivo está vacío")
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

        elif opcion == "6":
            os.system('cls')
            cantp=cant_prod()
            print(c.bold + "                            Patentes con menor descarga      " + c.resetear)
            print("                         __________________________________\n")
            for i in range(1,cantp+1):
                if busco_prod_cam(i):
                    posprod=buscaProducto_cod(i)
                    AL_PROD.seek(posprod)
                    rProd=pickle.load(AL_PROD)
                    nomprod=rProd.nom_prod.strip()
                    aaa=menor_patente(i)
                    if aaa!=-1:
                        print(f"La patente con menor descarga para {nomprod} es {aaa}\n")
            os.system('pause')
                    
        elif opcion == "7":
            alta_prov()

        elif opcion == "0":
            flag=False

def alta_prov():
    global AF_OP,AL_OP
    os.system('cls')
    print(c.bold + "                                  Alta provisoria " + c.resetear)
    print("                         __________________________________\n")
    rta='S'
    while rta=='S':
        t=os.path.getsize(AF_OP)
        if t==0:
            rOp=oper()
            AL_OP.seek(0)
            rOp.pat = validarPatente()
            rOp.cod_prod = input("Codigo de producto → ")
            rOp.fecha = validarFecha()
            rOp.est = input("Ingrese estado P.A.C.B.R.F → ").upper()
            rOp.pesob = int(input("Ingrese el peso bruto [Max: 50000 Kg Min: 8000 Kg] →"))
            rOp.tara = int(input("Ingrese la tara [Max: 30000 Kg Min: 1000 Kg] →"))
            rOp.neto = int(rOp.pesob-rOp.tara)
            formatOp(rOp)
            pickle.dump(rOp,AL_OP)
            AL_OP.flush()
            print(c.verde + f"Operación fue registrado con éxito... \n " + c.resetear)
            os.system('pause')
        else:
            os.system('cls')
            rOp=oper()
            AL_OP.seek(0,2)
            rOp.pat = validarPatente()
            rOp.cod_prod = input("Codigo Producto → ")
            rOp.fecha = validarFecha()
            rOp.est = input("Ingrese estado P.A.C.B.R.F → ").upper()
            rOp.pesob = int(input("Ingrese peso bruto entre 8000 y 50000 →"))
            rOp.tara = int(input("Ingrese TARA entre 1000 y 30000 →"))
            rOp.neto = int(rOp.pesob-rOp.tara)
            formatOp(rOp)
            pickle.dump(rOp,AL_OP)
            AL_OP.flush()
            print(c.verde + f"Operación fue registrado con éxito... \n " + c.resetear)
            os.system('pause')
        rta= input("Desea ingresar otro? S-si   N-no: ").upper()
        while rta != "S" and rta != "N" and rta !="s" and rta != "n":
            rta = input(c.rojo + "⚠ Por favor, solo S para Si o N para No:" + c.resetear)

def menor_patente(prod):
    global AF_OP, AL_OP
    t = os.path.getsize(AF_OP)
    AL_OP.seek(0)
    produc=prod
    menor=100000
    patente=""
    while AL_OP.tell()<t:
        pat_e = AL_OP.tell()
        RegOp = pickle.load(AL_OP)
        esta=RegOp.est.strip()
        neto=int(RegOp.neto)
        if int(RegOp.cod_prod) == produc and esta=="F":
            if neto<menor:
                menor=neto
                patente=RegOp.pat.strip()
    return patente

def mostrarOp(x):
    print(x.pat," - ",x.cod_prod," - ",x.fecha," - ",x.est," - ",x.pesob," - ",x.tara," - ",x.neto)

def mostrarProd(x):
    print(x.cod_prod," - ",x.nom_prod," - ",x.est)

def mostrarRub(x):
    print(x.cod_rub," - ",x.nom_rub)

def mostrarRxP(x):
    print(x.cod_prod," - ",x.cod_rub," - ",x.min," - ",x.max)

def mostrarSilo(x):
    print(x.cod_silo," - ",x.nom_silo," - ",x.cod_prod," - ",x.stock)


################# 7. REGISTRAR TARA ########################

def tara():
    global AF_OP, AL_OP,AF_SILOS,AL_SILOS
    os.system('cls')
    print(c.bold + "                             Opcion 7 - Registrar tara " + c.resetear)
    print("                         __________________________________\n")
    rta='S'
    while rta=='S':
        os.system('cls')
        pat=validarPatente()
        pat=pat.upper()
        RegOp= oper()
        if Busco_patente(pat) != -1:
            pat_e = Busco_patente(pat)
            AL_OP.seek(pat_e,0)
            RegOp = pickle.load(AL_OP)
            A= RegOp.est
            B= RegOp.pesob

            if A == "B":

                tara=input("Ingrese Tara: [Límite Legal Argentino = 30.000 Kg] tolerancia + 5000 Kg ")
                while validaRangoEntero(tara,1000,35000) and int(tara)>int(B):
                    tara=int(tara)
                    if tara>B:
                        print("⚠ La tara no puede ser mayor al Peso bruto. ")
                    tara=input("Ingrese Tara: [Límite Legal Argentino = 30.000 Kg] tolerancia + 5000 Kg ")
                tara=int(tara)
                RegOp.tara = tara
                RegOp.neto = tara-int(B)
                RegOp.est = "F"
                AL_OP.seek(pat_e,0)
                formatOp(RegOp)
                pickle.dump(RegOp, AL_OP)
                AL_OP.flush()

                ####### CARGO SILO #######

                print(c.verde + "\nSu tara ha sido registrada con exito. Felicitaciones! Ha finalizado su proceso\n" + c.resetear)

            elif Busco_patente(pat)!= -1 and A == "R":
                print("⚠ Su camion se encuentra en estado de rechazado")
            elif Busco_patente(pat)!= -1 and A =="A":
                print("⚠ Su camion se encuentra en arribado, debe dirigirse a registrar su calidad")
            elif Busco_patente(pat)!= -1 and A =="C":
                print("⚠ Su camion aun no ha registrado su peso bruto")
            elif Busco_patente(pat) != -1 and A == "P":
                print("⚠ Su camion se encuentra en pendientes")
        else:
            print("La patente ingresada no ha sido encontrada")
        rta= input("Desea ingresar otra patente? S-si   N-no: ").upper()
        while rta != "S" and rta != "N" and rta !="s" and rta != "n":
            print(c.rojo + "⚠ Por favor, solo S para Si o N para No:" + c.resetear)
            rta=input()

################# 8. REPORTES ########################

####### CUPOS OTORGADOS HISTORICAMENTE Y HOY ######

def Cupos_Otorgados():
    t=os.path.getsize(AF_OP)
    AL_OP.seek(0)
    RegOp = oper()
    c=0
    if t == 0:
        print("⚠ No hay cupos otorgados")
    else:
        while AL_OP.tell() < t:
            RegOp= pickle.load(AL_OP)
            if RegOp.est=="A" or RegOp.est=="P" or RegOp.est=="C" or RegOp.est=="B" or RegOp.est=="R" or RegOp.est=="F":
                c+=1
    print(f"La cantidad de cupos otorgados fue de: {c} \n")

def Cupos_Otorgados_hoy():
    t=os.path.getsize(AF_OP)
    AL_OP.seek(0)
    RegOp = oper()
    ch=0
    if t == 0:
        print("⚠ No hay cupos otorgados")
    else:
        while AL_OP.tell() < t:
            RegOp= pickle.load(AL_OP)
            if RegOp.fecha == hoy:
                ch+=1
    print(f"La cantidad de cupos otorgados para hoy {hoy} es: {ch} \n")

##### CAMIONES ARRIBADOS HISTORICAMENTE Y HOY #####
R = 0
RH = 0
def Arribados_hoy():
    t=os.path.getsize(AF_OP)
    AL_OP.seek(0)
    RegOp = oper()
    rh=0
    if t == 0:
        print("⚠ No han arribado camiones aun")
    else:
        while AL_OP.tell() < t:
            RegOp= pickle.load(AL_OP)
            if RegOp.est=="A" or RegOp.est=="C" or RegOp.est=="B" or RegOp.est=="R" or RegOp.est=="F":
                if RegOp.fecha == hoy:
                    rh+=1
    print(f"La cantidad de camiones arribados hoy {hoy} fue: {rh} ")

def Arribados():
    t=os.path.getsize(AF_OP)
    AL_OP.seek(0)
    RegOp = oper()
    r=0
    if t == 0:
        print("⚠ No han arribado camiones aun")
    else:
        while AL_OP.tell() < t:
            RegOp= pickle.load(AL_OP)
            if RegOp.est=="A" or RegOp.est=="C" or RegOp.est=="B" or RegOp.est=="R" or RegOp.est=="F":
                r+=1
    print(f"La cantidad total de camiones arribados fue: {r} ")

def reportes():
    flag=True
    while flag==True:
        os.system('cls')
        menu_Reportes()
        opcion=input( "\n → Ingrese la opción que desea usar, o 0 para volver al menú anterior: \n → " )
                
        if opcion == "1":
            os.system('cls')
            print(c.bold + "                            Cupos historicos otorgados " + c.resetear)
            print("                         __________________________________\n")
            Cupos_Otorgados()
            print(c.bold + "\n                         Cupos otorgados el dia de hoy " + c.resetear)
            print("                         __________________________________\n")
            Cupos_Otorgados_hoy()
            os.system('pause')
                      
        elif opcion == "2":
            os.system('cls')
            print(c.bold + "                            Cantidad total de camiones" + c.resetear)
            print("                         __________________________________\n")
            Arribados()
            print(c.bold + "\n                   Cantidad total de camiones el dia de hoy " + c.resetear)
            print("                         __________________________________\n")
            Arribados_hoy()
            os.system('pause')

        elif opcion == "3":
            os.system('pause')

        elif opcion == "4":
            os.system('pause')

        elif opcion == "5":
            os.system('pause')

        elif opcion == "6":
            os.system('cls')
            cantp=cant_prod()
            print(c.bold + "                            Patentes con menor descarga      " + c.resetear)
            print("                         __________________________________\n")
            for i in range(1,cantp+1):
                if busco_prod_cam(i):
                    posprod=buscaProducto_cod(i)
                    AL_PROD.seek(posprod)
                    rProd=pickle.load(AL_PROD)
                    nomprod=rProd.nom_prod.strip()
                    aaa=menor_patente(i)
                    if aaa!=-1:
                        print(f"La patente con menor descarga para {nomprod} es {aaa}\n")
            os.system('pause')
            

        elif opcion == "0":
            flag=False


################## PANTALLAS #####################

def menu_princ():
    print( "")
    print(c.bold + "                                     EL ACOPIO    " + c.resetear)
    print(c.bold + "                                   Menu Principal    " + c.resetear)
    print("                         __________________________________\n")
    print("                         ➤ 1 - Administraciones")
    print("                         ➤ 2 - Entrega de cupos")
    print("                         ➤ 3 - Recepcion")
    print("                         ➤ 4 - Registrar calidad")
    print("                         ➤ 5 - Registrar peso bruto")
    print("                         ➤ 6 - Archivos")
    print("                         ➤ 7 - Registrar tara")
    print("                         ➤ 8 - Reportes")
    print("                         ➤ 9 - Silos")
    print("                         ➤ 0 - Fin de programa")
    print("                         __________________________________")
    print("" )

def menu_01_administraciones():
    print( "")
    print(c.bold + "                                Menu Administraciones      " + c.resetear)
    print("                         __________________________________\n")
    print("                         ➤ A - Titulares")
    print("                         ➤ B - Productos")
    print("                         ➤ C - Rubros")
    print("                         ➤ D - Rubros por producto")
    print("                         ➤ E - Silos")
    print("                         ➤ F - Sucursales")
    print("                         ➤ G - Producto por titular")
    print("                         ➤ V - Volver al Menu Principal")
    print("                         __________________________________")
    print("" )

def menu_crud():
    print( "")
    print(c.bold + "                                 Menu de opciones    " + c.resetear)
    print("                         __________________________________\n")
    print("                         ➤ A - Alta")
    print("                         ➤ B - Baja")
    print("                         ➤ C - Consulta")
    print("                         ➤ M - Modificaciones")
    print("                         ➤ V - Volver al menu anterior")
    print("                         __________________________________")
    print("" )

def menu_crud_rubro():
    print( "")
    print(c.bold + "                                Menu alta de rubros          " + c.resetear)
    print("                         __________________________________\n")
    print("                         ➤ A - Alta")
    print("                         ➤ V - Volver al menu anterior")
    print("                         __________________________________")
    print("" )

def menu_crud_rxp():
    print( "")
    print(c.bold + "                          Menu alta de rubros por producto " + c.resetear)
    print("                         __________________________________\n")
    print("                         ➤ A - Alta")
    print("                         ➤ V - Volver al menu anterior")
    print("                         __________________________________")
    print("" )

def menu_crud_silos():
    print( "")
    print(c.bold + "                                 Menu alta de silos           " + c.resetear)
    print("                         __________________________________\n")
    print("                         ➤ A - Alta")
    print("                         ➤ V - Volver al menu anterior")
    print("                         __________________________________")
    print("" )

def menu_Archivos():
    print( "")
    print(c.bold + "                                 Menu de archivos" + c.resetear)
    print("                         __________________________________\n")
    print("                         ➤ 1 - Operaciones")
    print("                         ➤ 2 - Productos")
    print("                         ➤ 3 - Rubros")
    print("                         ➤ 4 - Rubros por productos")
    print("                         ➤ 5 - Silos")
    print("                         ➤ 6 - Patente menor")
    print("                         ➤ 7 - Alta provisoria")
    print("                         ➤ 0 - Volver al menu anterior")
    print("                         __________________________________")
    print("" )

def menu_Reportes():
    print( "")
    print(c.bold + "                                   Menu de reportes       " + c.resetear)
    print("                         __________________________________\n")
    print("                         ➤ 1 - Total de cupos otorgados")
    print("                         ➤ 2 - Total de camiones recibidos")
    print("                         ➤ 3 - Total de camiones por producto")
    print("                         ➤ 4 - Peso neto total por producto")
    print("                         ➤ 5 - Promedio de PN por camion")
    print("                         ➤ 6 - Patente con menor descarga")
    print("                         ➤ 0 - Volver al menu anterior")
    print("                         __________________________________\n")
    print("" )

def crud():
    flag=True
    while flag==True:
        
        menu_crud()
        opcion=input( "\n → Ingrese la opción que desea usar, o V para volver al menú anterior: \n → " )
            
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
        opcion=input( "\n → Ingrese la opción que desea usar, o V para volver al menú anterior: \n → " )
        
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
        opcion=input( "\n → Ingrese la opción que desea usar, o V para volver al menú anterior: \n → " )
        
        if opcion == "A" or opcion == "a":
            
            alta_rubros()
                              
        elif opcion == "V" or opcion == "v":
            flag=False

def crud_rxp():
    flag=True
    while flag==True:
        
        menu_crud_rxp()
        opcion=input( "\n → Ingrese la opción que desea usar, o V para volver al menú anterior: \n → " )
        
        if opcion == "A" or opcion == "a":
            
            alta_RxP()
                              
        elif opcion == "V" or opcion == "v":
            flag=False

def crud_silos():
    flag=True
    while flag==True:
        
        menu_crud_silos()
        opcion=input( "\n → Ingrese la opción que desea usar, o V para volver al menú anterior: \n → " )
        
        if opcion == "A" or opcion == "a":
            
            alta_silos()
                              
        elif opcion == "V" or opcion == "v":
            flag=False

def administraciones():
    flag=True
    while flag==True:
        os.system('cls')
        menu_01_administraciones()
        opcion=input( "\n → Ingrese de la A a la G según la opción que desea usar, o V para volver al menú anterior: \n → " )
        if opcion == "A" or opcion == "a":
            crud()
            
        elif opcion == "B" or opcion == "b":
            crud_productos()

        elif opcion == "C" or opcion == "c":
            crud_rubros()

        elif opcion == "D" or opcion == "d":
            crud_rxp()

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
    
    op=input("Ingrese un valor entre 1 y 9, ó 0 para finalizar → ")
    while validaRangoEntero(op, 0,9):
        op=input("Ingrese un valor entre 1 y 9, ó 0 para finalizar→ ")
  
    if op == "1":
        administraciones()
    elif op == "2":
        entrega_cupos()
    elif op == "3":
        recepcion()
    elif op == "4":
        registrar_calidad()
    elif op == "5":
        bruto()
    elif op == "6":
        archivos()
    elif op == "7":
        tara()
    elif op == "8":
        reportes()
    elif op == "9":
        silos()
    elif op =="0":
        flag=False
        AL_OP.close()
        AL_PROD.close()
        AL_RUBRO.close()
        AL_RUBROP.close()
        AL_SILOS.close()
        print(c.verde + 'Archivos cerrados correctamente' + c.resetear)

print("see you later, aligator...\n")

