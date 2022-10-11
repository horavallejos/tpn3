def BuscaDico (Cod):
	global AF_RUBRO, AL_RUBRO
	RegRub = Rubros()
	t = os.path.getsize(AL_RUB)
	if t>0:
		AL_RUBRO.seek (0,0)
		RegRub = pickle.load(AL_RUBRO)
		tamReg = AL_RUBRO.tell()
		cantReg = int(os.path.getsize(AF_RUBRO) / tamReg)
		inferior = 0
		superior = cantReg-1
		medio = inferior + superior // 2
		AL_RUBRO.seek(medio*tamReg, 0)
		RegRub= pickle.load(AL_RUBRO)
		while int(RegRub.cod)!= Cod and (inferior < superior):
			if int(Cod) < int(RegRub.cod):
				superior = medio - 1
			else:
				inferior = medio + 1
			medio = (inferior + superior) //2
			AL_RUBRO.seek(medio*tamReg, 0)
			RegRub= pickle.load(AL_RUBRO)
		if int(RegRub.cod) == Cod:
			return medio*tamReg
		else:
			return -1
	else:
    		print('-----------------')
    		print("Archivo sin datos")
    		print('-----------------')
    		input()
    		return -1