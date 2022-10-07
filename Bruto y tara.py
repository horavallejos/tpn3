def bruto():
    global AF_OP, AL_OP
    os.system('cls')
    print(" OPCION 5 - Registrar peso bruto ")
    print(" -----------------------------\n ")
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
            A= RegOp.est
            if A == "C":
                bru=input("Ingrese peso bruto: ")
                RegOp.pesob = bru
                RegOp.est = "B"
                AL_OP.seek(pat_e,0)
                pickle.dump(RegOp, AL_OP)
                AL_OP.flush()
                print("Su peso bruto ha sido registrado con exito")

            elif Busco_patente(pat)== pat_e and A == "R":
                print("Su camion se encuentra en estado de rechazado")
            elif Busco_patente(pat)== pat_e and A =="A":
                print("Su camion se encuentra en arribado, debe dirigirse a registrar su calidad")

            elif Busco_patente(pat) == pat_e and A == "P":
                print("Su camion se encuentra en pendientes")
        else:
            print("La patente ingresada no ha sido encontrada")
        rta= input("Desea ingresar otra patente? S-si   N-no: ").upper()
        while rta != "S" and rta != "N":
            rta = input("Por favor, solo S para Si o N para No:").upper()

def tara():
    global AF_OP, AL_OP
    os.system('cls')
    print(" OPCION 7 - Registrar tara ")
    print(" -----------------------------\n ")
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
            A= RegOp.est
            B= RegOp.pesob
            if A == "B":
                tara=input("Ingrese tara: ")
                while B < tara:
                    tara=input("Error. Su tara no puede ser superior a su peso bruto: ")
                RegOp.tara = tara
                RegOp.est = "F"
                AL_OP.seek(pat_e,0)
                pickle.dump(RegOp, AL_OP)
                AL_OP.flush()
                print("Su tara ha sido registrada con exito. Felicitaciones!!! Ha finalizado su proceso")

            elif Busco_patente(pat)== pat_e and A == "R":
                print("Su camion se encuentra en estado de rechazado")
            elif Busco_patente(pat)== pat_e and A =="A":
                print("Su camion se encuentra en arribado, debe dirigirse a registrar su calidad")
            elif Busco_patente(pat)== pat_e and A =="C":
                print("Su camion aun no ha registrado su peso bruto")
            elif Busco_patente(pat) == pat_e and A == "P":
                print("Su camion se encuentra en pendientes")
        else:
            print("La patente ingresada no ha sido encontrada")
        rta= input("Desea ingresar otra patente? S-si   N-no: ").upper()
        while rta != "S" and rta != "N":
            rta = input("Por favor, solo S para Si o N para No:").upper()

def Busco_patente(pat):
    global AF_OP, AL_OP
    t = os.path.getsize(AF_OP)
    AL_OP.seek(0)
    while AL_OP.tell()<t:
        pat_e = AL_OP.tell()
        RegOp = pickle.load(AL_OP)
        if RegOp.pat.strip() == pat:
            return pat_e
    return -1