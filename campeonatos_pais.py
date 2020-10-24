from consultas import paises_campeonatos
import matplotlib.pyplot as plt

data = {"x":[], "y":[]}


for key,value in paises_campeonatos.items():
    data["x"].append(key)
    data["y"].append(value)


plt.title("Campeonatos por país (2006-2019)")
plt.xlabel("Países")
plt.ylabel("Campeonatos")

plt.bar((data["x"]), (data["y"]))
