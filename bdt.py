import csv
import os
import json
import pprint

class BigDataTools():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def saveJson(self, targetFile, variable):
        if ".json" not in targetFile:
            targetFile += ".json"
        with open(targetFile, "w+") as fp:
            json.dumps(variable, fp)

    def loadCSV(self, fileName):
        with open(fileName, 'r') as fp:
            csvFile = csv.reader(fp)
            for row in csvFile:
                aux = row
                break
        return aux


    def dsinfo(self):
        csvPaths =  ["./assets/tlc_0.2perc/" + file for file in os.listdir("./assets/tlc_0.2perc/")]
        aux = {}
        for file in csvPaths:
            aux.setdefault(file[:file.find("_")], [])
            aux[file[:file.find("_")]].append(file)
        return aux

    def getHeaders(self, opt):
        return self.loadCSV(self.dsinfo()[opt])