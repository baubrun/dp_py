from abc import ABCMeta, abstractmethod


class StripesABC(metaclass=ABCMeta):

    @abstractmethod
    def amount(self):
        pass

    @abstractmethod
    def card_cvv(self):
        pass

    @abstractmethod
    def card_number(self):
        pass

    @abstractmethod
    def card_exp_month_day(self):
        pass

    @abstractmethod
    def card_exp_year(self):
        pass

    @abstractmethod
    def customer_name(self):
        pass


