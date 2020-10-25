from consultas import idades_campeonatos, plot_data

plot_data(
    idades_campeonatos.items(),
    "Campeonatos vencidos por idade (2006-2018)",
    "idade",
    "Campeonatos vencidos",
)
