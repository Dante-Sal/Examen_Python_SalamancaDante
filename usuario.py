import json

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

def bonificaciones(ID):
    for usuario in dic["usuarios"]:
        if usuario["id"]==ID and usuario["tiempo"]>6:
            aceptarBono=int(input(f"Haz recibido un bono especial en tu servicio de {usuario['servicio'].lower()}!\nAceptar? (1: Sí / 2: No / (Ingrese cualquier otro número): Salir de la plataforma): --- "))
            if aceptarBono==1:
                print("Bono aceptado con éxito! :)")
            elif aceptarBono==2:
                print("Bono rechazado...")
            else:
                exit()