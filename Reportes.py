def tara():
    global AF_OP, AL_OP, AL_PROD, AF_PROD
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
        RegProd= prod()
#        RegOp= oper()
        if Busco_patente(pat) != -1:
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
                # AL_PROD.seek(RegOp.cod_prod,0)
                # RegProd = pickle.load(AL_PROD)
                # if RegProd.cod == "A":
                #     RegProd.cont_cam = RegProd.cont_cam + 1
                #     RegProd.acum_cam = RegProd.acum_cam + tara
                #     RegProd.prom = RegProd.acum_cam // RegProd.cont_cam 
                # AL_PROD.seek(RegOp.cod_prod,0)
                # pickle.dump(RegProd, AL_PROD)
                # Al_PROD.flush()
                AL_OP.seek(pat_e,0)
                pickle.dump(RegOp, AL_OP)
                AL_OP.flush()
                print("Su tara ha sido registrada con exito. Felicitaciones!!! Ha finalizado su proceso")

            elif Busco_patente(pat)!= -1 and A == "R":
                print("Su camion se encuentra en estado de rechazado")
            elif Busco_patente(pat)!= -1 and A =="A":
                print("Su camion se encuentra en arribado, debe dirigirse a registrar su calidad")
            elif Busco_patente(pat)!= -1 and A =="C":
                print("Su camion aun no ha registrado su peso bruto")
            elif Busco_patente(pat) != -1 and A == "P":
                print("Su camion se encuentra en pendientes")
        else:
            print("La patente ingresada no ha sido encontrada")
        rta= input("Desea ingresar otra patente? S-si   N-no: ").upper()
        while rta != "S" and rta != "N":
            rta = input("Por favor, solo S para Si o N para No:").upper()

###### ALTERNATIVA ###########
def tara():
    global AF_OP, AL_OP, AL_PROD, AF_PROD
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
        RegProd= prod()
#        RegOp= oper()
        if Busco_patente(pat) != -1:
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
                #buscaProducto(RegOp.cod_prod)
                # AL_PROD.seek(pos,0)
                # RegProd = pickle.load(AL_PROD)
                # if RegProd.cod == "A":
                #     RegProd.cont_cam = RegProd.cont_cam + 1
                #     RegProd.acum_cam = RegProd.acum_cam + tara
                #     RegProd.prom = RegProd.acum_cam // RegProd.cont_cam 
                # AL_PROD.seek(RegOp.cod_prod,0)
                # pickle.dump(RegProd, AL_PROD)
                # Al_PROD.flush()
                AL_OP.seek(pat_e,0)
                pickle.dump(RegOp, AL_OP)
                AL_OP.flush()
                print("Su tara ha sido registrada con exito. Felicitaciones!!! Ha finalizado su proceso")

            elif Busco_patente(pat)!= -1 and A == "R":
                print("Su camion se encuentra en estado de rechazado")
            elif Busco_patente(pat)!= -1 and A =="A":
                print("Su camion se encuentra en arribado, debe dirigirse a registrar su calidad")
            elif Busco_patente(pat)!= -1 and A =="C":
                print("Su camion aun no ha registrado su peso bruto")
            elif Busco_patente(pat) != -1 and A == "P":
                print("Su camion se encuentra en pendientes")
        else:
            print("La patente ingresada no ha sido encontrada")
        rta= input("Desea ingresar otra patente? S-si   N-no: ").upper()
        while rta != "S" and rta != "N":
            rta = input("Por favor, solo S para Si o N para No:").upper()