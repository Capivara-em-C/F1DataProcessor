from source.model.Race import Race
from source.model.Drivers import Driver
from source.model.Constructor import Constructor
from source.model.Circuit import Circuit
from source.model.Result import Result
from source.model.Classificacao import Classificacao
from source.model.CSVToEntity import CSVToEntity

csv_to_entity = CSVToEntity()

races = csv_to_entity.csv_process(
    "source/data/races.csv",
    lambda row:
        Race(
            row[0],
            row[1],
            row[2],
            row[3]
        )
)

drivers = csv_to_entity.csv_process(
    "source/data/drivers.csv",
    lambda row:
        Driver(
            row[0],
            row[1],
            row[6],
            row[7]
        )
)

results = csv_to_entity.csv_process(
    "source/data/results.csv",
    lambda row:
        Result(
            row[0],
            row[1],
            row[2],
            row[3],
            row[5],
            row[8],
            row[9],
            row[14]
        )
)

circuits = csv_to_entity.csv_process(
    "source/data/circuits.csv",
    lambda row:
        Circuit(
            row[0],
            row[2],
            row[3],
            row[4]
        )
)

constructors = csv_to_entity.csv_process(
    "source/data/constructors.csv",
    lambda row:
        Constructor(
            row[0],
            row[1],
            row[3],
        )
)

classificacoes = csv_to_entity.csv_process(
    "source/data/classificacao.csv",
    lambda row:
        Classificacao(
            row[0],
            row[1],
            row[2],
            row[3],
            row[4]
        )
)
