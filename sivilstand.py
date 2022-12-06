import matplotlib.pyplot as plt
import json
import numpy as np


filnavn = "sivilstand.json"
gjennomsnitt1 = []
gjennomsnitt2 = []
gjennomsnitt3 = []
gjennomsnitt4 = []
gjennomsnitt5 = []

with open(filnavn, encoding="utf-8") as fil:
    data = json.load(fil)

    aarstallData = data["dataset"]["dimension"]["Tid"]["category"]["label"]
    aarstall = list(aarstallData.values())

    gjennomsnittData = data["dataset"]["value"]

    for i in range(0, 42):
        gjennomsnitt1.append(gjennomsnittData[i])

    for i in range(42, 42+42):
        gjennomsnitt2.append(gjennomsnittData[i])

    for i in range(84, 84+42):
        gjennomsnitt3.append(gjennomsnittData[i])

    for i in range(126, 126+42):
        gjennomsnitt4.append(gjennomsnittData[i])

    for i in range(168, len(gjennomsnittData)):
        gjennomsnitt5.append(gjennomsnittData[i])


print(gjennomsnittData)
print(aarstall)


plt.plot(aarstall, gjennomsnitt1)
plt.plot(aarstall, gjennomsnitt2)
plt.plot(aarstall, gjennomsnitt3)
plt.plot(aarstall, gjennomsnitt4)
plt.plot(aarstall, gjennomsnitt5)
plt.ylim(0, 700000)
plt.xlabel("År")
plt.ylabel("")
plt.title("")
plt.grid()
plt.show()
