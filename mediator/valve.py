from wash_machine_colleague import WashMachineColleague



class Valve(WashMachineColleague):
    def __init__(self):
        self._mediator = None

    def set_mediator(self, mediator):
        self._mediator = mediator

    def open(self):
       print("Opened valve.")
       print("Filling water.")
       self._mediator.closed()

    def closed(self):
       print("Closed valve.")
       self._mediator.on()

