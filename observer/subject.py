from abc import ABCMeta, abstractmethod

class Subject(metaclass=ABCMeta):

    @abstractmethod
    def notify_observers(self):
        pass

    @abstractmethod
    def subscribe_observer(self, observer):
        pass

    @abstractmethod
    def subject_details(self):
        pass

    @abstractmethod
    def set_desc(self, desc):
        pass

    @abstractmethod
    def unsubscribe_observer(self, observer):
        pass
