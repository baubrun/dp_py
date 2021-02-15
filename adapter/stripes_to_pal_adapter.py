from pal_abc import PalABC

class StripesToPalAdapter(PalABC):
    def __init__(self, stripes):
        self._total_amount = None
        self._cvv = None
        self._customer_card_number = None
        self._card_exp_month_date = str()
        self._customer_card_name = str()
        self.stripes = stripes
        self.__set_adapter_props()

    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        self._total_amount = total_amount

    @property
    def cvv(self):
        return self._cvv

    @cvv.setter
    def cvv(self, cvv):
        self._cvv = cvv

    @property
    def customer_card_number(self):
        return self._customer_card_number

    @customer_card_number.setter
    def customer_card_number(self, card_number):
        self._customer_card_number = card_number

    @property
    def card_exp_month_date(self):
        return self._card_exp_month_date

    @card_exp_month_date.setter
    def card_exp_month_date(self, exp_date):
        self._card_exp_month_date = exp_date


    @property
    def customer_card_name(self):
        return self._customer_card_name

    @customer_card_name.setter
    def customer_card_name(self, name):
        self._customer_card_name = name

    def __set_adapter_props(self):
        self._total_amount = self.stripes.amount
        self._cvv = self.stripes.card_cvv
        self._customer_card_number = self.stripes.card_number
        self._card_exp_month_date = self.stripes._card_exp_month_day \
                                    + self.stripes.card_exp_year
        self._customer_card_name = self.stripes.customer_name
