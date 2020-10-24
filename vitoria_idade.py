from consultas import idades
import matplotlib.pyplot as plt

data = {"x":[], "y":[]}


for key,value in idades.items():
    data["x"].append(key)
    data["y"].append(value)


plt.title("Vitórias por idade (2006-2018)")
plt.xlabel("Intervalo de idade")
plt.ylabel("vitórias")

plt.bar((data["x"]), (data["y"]))
