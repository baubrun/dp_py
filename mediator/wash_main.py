from colors_mediator import ColorsMediator
from heater import Heater
from motor import Motor
from sensor import Sensor
from stain_removal import StainRemoval
from valve import Valve
from wash_button import WashButton
from wash_machine import WashMachine
from whites_mediator import WhitesMediator




def wash_main():
    heater = Heater()
    motor = Motor()
    sensor = Sensor()
    stain_removal = StainRemoval()
    wash_button = WashButton()
    wash_machine = WashMachine()
    valve = Valve()

    def wash_cycle(mediator):
        wash_machine.set_mediator(mediator)
        wash_button.set_mediator(mediator)
        heater.set_mediator(mediator)
        valve.set_mediator(mediator)
        wash_button.press()

    mediator = ColorsMediator(
        heater,
        wash_machine,
        motor,
        stain_removal,
        sensor,
        valve,
    )


    wash_cycle(mediator)
    print("\n")
    mediator = WhitesMediator(
        heater,
        wash_machine,
        motor,
        stain_removal,
        sensor,
        valve,
    )
    wash_cycle(mediator)


if __name__ == "__main__":
    wash_main()
