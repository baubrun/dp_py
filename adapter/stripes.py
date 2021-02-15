from stripes_abc import StripesABC


class Stripes(StripesABC):
    def __init__(self):
        self._amount = None
        self._card_cvv = None
        self._card_number = None
        self._card_exp_month_day = str()
        self._card_exp_year = str()
        self._customer_name = str()


    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount

    @property
    def card_cvv(self):
        return self._card_cvv

    @card_cvv.setter
    def card_cvv(self, cvv):
        self._card_cvv = cvv

    @property
    def card_number(self):
        return self._card_number

    @card_number.setter
    def card_number(self, card_number):
        self._card_number = card_number

    @property
    def card_exp_month_day(self):
        return self._card_exp_month_day

    @card_exp_month_day.setter
    def card_exp_month_day(self, exp_month):
        self._card_exp_month_day = exp_month

    @property
    def card_exp_year(self):
        return self._card_exp_year

    @card_exp_year.setter
    def card_exp_year(self, exp_year):
        self._card_exp_year = exp_year

    @property
    def customer_name(self):
        return self._customer_name

    @customer_name.setter
    def customer_name(self, name):
        self._customer_name = name