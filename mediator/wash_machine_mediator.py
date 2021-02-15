from abc import abstractmethod, ABCMeta


class WashMachineMediator(metaclass=ABCMeta):

    @abstractmethod
    def check_temperature(self, temperature):
        pass

    @abstractmethod
    def on(self):
        pass

    @abstractmethod
    def off(self):
        pass

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def closed(self):
        pass

    @abstractmethod
    def wash(self):
        pass


