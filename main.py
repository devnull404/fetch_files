import random
import os

def createFiles():
    reg = ["ngh", "green", "yellow", "red"]
    irr = [reg[int(random.random()*4)]+"_"+str(int(random.random()*100))+"_"+str(int(random.random()*100))+"_"+str(int(random.random()*100)) for i in range(300)]
    for name in irr:
        os.system("touch " + name + ".csv")
    return irr

def renameFiles():
    files = os.listdir()
    files = [file for file in files if ".csv" in file]
    names = {}
    for name in files:
        names.setdefault(name[:name.find("_")], 0)
        names[name[:name.find("_")]] += 1
        aux = name[:name.find("_")]
        os.rename(name, aux+str(names[aux])+".csv")


renameFiles()