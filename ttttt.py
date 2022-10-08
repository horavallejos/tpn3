def entrega_cupos():
    global AF_OP, AL_OP
    rOp=oper()
    rOp.pat=validarPatente()
    e=Busco_patente(rOp.pat)
    if e!=-1:
        print("Patente existente. CHAU no'vemo' ")
        os.system('pause')
    else:
        canp=cant_prod()
        mostrar_productos_all()
        rOp.cod_prod=input("Ingrese el código del producto -> ")
        while rOp.cod_prod<"1" or rOp.cod_prod>str(canp):
            rOp.cod_prod=input("Ingrese el código del producto -> ")
        rOp.fecha=validarFecha()
        rOp.est="P"
        AL_OP.seek(0,2)
        formatOp(rOp)
        pickle.dump(rOp,AL_OP)
        AL_OP.flush()
        print(f"El CUPO para {rOp.pat} fue registrado con éxito... \n ")
        os.system('pause')