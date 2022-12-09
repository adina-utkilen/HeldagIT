import matplotlib.pyplot as plt
import json
import csv


class Fil:
    def __init__(self, csvfil, jsonfil, overskrift):
        self.csvfil = csvfil
        self.jsonfil = jsonfil
        self.overskrift = overskrift
        self.aar = []
        self.befolkning = []

        
        with open(self.jsonfil, encoding="utf-8-sig") as fil:
            data = json.load(fil)

            self.aarstallData = data["dataset"]["dimension"]["Tid"]["category"]["label"]
            self.aarstall = list(self.aarstallData.values())
                # gjøres om til tall for å kunne endre de senere i grafen
            for i in range(0, len(self.aarstall)):
                self.aarstall[i] = int(self.aarstall[i])

            self.gjennomsnittutvikling = data["dataset"]["value"]

            self.label = data["dataset"]["dimension"]["EkteskStatus"]["category"]["label"]
            self.label = list(self.label.values())

        
        with open(self.csvfil, encoding="utf-8-sig") as fil:
            filinnhold = csv.reader(fil, delimiter=";")

            overskrifter = next(filinnhold)
            next(filinnhold)
            next(filinnhold)
            print(overskrifter)

            for rad in filinnhold:
                #print(rad)
                self.aar.append(int(rad[0])) #x-akse
                self.befolkning.append(int(rad[1])) #y-akse
            print(self.befolkning)
            print(len(self.befolkning))
            print(len(self.aarstall))
            

    def PlassereData(self):
        self.utvikling = []

        for i in range(0, len(self.gjennomsnittutvikling), 42):
            self.utvikling.append(self.gjennomsnittutvikling[i:i+42])
        print((self.utvikling[1]))

    def skriveLister(self):
        print(self.aarstall)
        print(self.label)
        print(self.utvikling)

    def plotteGrafer(self):
        plt.plot(self.aar, self.befolkning,label="Befolkning") 
        for i in range(0, 5):
            plt.plot(self.aarstall, self.utvikling[i], label=self.label[i])
            


    def pynteGrafer(self):
        plt.ylim(0, 5500000)
        plt.xlim(1769, 2022)
        plt.xlabel("")
        plt.ylabel("")
        plt.title(self.overskrift)
        plt.grid()
        plt.legend()
        plt.show()


graf = Fil("Befolkning.csv","Sivilstand.json","Utvikling i Norge fra 1769-2022")
graf.PlassereData()
graf.plotteGrafer()
graf.pynteGrafer()
