import matplotlib.pyplot as plt
import json
import csv


class Fil:
    def __init__(self, filnavn, filtype, overskrift):
        self.filnavn = filnavn
        self.filtype = filtype
        self.overskrift = overskrift
        self.aarstall = []
        self.utvikling = []

        if filtype == "json":
            with open(self.filnavn, encoding="utf-8-sig") as fil:
                data = json.load(fil)

                self.aarstallData = data["dataset"]["dimension"]["Tid"]["category"]["label"]
                self.aarstall = list(self.aarstallData.values())
                # gjøres om til tall for å kunne endre de senere i grafen
                for i in range(0, len(self.aarstall)):
                    self.aarstall[i] = int(self.aarstall[i])

                self.gjennomsnittutvikling = data["dataset"]["value"]

                self.label = data["dataset"]["dimension"]["EkteskStatus"]["category"]["label"]
                self.label = list(self.label.values())

        elif filtype == "csv":
            with open(self.filnavn, encoding="utf-8-sig") as fil:
                filinnhold = csv.reader(fil, delimiter=";")

                overskrifter = next(filinnhold)
                next(filinnhold)
                next(filinnhold)
                print(overskrifter)

                for rad in filinnhold:
                    print(rad)
                    self.aarstall.append(int(rad[0])) #x-akse
                    self.utvikling.append(int(rad[1])) #y-akse

    def PlassereData(self):
        self.utvikling = []

        for i in range(0, len(self.gjennomsnittutvikling), 42):
            self.utvikling.append(self.gjennomsnittutvikling[i:i+42])

    def skriveLister(self):
        print(self.aarstall)
        print(self.label)
        print(self.utvikling)

    def plotteGrafer(self):
        if self.filtype == "json":
            for i in range(0, 5):
                plt.plot(self.aarstall, self.utvikling[i], label=self.label[i])
        elif self.filtype == "csv":
            plt.plot(self.aarstall, self.utvikling)  # Lager stolpediagrammet


    def pynteGrafer(self):
        plt.ylim(0, 5500000)
        plt.xlim(1769, 2022)
        plt.xlabel("")
        plt.ylabel("")
        plt.title(self.overskrift)
        plt.grid()
        plt.legend()
        plt.show()

"""
sivilstand = Fil("Sivilstand.json", "json", "Sivilstand fra 1769 til i dag")
sivilstand.PlassereData()
# sivilstand.skriveLister()
sivilstand.plotteGrafer()
sivilstand.pynteGrafer()
"""

befolkning = Fil("Befolkning.csv","csv","Befolkning i Norge per 1. januar 1769-2022")
befolkning.plotteGrafer()
befolkning.pynteGrafer()

