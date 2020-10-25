

class Result:
    def __init__(
            self,
            result_id,
            race_id,
            driver_id,
            constructor_id,
            grid,
            position_order,
            points,
            rank
    ):
        self.result_id = result_id
        self.race_id = race_id
        self.driver_id = driver_id
        self.constructor_id = constructor_id
        self.grid = grid
        self.position_order = position_order
        self.points = points
        self.rank = rank
