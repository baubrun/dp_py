from caterer import Caterer
from concierge import Concierge
from florist import Florist
from musician import Musician


class EventManager:
    def __init__(self):
        print("Event Manager: I will take care of everything.\n")

    def arrange(self):
        self.caterer = Caterer()
        self.caterer.set_catering()
        self.concierge = Concierge()
        self.concierge.reserve_hotel()
        self.florist = Florist()
        self.florist.set_flower_requirements()
        self.musician = Musician()
        self.musician.set_music_type()