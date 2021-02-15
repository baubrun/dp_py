from payment import Payment


class Bank(Payment):
    def __init__(self):
        self._card = None
        self._account = None

    def __check_funds(self):
        print(f"Checking account {self.__get_account()} for sufficient funds...")
        return True

    def __get_account(self):
        self._account = self._card
        return self._account

    def set_card(self, card):
        self._card = card

    def charge(self):
        if self.__check_funds():
            print("Charging merchant...")
            return True
        else:
            print("Insufficient funds.")
            return False