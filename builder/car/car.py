# product part of builder
class Car:
    def __init__(self, car_type):

        self.car_type = car_type
        self._body_style = None
        self._power = None
        self._engine = None
        self._breaks = None
        self._seats = None
        self._windows = None
        self._fuel_type = None

    @property
    def body_style(self):
        return self._body_style

    @body_style.setter
    def body_style(self, body_style):
        self._body_style = body_style

    @property
    def power(self):
        return self._power

    @power.setter
    def power(self, power):
        self._power = power

    @property
    def engine(self):
        return self._engine

    @engine.setter
    def engine(self, engine):
        self._engine = engine

    @property
    def breaks(self):
        return self._breaks

    @breaks.setter
    def breaks(self, breaks):
        self._breaks = breaks

    @property
    def seats(self):
        return self._seats

    @seats.setter
    def seats(self, seats):
        self._seats = seats

    @property
    def windows(self):
        return self._windows

    @windows.setter
    def windows(self, windows):
        self._windows = windows

    @property
    def fuel_type(self):
        return self._fuel_type

    @fuel_type.setter
    def fuel_type(self, fuel_type):
        self._fuel_type = fuel_type


    def __str__(self):
        return f""" 
        Car Type: {self.car_type}
        Body style: {self._body_style}
        Power: {self._power}
        Engine: {self._engine}
        Breaks: {self._breaks}
        Windows: {self._windows}
        Fuel Type: {self._fuel_type}
        """
