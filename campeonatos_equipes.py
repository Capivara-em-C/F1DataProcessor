from consultas import equipes_campeonatos
import matplotlib.pyplot as plt

data = {"x":[], "y":[]}


for key,value in equipes_campeonatos.items():
    data["x"].append(key)
    data["y"].append(value)


plt.title("Campeonatos por equipe (2006-2019)")
plt.xlabel("Equipes")
plt.ylabel("Campeonatos")

plt.bar((data["x"]), (data["y"]))
plt.show()
