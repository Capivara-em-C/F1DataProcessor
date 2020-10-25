from main import constructors
from main import drivers
from main import races
from main import results
from main import classificacoes
import matplotlib.pyplot as plt

vitorias = []
anos = ["2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018"]


def format_date(date: str) -> str:
    split_date = date.split("-")
    if len(split_date) > 1:
        split_date.reverse()
        return "/".join(split_date)

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
corridas_2006 = []

for corrida in races:
    if corrida.year in anos:
        corridas_2006.append(corrida)

races = corridas_2006

for resultado in results:
    is_race_in_result = False
    for race in races:
        if resultado.race_id == race.race_id:
            is_race_in_result = True

    if resultado.position_order == "1" and is_race_in_result:
        vitorias.append(resultado)

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

    if date_birth != '' and (2020 - int(date_birth[6:10])) <= 51:
        pilotos_2006.append(piloto)

drivers = pilotos_2006

# PEGAR VITÓRIAS POR PAÍS #
paises = {}

# pegando paises
for piloto in drivers:
    if piloto.nationality not in paises:
        paises[piloto.nationality] = 0

# pegando vitórias de cada pais
for piloto in drivers:
    for vitoria in vitorias:
        if piloto.driver_id == vitoria.driver_id:
            paises[piloto.nationality] += 1

# VITORIAS POR EQUIPE
# pegando equipes
equipes = {}

for equipe in constructors:
    if equipe.name not in equipes:
        equipes[equipe.name] = 0

# contando vitórias de cada equipe
for equipe in constructors:
    for vitoria in vitorias:
        if vitoria.constructor_id == equipe.constructor_id:
            equipes[equipe.name] += 1

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

# Fazendo pares ordenados com o id da vitoria e o id do piloto, pra pegar o ano da corrida posteriormente
for vitoria in vitorias:
    for piloto in drivers:
        if vitoria.driver_id == piloto.driver_id:
            vitoria_piloto[vitoria.race_id] = piloto.driver_id

# Pegando idade dos pilotos quando eles venceram corridas
for id_race, piloto_id in vitoria_piloto.items():
    for corrida in races:
        if id_race == corrida.race_id:
            for piloto in drivers:
                if piloto.driver_id == piloto_id:
                    idade = int(corrida.year) - int(piloto.date_of_birth[6:10])
                    idades_valores.append(idade)

# quantidade de vitórias por intervalo de idade
for idade in idades_valores:
    for intervalo_de_idade in idades.keys():
        if int(intervalo_de_idade[0:2]) <= idade < int(intervalo_de_idade[5:7]):
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
    for piloto in drivers:
        if classificacao.driver_id == piloto.driver_id:
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
