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

                overskrifter = next(self.filinnhold)
              #  print(str(overskrifter))

                for rad in self.filinnhold:
                    self.data.append(rad)

                for i in range(0, len(self.data)):
                    self.data[i].pop(0)

                self.aarstall = self.data[0]
                self.ekteskap = self.data[1]
                self.skillsmisse = self.data[2]

                for i in range(0, len(self.aarstall)):
                    self.aarstall[i] = int(self.aarstall[i])

                for i in range(0, len(self.ekteskap)):
                    self.ekteskap[i] = int(self.ekteskap[i])

                for i in range(0, len(self.skillsmisse)):
                    self.skillsmisse[i] = int(self.skillsmisse[i])

    def plotteGraf(self):
        fig, ax = plt.subplots(figsize=(10, 5))
        y = np.arange(10)
        # Lager stolpediagram jenter
        ax.barh(y+0.2, self.ekteskap, height=0.4, label="Jenter")
        # Lager stolpediagram gutter
        ax.barh(y-0.2, self.skillsmisse, height=0.4, label="Gutter")
        # Legger til akseverdier
        ax.set_yticks(y, self.aarstall)
        ax.legend()                                               # Legger til beskrivelse

        # Øker plassen på venstre side av diagrammet
        fig.subplots_adjust(left=0.4)

        ax.grid(axis="x")  # Legger til rutenett (bare vertikale linjer)
        plt.show()


Skilsmisser = Fil("Skilsmisserogekteskap.csv", "csv",
                  "Inngåtte ekteskap og skilsmisser fra 1902 til 2022")
Skilsmisser.plotteGraf()
