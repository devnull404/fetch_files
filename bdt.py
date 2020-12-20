import csv
import os
import json
import pprint

class tools():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def saveJson(self, targetFile, variable):
        if ".json" not in targetFile:
            targetFile += ".json"
        with open(targetFile, "w+") as fp:
            json.dump(variable, fp)

    def loadCSV(self, fileName):
        count = 0
        with open(fileName, 'r') as fp:
            csvFile = csv.reader(fp)
            for row in csvFile:
                aux = row
                break
            for row in csvFile:
                count += 1
        return aux, count


    def dsinfo(self):
        csvPaths =  ["./assets/tlc_0.2perc/" + file for file in os.listdir("./assets/tlc_0.2perc/")]
        aux = {}
        for file in csvPaths:
            file = file[21:]
            if file[0] != ".":
                aux.setdefault(file[:file.find("_")], [])
                aux[file[:file.find("_")]].append("./assets/tlc_0.2perc/" + file)
        return aux

    def getHeaders(self, fileStructure):
        for file in fileStructure:
            print(self.loadCSV(file))
        return 1

    def getStats(self):
        datasetinfo = self.dsinfo()
        aux = []
        i = 0
        for subset in datasetinfo.keys():
            aux.append([])
            for elem in datasetinfo[subset]:
                aux[i].append(self.loadCSV(elem))
            i += 1
        return aux