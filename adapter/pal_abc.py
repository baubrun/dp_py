from abc import ABCMeta, abstractmethod


class PalABC(metaclass=ABCMeta):

    @abstractmethod
    def total_amount(self):
        pass

    @abstractmethod
    def cvv(self):
        pass

    @abstractmethod
    def customer_card_number(self):
        pass

    @abstractmethod
    def card_exp_month_date(self):
        pass

    @abstractmethod
    def customer_card_name(self):
        pass


