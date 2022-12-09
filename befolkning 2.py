import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import csv

filnavn = "Befolkning.csv"

ar = []
befolkning = []

with open(filnavn, encoding="utf-8-sig") as fil:
  filinnhold = csv.reader(fil, delimiter=";")

  overskrifter = next(filinnhold)
  next(filinnhold)
  next(filinnhold)
  print(overskrifter)

  for rad in filinnhold:
    print(rad)
    ar.append(int(rad[0])) #x-akse
    befolkning.append(int(rad[1])) #y-akse

print(ar)
print(befolkning)




plt.plot(ar, befolkning)  # Lager stolpediagrammet
plt.title("Befolkning i Norge per 1. januar 1769-2022")
plt.grid(axis="y")  # Legger til rutenett (bare horisontale linjer)
plt.xlabel("År")
plt.ylabel("Befolkning i millioner")
plt.xlim(1769,2022)
#plt.ylim(0,6000000)
xlabels = ['jan','feb','mar','apr','may','jun']
plt.show()   


class Graf:
  def __init__(self,filnavn,skilletegn = ",",tegn="utf-8-sig"):
        self.csvfil = csvfil
        self.txtfil = txtfil 
        self.tegn = tegn
        self.skilletegn = skilletegn
        self.filinnholdcsv = []
        self.filinnholdtxt = []
        self.navneliste = []

        with open(self.csvfil, encoding=self.tegn) as fil:
                filinnholdet = csv.reader(fil, delimiter=self.skilletegn)

                for rad in filinnholdet:
                    for info in rad:
                        self.filinnholdcsv.append(info)

        with open(self.txtfil,encoding="utf-8-sig") as fil:
                for linje in fil:
                    info = linje.rstrip()
                    self.filinnholdtxt.append(info)
                del self.filinnholdtxt[3::4] #for å fjerne hver 4 element som er bare ''

        self.navneliste = self.filinnholdcsv+self.filinnholdtxt #Lage en felles liste fra csv filen og txt filen
