import os
import os.path
import pickle


class Empleado:
    def __init__(self) -> None:
        self.legajo = 0
        self.nomyape = ""
        self.sueldo = 0.00
        self.estado = "A" # A - Activo B - Baja


def validaRangoEnteros(nro, desde, hasta):
    try:
        int(nro)
        if int(nro) >= desde and int(nro) <= hasta:
            return False
        else:
            return True
    except:
        return True

def validaRangoReales(nro, desde, hasta):
    try:
        float(nro)
        if float(nro) >= desde and float(nro) <= hasta:
            return False
        else:
            return True
    except:
        return True

def buscarEmpleado(leg):
    t = os.path.getsize(afEmpleados)
    alEmpleados.seek(0)
    while alEmpleados.tell() < t :
        pos = alEmpleados.tell()
        vrTemp = pickle.load(alEmpleados)
        if int(vrTemp.legajo) == leg:
            return pos
    return -1

def altaEmpleado():
    os.system('cls')
    print(" OPCION 1 - Alta de Empleados ")
    print(" -----------------------------\n ")
    leg = input("Ingrese el legajo del empleado a dar de alta, entre 1 y 99999: ")
    while validaRangoEnteros(leg, 1, 99999):
        leg = input("Incorrecto - Entre 1 y 99999: ")
    leg = int(leg)
    emp = Empleado()
    if buscarEmpleado(leg) == -1: 
        emp.legajo=leg
        emp.nomyape=input("Nombre y Apellido: ")
        emp.sueldo=float(input("Sueldo: "))
        formatearEmpleado(emp)
        pickle.dump(emp,alEmpleados)
        alEmpleados.flush()
        print("Alta de empleado Exitosa\n")
    else:
        print("Ya existe un empleado con ese legajo ", leg, "\n")
    os.system('pause')

def mostrarEmpleado(emp):
    print("Legajo: ",emp.legajo)
    print("Nombre y Apellido: ", emp.nomyape)
    print("Sueldo: ", emp.sueldo)
    print("Estado: ", emp.estado)

def formatearEmpleado(regEmp):
    regEmp.legajo = str(regEmp.legajo)
    regEmp.legajo = regEmp.legajo.ljust(10)
    regEmp.nomyape = regEmp.nomyape.ljust(40)
    regEmp.sueldo = str(regEmp.sueldo)
    regEmp.sueldo = regEmp.sueldo.ljust(10)
    ## El estado no es necesario formatear ya que es de 
    ## asignación interna y siempre va a ser A o B.

def modificaEmpleado():
    os.system('cls')
    print(" OPCION 2 - Modificar Empleado ")
    print(" -----------------------------\n ")
    t=os.path.getsize(afEmpleados)
    if t==0:
        print("No hay empleados cargados")
        os.system('pause')
    else:
        leg = input("Ingrese el legajo del empleado a Modificar, entre 1 y 99999 [0 para volver] : ")
        while validaRangoEnteros(leg, 0, 99999):
            leg = input("Incorrecto - entre 1 y 99999 [0 para volver] : ")
        leg = int(leg)
        if leg != 0:
            pos = buscarEmpleado(leg)
            if pos == -1:
                print("El legajo del empleado no existe")
            else:
                emp = Empleado()
                alEmpleados.seek(pos,0)
                emp=pickle.load(alEmpleados)
                if emp.estado == "B":
                    print("El empleado está dado de baja y no se puede modificar")
                else:
                    print("Empleado a modificar: ")
                    mostrarEmpleado(emp)
                    print("\n Solo se podrán modificar el nombre y apellido y su sueldo.\n")
                    emp.nomyape = input("Nuevo Nombre y Apellido [hasta 40 carcateres]: ")
                    while len(emp.nomyape)<1 or len(emp.nomyape)>40:
                        emp.nomyape = input("Ingrese un valor correcto [hasta 40 carcateres]: ")
                    emp.sueldo = input("Nuevo sueldo [entre 100000 y 300000]: ")
                    while validaRangoReales(emp.sueldo, 100000, 300000):
                        emp.sueldo = input("Incorrecto: sueldo [entre 100000 y 300000]: ")
                    emp.sueldo=float(emp.sueldo)
                    rpta=input("Confirma? Si o No")
                    while rpta.lower() != "si" and rpta.lower() != "no":
                        rpta=input("Incorrecto. Confirma? Si o No")
                    if rpta.lower() == "si":
                        alEmpleados.seek(pos)
                        formatearEmpleado(emp)
                        pickle.dump(emp,alEmpleados)
                        alEmpleados.flush()
                        print("Modificación exitosa")
                        print("Los datos actualizados del empleado son: ")
                        mostrarEmpleado(emp)
            os.system('pause')


def bajaEmpleado():
    os.system('cls')
    print(" OPCION 3 - Baja Empleado ")
    print(" -----------------------------\n ")
    t=os.path.getsize(afEmpleados)
    if t==0:
        print("No hay empleados cargados")
        os.system('pause')
    else:
        leg = input("Ingrese el legajo del empleado a dar de BAJA, entre 1 y 99999 [0 para volver] : ")
        while validaRangoEnteros(leg, 0, 99999):
            leg = input("Incorrecto - entre 1 y 99999 [0 para volver] : ")
        leg = int(leg)
        if leg != 0:
            pos = buscarEmpleado(leg)
            if pos == -1:
                print("El legajo del empleado no existe")
            else:
                emp = Empleado()
                alEmpleados.seek(pos,0)
                emp=pickle.load(alEmpleados)
                if emp.estado == "B":
                    print("El empleado está dado de baja y no se puede modificar")
                else:
                    print("Empleado a modificar: ")
                    mostrarEmpleado(emp)
                    rpta=input("Está seguro que quiere darlo de baja? Si o No")
                    while rpta.lower() != "si" and rpta.lower() != "no":
                        rpta=input("Incorrecto. Confirma? Si o No")
                    if rpta.lower() == "si":
                        alEmpleados.seek(pos)
                        emp.estado="B"
                        pickle.dump(emp,alEmpleados)
                        alEmpleados.flush()
                        print("BAJA exitosa")
                        print("Los datos actualizados del empleado son: ")
                        mostrarEmpleado(emp)
            os.system('pause')


# si no existe, creo directorio
if not os.path.exists("tpn3\\files"):
    os.makedirs("tpn3\\files")

afEmpleados = "tpn3\\files\\empleados.dat"

# si no existe, creo archivo
if not os.path.exists(afEmpleados):
    alEmpleados = open(afEmpleados, "w+b")
else:
    alEmpleados = open(afEmpleados, "r+b")

def mostrarMenu():
    os.system("cls")
    print("ABM DE EMPLEADOS")
    print("-------------------")
    print(" 1. Alta de Empleados ")
    print(" 2. Modificación de Empleado ")
    print(" 3. Baja de Empleado ")
    print(" 4. Listado de Empleados ")
    print(" 0. Salir ")


# inicio Menú principal
opc = -1
while opc != 0:
    mostrarMenu()
    opc = input("Ingrese una opción [0-4]: ")
    while validaRangoEnteros(opc,0,4):
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
