from main import constructors
from main import drivers
from main import races
from main import circuits
from main import results
import matplotlib.pyplot as plt

vitorias = []
corridas_2006 = []
vitorias_2006 = []
anos = ["2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018"]

#Pegar vitorias de 2006 para frente
for corrida in races:
    for corrida1 in corrida:
        if corrida1.year in anos:
            corridas_2006.append(corrida1)


for resultado in results:
    for resultado1 in resultado:
        if resultado1.positionOrder == "1":
            vitorias.append(resultado1)


for vitoria in vitorias:
    for corrida in corridas_2006:
        if vitoria.raceId == corrida.id:
            vitorias_2006.append(vitoria)


piloto_por_pais = {}

#pegar quantos pilotos por pais
for piloto in drivers:
    for piloto1 in piloto:
        if piloto1.nationality not in piloto_por_pais:
            piloto_por_pais[piloto1.nationality] = 1
        else:
            piloto_por_pais[piloto1.nationality] += 1


#PEGAR VITÓRIAS POR PAÍS#

paises = {}

#pegando paises
for piloto in drivers:
    for piloto1 in piloto:
        if piloto1.nationality not in paises:
            paises[piloto1.nationality] = 0

for piloto in drivers:
    for piloto1 in piloto:
        for vitoria in vitorias_2006:
            if piloto1.driver_id == vitoria.driverId:
                paises[piloto1.nationality] += 1




#VITORIAS POR EQUIPE

#pegando equipes

equipes = {}

for equipe in constructors:
    for equipe1 in equipe:
        if equipe1.constructor_ref not in equipes:
            equipes[equipe1.constructor_ref] = 0

for equipe in constructors:
    for equipe1 in equipe:
        for vitoria in vitorias:
            if vitoria.constructorId == equipe1.constructor_id:
                equipes[equipe1.constructor_ref] += 1


#grafico vitorias por equipe
data = {"x":[], "y":[]}

for key,value in equipes.items():
    if value >= 20:
        data["x"].append(key)
        data["y"].append(value)

data["x"] = sorted(data["x"])
data["y"] = sorted(data["y"])


plt.bar((data["x"]), (data["y"]))
plt.show()
