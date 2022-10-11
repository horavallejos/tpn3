import os
import os.path
import pickle
import re

class rubros:
    def __init__(self):
        self.cod=0
        self.nom=""

def format(reg):
    reg.cod = str(reg.cod)
    reg.cod = reg.cod.ljust(2)
    reg.nom = reg.nom.ljust(10)


def crear():
    reg=rubros()
    reg.cod=input("Ingrese un codigo -> ")
    reg.nom=input("Ingrese un nombre -> ")
    AL_RUBRO.seek(0,2)
    format(reg)
    pickle.dump(reg,AL_RUBRO)
    AL_RUBRO.flush()
    print("Creado")
    os.system('pause')


def mostrar():
    t=os.path.getsize(AF_RUBRO)
    AL_RUBRO.seek(0)
    while AL_RUBRO.tell()<t:
        reg=pickle.load(AL_RUBRO)
        print(f"codigo= {reg.cod} - Nombre= {reg.nom} ")

def BuscaDico(Cod):
    global AF_RUBRO, AL_RUBRO
    rRxP = rubros()
    t = os.path.getsize(AF_RUBRO)
    if t>0:
        AL_RUBRO.seek (0,0)
        rRxP = pickle.load(AL_RUBRO)
        tamReg = AL_RUBRO.tell()
        cantReg = int(os.path.getsize(AF_RUBRO) / tamReg)
        inferior = 0
        superior = cantReg-1
        medio = inferior + superior // 2
        AL_RUBRO.seek(medio*tamReg, 0)
        rRxP= pickle.load(AL_RUBRO)
        Cod=int(Cod)
        while int(rRxP.cod)!= Cod and (inferior < superior):
            if int(Cod) < int(rRxP.cod):
                superior = medio - 1
            else:
                inferior = medio + 1
            medio = (inferior + superior) //2
            AL_RUBRO.seek(medio*tamReg, 0)
            rRxP= pickle.load(AL_RUBRO)
        if int(rRxP.cod) == Cod:
            return medio*tamReg
        else:
            return -1
    else:
        print('-----------------')
        print("Archivo sin datos")
        print('-----------------')
        input()
        return -1 

AF_RUBRO = "D:\\RUBRO\\RUBRO.DAT"

if not os.path.exists('D:\\RUBRO'):
    os.makedirs('D:\\RUBRO')

if not os.path.exists(AF_RUBRO):   
    AL_RUBRO = open(AF_RUBRO, "w+b")   
else:
    AL_RUBRO = open(AF_RUBRO, "r+b")


rta='S'
while rta=='S':
    registro=input("Ingresar una opcion 1registro o 2mostrar 3 buscar 4 salir")

    if registro=='1':
        os.system('cls')
        crear()
        

    elif registro=='2':
        os.system('cls')
        mostrar()
        os.system('pause')

    elif registro=='3':
        cod=input("Ingrese un codigo -> ")
        a=BuscaDico(cod)
        print("trae= ",a)
        os.system('pause')
        AL_RUBRO.seek(a)
        reg=pickle.load(AL_RUBRO)
        nombre=reg.nom
        print(nombre)
        os.system('pause')

    elif registro=='4':
        rta='N'
    
    
