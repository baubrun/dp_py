from abc import abstractmethod, ABCMeta


class WashMachineColleague(metaclass=ABCMeta):

    @abstractmethod
    def set_mediator(self, mediator):
        pass