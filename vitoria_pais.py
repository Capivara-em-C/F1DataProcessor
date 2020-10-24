from consultas import paises
import matplotlib.pyplot as plt


data = {"x":[], "y":[]}


for key,value in paises.items():
    if value >= 1:
        data["x"].append(key)
        data["y"].append(value)


data["x"] = sorted(data["x"])
data["y"] = sorted(data["y"])
plt.title("Vitórias por equipe (2006-2018)")
plt.xlabel("Equipes")
plt.ylabel("Vitorias")


plt.bar(data["x"], data["y"])

