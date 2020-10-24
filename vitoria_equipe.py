from consultas import equipes
import matplotlib.pyplot as plt

data = {"x":[], "y":[]}


for key,value in equipes.items():
    if value >= 20:
        data["x"].append(key)
        data["y"].append(value)


plt.title("Vitórias por equipe (2006-2018)")
plt.xlabel("Equipes")
plt.ylabel("Vitórias")

plt.bar((data["x"]), (data["y"]))

