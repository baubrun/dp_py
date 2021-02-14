from car_builder import CarBuilder
from car import Car



class SportsCarBuilder(CarBuilder):

    def __init__(self):
        self._car = Car("SPORTS")

    def build_body_style(self):
        self._car.body_style = \
            """External dimensions: 
            overall length: 490cm, \
            overall width: 192cm,  \
            overall height: 138cm \
            wheelbase: 285cm \
            """

    def build_power(self):
        self._car.power = "323 hp @ 6,800 rpm; 6m lb of torque @ 4,800 rpm"

    def build_engine(self):
        self._car.engine = "3.6L V 6 DOHC and variable valve timing"

    def build_breaks(self):
        self._car.breaks = """Four-wheel disc brakes: two ventilated. Electronic brake - distribution. \
                           StabiliTrak stability control"""

    def build_seats(self):
        self._car.seats = """Driver sports front seat with one power adjustments manual  - \
        height, front passenger seat sports front seat with one power - adjustments"""

    def build_windows(self):
        self._car.windows = "Front windows with one-touch on two windows"

    def build_fuel_type(self):
        self._car.fuel_type = "Gasoline 28 KMPG city, 45 KMPG highway, 32 KMPG combined and - 611 KM. range"

    def get_car(self):
        return self._car

