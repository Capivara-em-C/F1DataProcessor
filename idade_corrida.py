from consultas import drivers, races, results, idades, plot_data
import time

inicio = time.time()

# Idade por corrida
idade_corridas = {
    "17 - 20": 0,
    "20 - 23": 0,
    "23 - 26": 0,
    "26 - 29": 0,
    "29 - 32": 0,
    "32 - 35": 0,
    "35 - 38": 0,
    "38 - 41": 0
}

for piloto in drivers:
    for race in races:
        for result in results:
            if result.race_id == race.race_id and result.driver_id == piloto.driver_id:
                for idade_corrida in idade_corridas.keys():
                    idade = int(race.year) - int(piloto.date_of_birth[6:10])

                    if int(idade_corrida[0:2]) <= idade < int(idade_corrida[5:7]):
                        idade_corridas[idade_corrida] += 1

for key, value in idade_corridas.items():
    idade_corridas[key] = idades[key] / value * 100

plot_data(
    idade_corridas.items(),
    "Porcentagem de vitórias por idade de pilotos (2006-2018)",
    "Idades de pilotos",
    "Porcentagem de vitórias(%)",
)

fim = time.time()

print("\n\nTempo de execução: ", (fim - inicio), "s\n")
