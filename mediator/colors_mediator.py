from wash_machine_mediator import WashMachineMediator


class ColorsMediator(WashMachineMediator):

    def __init__(self, heater, machine, motor,
                 stain_removal, sensor, valve):
        self._heater = heater
        self._machine = machine
        self._motor = motor
        self._stain_removal = stain_removal
        self._sensor = sensor
        self._valve = valve
        print("Washing colors.")

    def check_temperature(self, temperature):
        return self._sensor.check_temperature(temperature)

    def on(self):
        self._heater.on(0)

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
        self._motor.rotate_drum(400)
        print("Adding detergent.")
        self._stain_removal.heavy()
        print("Adding softener.")

