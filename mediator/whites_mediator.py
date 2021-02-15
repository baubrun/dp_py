from wash_machine_mediator import WashMachineMediator


class WhitesMediator(WashMachineMediator):

    def __init__(self, heater, machine, motor,
                 stain_removal, sensor, valve):
        self._heater = heater
        self._machine = machine
        self._motor = motor
        self._stain_removal = stain_removal
        self._sensor = sensor
        self._valve = valve
        print("Washing whites.")

    def check_temperature(self, tempearature):
        return self._sensor.check_temperature(tempearature)

    def on(self):
        self._heater.on(30)

    def off(self):
        self._heater.off()

    def open(self):
        self._valve.open()

    def closed(self):
        self._valve.closed()


    def start(self):
        self._machine.start()

    def wash(self):
        self._motor.start_motor()
        self._motor.rotate_drum(600)
        print("Adding detergent.")
        self._stain_removal.regular()
        print("Adding softener.")

