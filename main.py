import json
from administrador import registroGestionUsuarios,mostrarServicios
from usuario import bonificaciones

def abrirJSON():
    dicFinal={}
    with open("./bbdd.json","r") as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open("./bbdd.json","w") as outFile:
        json.dump(dic,outFile,indent=4,ensure_ascii=True)

dic={}
dic=abrirJSON()

opc=int(input("Bienvenido a la plataforma de Movistar!\n¿Cómo deseas ingresar? (1: Administrador / 2: Usuario / (Ingrese cualquier otro número): Salir de la plataforma): --- "))
if opc==1:
    print("\n1. Abrir menú CRUD (perfiles / usuarios)")
    print("2. Asignar categorías de usuarios")
    print("3. Ver servicios utilizados por cada usuario")
    print("(Ingrese cualquier otro número). Salir del programa")
    funcionalidad=int(input("\nIngrese la opción a realizar: --- "))
    if funcionalidad==1 or funcionalidad==2:
        registroGestionUsuarios(funcionalidad)
    elif funcionalidad==3:
        mostrarServicios()
    else:
        exit()
if opc==2:
    ID=int(input("\nIngrese su número de identificación: --- "))
    for usuario in dic["usuarios"]:
        if usuario["id"]==ID:
            print(f"\nBienvenido de nuevo, {usuario['nombres']} {usuario['apellidos']}!")
            usuario["ingresos"]+=1
            guardarJSON(dic)
            break
    else:
        print("Usuario inexistente... :(")
    bonificaciones(ID)
