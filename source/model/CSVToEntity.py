import csv


class CSVToEntity:
    @staticmethod
    def csv_process(path, row_to_entity_function):
        entities = []

        with open(path, newline="", encoding='utf-8') as csvFile:
            rows = csv.reader(csvFile, delimiter=",")

            is_first_row = True
            for row in rows:
                if is_first_row:
                    is_first_row = False
                    continue

                entities += [
                    row_to_entity_function(row)
                ]

        return entities
