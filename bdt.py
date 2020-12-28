import csv
import os
import json
import pprint

class tools(object):
    def __init__(self):
        self.ABS_PATH_WINDOWS = "./assets/tlc_0.2perc/"
        self.REL_PATD_UNIX = "./assets/tlc_0.2perc/"

    def saveJson(self, targetFile, variable):
        if ".json" not in targetFile:
            targetFile += ".json"
        with open(targetFile, "w+") as fp:
            json.dump(variable, fp)

    def loadJson(self):
        jfile = [file for file in os.listdir() if ".json" in file]
        index = list(range(len(jfile)))
        print("Select a file to return as a variable: ")
        for i in range(len(jfile)):
            print(str(index[i]+1) + " - " + jfile[i])
        flag = True
        while flag:
            aux = input(">>> ? ")
            if (int(aux)-1) in index:
                flag = False
        with open(jfile[int(aux)-1], "r") as fp:
            var = json.load(fp)
        
        return var

    def loadCSV(self, fileName):
        count = 0
        with open(fileName, 'r') as fp:
            csvFile = csv.reader(fp)
            for row in csvFile:
                aux = row
                break
            count = sum(1 for row in csvFile)
        return aux, count


    def dsinfo(self):
        csvPaths =  [self.ABS_PATH_WINDOWS + file for file in os.listdir(self.ABS_PATH_WINDOWS)]
        aux = {}
        for file in csvPaths:
            file = file[21:]
            if file[0] != ".":
                aux.setdefault(file[:file.find("_")], [])
                aux[file[:file.find("_")]].append(self.ABS_PATH_WINDOWS + file)
        return aux

    def getHeaders(self, fileStructure):
        for file in fileStructure:
            print(self.loadCSV(file))
        return 1

    def getStats(self):
        aux = {}
        datasetinfo = self.dsinfo()
        count = 0
        i = 0
        for category in datasetinfo.keys():
            aux.setdefault(category, [])
            for elem in datasetinfo[category]:
                aux[category].append({})
                aux[category][-1][elem] = []
                out = self.loadCSV(elem)
                aux[category][-1][elem].append(out[0])
                aux[category][-1][elem].append(out[1])
                count += out[1]
                i += 1
            count = count/i
            aux[category].append(count)
            count = 0
            i = 0
        return aux

        def patternIDentification(self, structuredData):
            