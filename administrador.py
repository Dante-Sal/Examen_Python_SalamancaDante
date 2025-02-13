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

def registroGestionUsuarios(funcionalidad):
    if funcionalidad==1:
        print("\n1. Crear perfil")
        print("2. Ver perfiles")
        print("3. Actualizar perfil")
        print("4. Eliminar perfil")
        print("(Ingrese cualquier otro número). Salir del programa")
        opcCRUDuser=int(input("\nIngrese la opción a realizar: --- "))
        if opcCRUDuser==1:
            perfilNuevo={}
            perfilNuevo["id"]=int(input("\nIngrese el número de identificación del nuevo usuario: --- "))
            perfilNuevo["nombres"]=input("Ingrese el/los nombre/s del nuevo usuario: --- ")
            perfilNuevo["apellidos"]=input("Ingrese los apellidos del nuevo usuario: --- ")
            perfilNuevo["direccion"]=input("Ingrese la dirección del nuevo usuario: --- ")
            perfilNuevo["infoContacto"]={}
            perfilNuevo["infoContacto"]["tel"]=int(input("Ingrese el número de teléfono fijo del nuevo usuario: --- "))
            perfilNuevo["infoContacto"]["cel"]=int(input("Ingrese el número de teléfono celular del nuevo usuario: --- "))
            perfilNuevo["tiempo"]=0
            perfilNuevo["servicio"]=input("Ingrese el servicio adquirido por el nuevo usuario: --- ")
            perfilNuevo["frecuencia"]=0
            dic["usuarios"].append(perfilNuevo)
        elif opcCRUDuser==2:
            c=0
            for usuario in dic["usuarios"]:
                print(f"\nUsuario #{c+1}: ---")
                print(f"\nID: {usuario['id']} / Nombre: {usuario['nombres']} {usuario['apellidos']}")
                print(f"Dirección: {usuario['direccion']} / TEL: {usuario['infoContacto']['tel']} / CEL: {usuario['infoContacto']['cel']}")
                print(f"El usuario lleva {usuario['tiempo']} años con Movistar / Servicio adquirido por el usuario: {usuario['servicio']}")
                print(f"El usuario ha visitado la plataforma de Movistar {usuario['frecuencia']} veces")
                c+=1
        elif opcCRUDuser==3:
            ID=int(input("\nIngrese el número de identificación del usuario a editar: --- "))
            for usuario in dic["usuarios"]:
                if usuario["id"]==ID:
                    print("\n1. Editar el número de identificación")
                    print("2. Editar los nombres")
                    print("3. Editar los apellidos")
                    print("4. Editar la dirección")
                    print("5. Editar la información de contacto")
                    print("6. Editar el tiempo que el usuario lleva con Movistar")
                    print("7. Editar el servicio adquirido por el usuario")
                    print("(Ingrese cualquier otro número). Salir del programa")
                    opcEdit=int(input("\nIngrese la opción a realizar: --- "))
                    if opcEdit==1:
                        usuario["id"]=int(input("\nIngrese el nuevo número de identificación del usuario: --- "))
                    elif opcEdit==2:
                        usuario["nombres"]=input("Ingrese el/los nuevo/s nombre/s del usuario: --- ")
                    elif opcEdit==3:
                        usuario["apellidos"]=input("Ingrese los nuevos apellidos del usuario: --- ")
                    elif opcEdit==4:
                        usuario["direccion"]=input("Ingrese la nueva dirección del usuario: --- ")
                    elif opcEdit==5:
                        print("\n1. Editar el número de teléfono fijo")
                        print("2. Editar el número de teléfono celular")
                        print("(Ingrese cualquier otro número). Salir del programa")
                        opcInfoContacto=int(input("\nIngrese la opción a realizar: --- "))
                        if opcInfoContacto==1:
                            usuario["infoContacto"]["tel"]=int(input("Ingrese el nuevo número de teléfono fijo del usuario: --- "))
                        elif opcInfoContacto==2:
                            usuario["infoContacto"]["cel"]=int(input("Ingrese el nuevo número de teléfono celular del usuario: --- "))
                        else:
                            exit()
                    elif opcEdit==6:
                        usuario["tiempo"]=int(input("Ingrese el tiempo que el usuario lleva con Movistar actualizado: --- "))
                    elif opcEdit==7:
                        usuario["servicio"]=input("Ingrese el nuevo servicio adquirido por el usuario: --- ")
                    else:
                        exit()
        elif opcCRUDuser==4:
            ID=int(input("\nIngrese el número de identificación del usuario a eliminar de la base de datos (esta acción es PERMANENTE,\nsi desea retornar la base de datos a su estado original, tendrá que ingresar los datos del usuario eliminado nuevamente): --- "))
            for usuario in dic["usuarios"]:
                if usuario["id"]==ID:
                    print(f"\n¿Está seguro que quiere eliminar al usuario {usuario['nombres']} {usuario['apellidos']} de número de identificación {usuario['id']}?")
                    print(f"\n1. Sí, estoy seguro")
                    print(f"2. No, salir del programa")
                    opcVerificarEliminar=int(input("\nIngrese la opción a realizar: --- "))
                    if opcVerificarEliminar==1:
                        dic["usuarios"].remove(usuario)
                    else:
                        exit()
        else:
            exit()
    elif funcionalidad==2:
        print()
    guardarJSON(dic)