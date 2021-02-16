class Concierge:
    def __init__(self):
        print("Arranging the Hotel for Marriage? --")

    def __isAvailable(self):
        print("Is the Hotel free for the event on given day?")
        return True


    def reserve_hotel(self):
        if self.__isAvailable():
            print("Registered the Booking\n\n")


