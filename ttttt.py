hoy=fecha_hoy() # VARIABLE GLOBAL PARA FECHA DE HOY

def Busco_patente(pat):
    global AF_OP, AL_OP
    t = os.path.getsize(AF_OP)
    AL_OP.seek(0)
    RegOp=oper()
    ban=False
    while AL_OP.tell()<t and ban== False:
        pat_e = AL_OP.tell()
        RegOp = pickle.load(AL_OP)
        if RegOp.pat.strip() == pat and RegOp.fecha == hoy and RegOp.est == "P":
            return pat_e
        elif RegOp.pat.strip() == pat and RegOp.fecha == hoy and RegOp.est == "A":
            return "2"
        elif RegOp.pat.strip() == pat and RegOp.fecha == hoy and RegOp.est != "P":
            return "1"
        elif RegOp.pat.strip() == pat and RegOp.fecha != hoy :
            if RegOp.fecha > hoy:
                A = RegOp.fecha
                return A 
    return "3"

def recepcion():
    global AF_OP, AL_OP
    os.system('cls')
    print(" OPCION 3 - Recepcion ")
    print(" -----------------------------\n ")
    t = os.path.getsize(AF_OP)
    if t==0:
        print("NO HAY NADA EN CUPOS")
    else:
        rta='S'
        while rta=='S':
            os.system('cls')
            pat=input("Ingrese patente: ")
            while len(pat)<6 or len(pat)>7:
                pat=input("Error. Ingrese una patente valida: ")
            pat=pat.upper
            RegOp= oper()
            if Busco_patente(pat) == pat_e:
                pat_e = Busco_patente(pat)
                AL_OP.seek(pat_e,0)
                RegOp = pickle.load(AL_OP)
                RegOp.est = "A"
                AL_OP.seek(pat_e,0)
                pickle.dump(RegOp, AL_OP)
                AL_OP.flush()
                print("El estado de su camion ha cambiado a arribado")

            elif Busco_patente(pat)== "2":
                print("Su camion ya se encuentra en estado de arribado")
                
            elif Busco_patente(pat)== "3":
                print("La patente ingresada no tiene cupo")

            elif Busco_patente(pat) == A:
                print("Su cupo está asignado para la fecha:",A)
            
            elif Busco_patente(pat) == "1":
                print("El camion ingresado no se encuentra en pendientes")
            
            rta= input("Desea ingresar otra patente? S-si   N-no: ").upper()
            while rta != "S" and rta != "N":
                rta = input("Por favor, solo S para Si o N para No:").upper()