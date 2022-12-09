import csv
import matplotlib.pyplot as plt


class Fil:
    def __init__(self, filnavn, filtype, overskrift):
        self.filnavn = filnavn
        self.filtype = filtype
        self.overskrift = overskrift
        self.data = []
        self.aarstall = []
        self.ekteskap = []
        self.skillsmisse = []

        if filtype == "csv":
            with open(filnavn, encoding="utf-8") as fil:
                self.filinnhold = csv.reader(fil, delimiter=";")

                overskrifter = next(self.filinnhold)
              #  print(str(overskrifter))

                for rad in self.filinnhold:
                    self.data.append(rad)

                self.aarstall.append(self.data[0])
                self.ekteskap.append(self.data[1])
                self.skillsmisse.append(self.data[2])

    def fjerneOverskrift(self):
        self.aarstall.pop()


Skilsmisser = Fil("Skilsmisserogekteskap.csv", "csv",
                  "Inngåtte ekteskap og skilsmisser fra 1902 til 2022")
