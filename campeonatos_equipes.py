from consultas import equipes_campeonatos, plot_data

plot_data(
    equipes_campeonatos.items(),
    "Campeonatos Vencidos por equipe (2006-2019)",
    "Equipes",
    "Campeonatos Vencidos"
)
