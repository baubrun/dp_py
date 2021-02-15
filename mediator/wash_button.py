from wash_machine_colleague import WashMachineColleague


class WashButton(WashMachineColleague):
    def __init__(self):
        self._mediator = None

    def set_mediator(self, mediator):
        self._mediator = mediator


    def press(self):
        print("Starting wash.")
        self._mediator.start()

