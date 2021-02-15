from debit_card import DebitCard

class Customer:
    def __init__(self):
        print("Making a purchase...")
        self._debit_card = DebitCard()
        self._is_purchased = None

    def make_payment(self):
        self._is_purchased = self._debit_card.charge()


    def __del__(self):
        if self._is_purchased:
            print("Item purchased.")
        else:
            print("Not enough funds.")

