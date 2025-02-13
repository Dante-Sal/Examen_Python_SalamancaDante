import json
from administrador import registroGestionUsuarios

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

opc=int(input("Bienvenido a la plataforma de Movistar!\n¿Cómo deseas ingresar? (1: Administrador / 2: Usuario): --- "))
if opc==1:
    print("\n1. Abrir menú CRUD (perfiles / usuarios)")
    print("2. Asignar categorías de usuarios")
    print("(Ingrese cualquier otro número). Salir del programa")
    funcionalidad=int(input("\nIngrese la opción a realizar: --- "))
    registroGestionUsuarios(funcionalidad)
if opc==2:
    print()