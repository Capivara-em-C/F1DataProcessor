from consultas import paises_campeonatos, plot_data

plot_data(
    paises_campeonatos.items(),
    "Campeonatos vencidos por país (2006-2019)",
    "Países",
    "Campeonatos vencidos"
)
