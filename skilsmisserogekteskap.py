import csv
import matplotlib.pyplot as plt
import numpy as np


class Fil:
    def __init__(self, filnavn, filtype, overskrift):
        self.filnavn = filnavn
        self.filtype = filtype
        self.overskrift = overskrift
        self.data = []

        if filtype == "csv":
            with open(filnavn, encoding="utf-8") as fil:
                self.filinnhold = csv.reader(fil, delimiter=";")

                next(self.filinnhold)

                for rad in self.filinnhold:
                    self.data.append(rad)

                for i in range(0, len(self.data)):
                    self.data[i].pop(0)

                print(self.data)

                for variabel in self.data:
                    for i in range(0,len(variabel)):
                        if variabel[i] == "..":
                            variabel[i] = 0
                        else:
                            variabel[i] = int(variabel[i])

                self.aarstall = self.data[0]
                self.ekteskap = self.data[1]
                self.skillsmisse = self.data[2]

    def plotteGraf(self):
        fig, ax = plt.subplots(figsize=(10, 5))    # Angir dimensjoner for figure-objektet

        y = np.arange(len(self.aarstall)) #angir hvor mange årstall vi har

        ax.barh(y+0.2, self.ekteskap, height=0.4, label="Ekteskap")  # Lager stolpediagram ekteskap
        ax.barh(y-0.2, self.skillsmisse, height=0.4, label="Skillsmisse")  # Lager stolpediagram skillsmisse
        ax.set_yticks(y, self.aarstall)                       # Legger til akseverdier
        ax.legend()                                               # Legger til beskrivelse

        fig.subplots_adjust(left=0.1)  # Øker plassen på venstre side av diagrammet

        plt.title(self.overskrift) #Lager tittel

        ax.grid(axis="x")  # Legger til rutenett (bare vertikale linjer)
        plt.show()  


Skilsmisser = Fil("Skilsmisserogekteskap.csv", "csv", "Inngåtte ekteskap og skilsmisser fra 1902 til 2022")
Skilsmisser.plotteGraf()
