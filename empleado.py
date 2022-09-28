from asyncore import read
import os
import os.path
import pickle
from turtle import update

class Empleado:
    def __init__(self) -> None:
        self.legajo = 0
        self.nomyape = ""
        self.sueldo = 0.00
        self.estado = "A" # A - Activo B - Baja

# si no existe, creo directorio
if not os.path.exists("files"):
    os.makedirs("files")

afEmpleados = "files\\empleados.dat"

# si no existe, creo archivo
if not os.path.exists(afEmpleados):
    alEmpleados = open(afEmpleados, "w+b")
else:
    alEmpleados = open(afEmpleados, "r+b")

def mostrarMenu():
    os.system("cls")
    print("ABM DE EMPLEADOS")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")


# inicio Menú principal
opc = -1
while opc != 0:
    mostrarMenu()
    opc = input("Ingrese una opción [0-4]: ")
    while is_integuer(opc,0,5):
        opc = input("Incorrecto. Ingrese una opción de [0-4]: ")
    opc = int(opc)
    if opc == 1:
        altaEmpleado()
    elif opc == 2:
        modificaEmpleado()
    elif opc == 3:
        bajaEmpleado()
    elif opc == 4:
        listarEmpleadosActivos()
    else:
        print("\n\nGracias por la visita")
        alEmpleados.close()
