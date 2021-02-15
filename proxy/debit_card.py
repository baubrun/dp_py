from payment import Payment
from bank import Bank


class DebitCard(Payment):
    def __init__(self):
        self._bank = Bank()


    def charge(self):
        card = input("Enter your card # :>> ")
        self._bank.set_card(card)
        return self._bank.charge()