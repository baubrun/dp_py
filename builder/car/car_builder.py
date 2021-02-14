from abc import ABCMeta, abstractmethod


class CarBuilder(metaclass=ABCMeta):

    @abstractmethod
    def build_body_style(self):
        pass

    @abstractmethod
    def build_power(self):
        pass

    @abstractmethod
    def build_engine(self):
        pass

    @abstractmethod
    def build_breaks(self):
        pass

    @abstractmethod
    def build_seats(self):
        pass

    @abstractmethod
    def build_windows(self):
        pass

    @abstractmethod
    def build_fuel_type(self):
        pass

