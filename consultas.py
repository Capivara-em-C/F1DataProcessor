from main import constructors
from main import drivers
from main import races
from main import results
from main import classificacoes
import matplotlib.pyplot as plt

vitorias = []
corridas_2006 = []
vitorias_2006 = []
anos = ["2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018"]


def format_date(date: str) -> str:
    splited_date = date.split("-")
    if len(splited_date) > 1:
        splited_date.reverse()
        return "/".join(splited_date)

    return date


def plot_data(items: dict, title, x_label, y_label):
    x_axis = []
    y_axis = []

    for key, value in items:
        if value >= 1:
            x_axis.append(key)
            y_axis.append(value)

    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    plt.bar(x_axis, y_axis)
    plt.show()


# Pegar vitorias de 2006 para frente
for corrida in races:
    if corrida.year in anos:
        corridas_2006.append(corrida)

for resultado in results:
    if resultado.positionOrder == "1":
        vitorias.append(resultado)

for vitoria in vitorias:
    for corrida in corridas_2006:
        if vitoria.raceId == corrida.id:
            vitorias_2006.append(vitoria)

piloto_por_pais = {}

# Pegar nacionalidades
for piloto in drivers:
    if piloto.nationality not in piloto_por_pais:
        piloto_por_pais[piloto.nationality] = 1
    else:
        piloto_por_pais[piloto.nationality] += 1

# O piloto mais velho que correu em 2006 foi Michael Schumacher que hoje tem 51 anos
# Logo filtramos os pilotos pela idade 51
pilotos_2006 = []

for piloto in drivers:
    date_birth = format_date(piloto.date_of_birth)

    if date_birth != "" and (2020 - int(date_birth[6:10])) <= 51:
        pilotos_2006.append(piloto)

# PEGAR VITÓRIAS POR PAÍS#

paises = {}

# pegando paises
for piloto in pilotos_2006:
    if piloto.nationality not in paises:
        paises[piloto.nationality] = 0

# pegando vitórias de cada equipe
for piloto in pilotos_2006:
    for vitoria in vitorias_2006:
        if piloto.driver_id == vitoria.driverId:
            paises[piloto.nationality] += 1

# VITORIAS POR EQUIPE

# pegando equipes
equipes = {}

for equipe in constructors:
    if equipe.constructor_ref not in equipes:
        equipes[equipe.constructor_ref] = 0

# contando vitórias de cada equipe
for equipe in constructors:
    for vitoria in vitorias_2006:
        if vitoria.constructorId == equipe.constructor_id:
            equipes[equipe.constructor_ref] += 1

idades = {
    "17 - 20": 0,
    "20 - 23": 0,
    "23 - 26": 0,
    "26 - 29": 0,
    "29 - 32": 0,
    "32 - 35": 0,
    "35 - 38": 0,
    "38 - 41": 0
}

idades_valores = []

vitoria_piloto = {}

# Fazendo pares ordenados com o id da vitoria e o id do piloto, pra pegar o ano da corrida porteriormente
for vitoria in vitorias_2006:
    for piloto in pilotos_2006:
        if vitoria.driverId == piloto.driver_id:
            vitoria_piloto[vitoria.raceId] = piloto.driver_id

# Pegando idade dos pilotos quando eles venceram corridas
for id_vitoria, pilotoId in vitoria_piloto.items():
    for corrida in corridas_2006:
        if id_vitoria == corrida.id:
            for piloto in pilotos_2006:
                if piloto.driver_id == pilotoId:
                    idade = int(corrida.year) - int(piloto.date_of_birth[6:10])
                    idades_valores.append(idade)

# quantidade de vitórias por intervalo de idade
for idade in idades_valores:
    for intervalo_de_idade in idades.keys():
        if idade >= int(intervalo_de_idade[0:2]) and idade < int(intervalo_de_idade[5:7]):
            idades[intervalo_de_idade] += 1

# campeonatos por paises
paises_campeonatos = {}

for classificacao in classificacoes:
    if classificacao.nationality not in paises_campeonatos.keys():
        paises_campeonatos[classificacao.nationality] = 0

for classificacao in classificacoes:
    paises_campeonatos[classificacao.nationality] += 1

# campeonatos por idade

idades_campeonatos = {
    "17 - 20": 0,
    "20 - 23": 0,
    "23 - 26": 0,
    "26 - 29": 0,
    "29 - 32": 0,
    "32 - 35": 0,
    "35 - 38": 0,
    "38 - 41": 0
}

for classificacao in classificacoes:
    for piloto in pilotos_2006:
        if classificacao.driverId == piloto.driver_id:
            for intervalo_de_idade in idades_campeonatos.keys():
                idade = int(classificacao.year) - int(piloto.date_of_birth[6:10])

                if int(intervalo_de_idade[0:2]) <= idade < int(intervalo_de_idade[5:7]):
                    idades_campeonatos[intervalo_de_idade] += 1

# campeonatos por equipe

equipes_campeonatos = {}

for classificacao in classificacoes:
    if classificacao.equipe not in equipes_campeonatos.keys():
        equipes_campeonatos[classificacao.equipe] = 0

for classificacao in classificacoes:
    equipes_campeonatos[classificacao.equipe] += 1

for k, v in paises_campeonatos.items():
    print(k + ": " + str(v))
