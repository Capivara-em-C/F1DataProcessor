from consultas import paises
import matplotlib.pyplot as plt


data = {"x":[], "y":[]}


for key,value in paises.items():
    if value >= 1:
        data["x"].append(key)
        data["y"].append(value)


plt.title("Vitórias por País (2006-2018)")
plt.xlabel("País")
plt.ylabel("Vitorias")


plt.bar(data["x"], data["y"])

