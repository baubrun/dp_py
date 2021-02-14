from abc import ABCMeta, abstractmethod

class Observer(metaclass=ABCMeta):

    @abstractmethod
    def update(self, desc):
        pass

    @abstractmethod
    def unsubscribe(self):
        pass

    @abstractmethod
    def subscribe(self):
        pass

