from wash_machine_colleague import WashMachineColleague


class Heater(WashMachineColleague):
    def __init__(self):
        self._mediator = None

    def set_mediator(self, mediator):
        self._mediator = mediator

    def on(self, temperature):
        print("Heater is on.")
        if self._mediator.check_temperature(temperature):
            print(f"Temperature set to {temperature}C.")
            self._mediator.off()

    def off(self):
        print("Heater is off.")
        self._mediator.wash()

