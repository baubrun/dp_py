from sports_car_builder import SportsCarBuilder


class CarDirector:
    def __init__(self):
        self.builder = None


    def build_car(self, builder):
        self.builder = builder
        [step() for step in (
            builder.build_body_style,
            builder.build_power,
            builder.build_engine,
            builder.build_breaks,
            builder.build_seats,
            builder.build_windows,
            builder.build_fuel_type,
        )]

    @property
    def car(self):
        return self.builder.get_car()

