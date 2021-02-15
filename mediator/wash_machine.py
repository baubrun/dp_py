from wash_machine_colleague import WashMachineColleague


class WashMachine(WashMachineColleague):
    def __init__(self):
        self.mediator = None


    def set_mediator(self, mediator):
        self.mediator = mediator

    def start(self):
        self.mediator.open()

    def wash(self):
        self.mediator.wash()

