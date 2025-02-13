import json

def abrirJSON():
    dicFinal={}
    with open("./bbdd.json","r") as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open("./bbdd.json","w") as outFile:
        json.dump(outFile,dic)

dic={}
dic=abrirJSON()

