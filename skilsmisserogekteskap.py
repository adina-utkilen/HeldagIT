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
              #  print(str(overskrifter))

                for rad in self.filinnhold:
                    self.data.append(rad)

                for i in range(0, len(self.data)):
                    self.data[i].pop(0)

                self.aarstall = self.data[0]
                self.ekteskap = self.data[1]
                self.skillsmisse = self.data[2]

                for i in range(0, len(self.aarstall)):
                    if self.aarstall[i] == "..":
                        self.aarstall[i] = 0
                    else:
                        self.aarstall[i] = int(self.aarstall[i])

                for i in range(0, len(self.ekteskap)):
                    if self.ekteskap[i] == "..":
                        self.ekteskap[i] = 0
                    else:
                        self.ekteskap[i] = int(self.ekteskap[i])

                print(self.ekteskap)

                for i in range(0, len(self.skillsmisse)):
                    if self.skillsmisse[i] == "..":
                        self.skillsmisse[i] = 0
                    else:
                        self.skillsmisse[i] = int(self.skillsmisse[i])

                print(self.aarstall)
                print(self.ekteskap)
                print(self.skillsmisse)

    def plotteGraf(self):
        # Angir dimensjoner for figure-objektet
        fig, ax = plt.subplots(figsize=(10, 5))

        y = np.arange(13)

        # Lager stolpediagram jenter
        ax.barh(y+0.2, self.ekteskap, height=0.4, label="Ekteskap")
        ax.barh(y-0.2, self.skillsmisse, height=0.4,
                label="Skillsmisse")  # Lager stolpediagram gutter
        # Legger til akseverdier
        ax.set_yticks(y, self.aarstall)
        ax.legend()                                               # Legger til beskrivelse

        # Øker plassen på venstre side av diagrammet
        fig.subplots_adjust(left=0.1)

        # Lager tittel
        plt.title('Inngåtte ekteskap og skilsmisser i perioden 1902-2022')

        ax.grid(axis="x")  # Legger til rutenett (bare vertikale linjer)
        plt.show()

        """
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
        """


Skilsmisser = Fil("Skilsmisserogekteskap.csv", "csv",
                  "Inngåtte ekteskap og skilsmisser fra 1902 til 2022")
Skilsmisser.plotteGraf()
