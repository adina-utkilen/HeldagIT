import matplotlib.pyplot as plt
import json


class Fil:
    def __init__(self, filnavn, filtype, overskrift):
        self.filnavn = filnavn
        self.filtype = filtype
        self.overskrift = overskrift

        if filtype == "json":
            with open(self.filnavn, encoding="utf-8-sig") as fil:
                data = json.load(fil)

                self.aarstallData = data["dataset"]["dimension"]["Tid"]["category"]["label"]
                self.aarstall = list(self.aarstallData.values())
                # gjøres om til tall for å kunne endre de senere i grafen
                for i in range(0, len(self.aarstall)):
                    self.aarstall[i] = int(self.aarstall[i])

                self.gjennomsnittutvikling = data["dataset"]["value"]

    def PlassereData(self):
        self.utvikling1 = []
        self.utvikling2 = []
        self.utvikling3 = []
        self.utvikling4 = []
        self.utvikling5 = []

        for i in range(0, 42):
            self.utvikling1.append(self.gjennomsnittutvikling[i])

        for i in range(42, 42+42):
            self.utvikling2.append(self.gjennomsnittutvikling[i])

        for i in range(84, 84+42):
            self.utvikling3.append(self.gjennomsnittutvikling[i])

        for i in range(126, 126+42):
            self.utvikling4.append(self.gjennomsnittutvikling[i])

        for i in range(168, len(self.gjennomsnittutvikling)):
            self.utvikling5.append(self.gjennomsnittutvikling[i])

    def skriveLister(self):
        print(self.aarstall)
        print(self.gjennomsnittutvikling)

    def plotteGrafer(self):
        plt.plot(self.aarstall, self.utvikling1)
        plt.plot(self.aarstall, self.utvikling2)
        plt.plot(self.aarstall, self.utvikling3)
        plt.plot(self.aarstall, self.utvikling4)
        plt.plot(self.aarstall, self.utvikling5)

    def pynteGrafer(self):
        plt.ylim(0, 4000000)
        plt.xlim(1769, 2022)
        plt.xlabel("")
        plt.ylabel("")
        plt.title(self.overskrift)
        plt.grid()
        plt.show()


sivilstand = Fil("Sivilstand.json", "json", "Sivilstand fra 1769 til i dag")
sivilstand.PlassereData()
# sivilstand.skriveLister()
sivilstand.plotteGrafer()
sivilstand.pynteGrafer()
