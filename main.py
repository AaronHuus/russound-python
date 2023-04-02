import logging
from russound.russound import Russound

# TCP to Serial Redirector here
# https://github.com/pyserial/pyserial/blob/master/examples/tcp_serial_redirect.py

IP_ADDRESS = '192.168.0.2'
PORT = 7777
logging.basicConfig(filename='russound_debugging.log', level=logging.DEBUG,
                    format='%(asctime)s:%(name)s:%(levelname)s:%(funcName)s():%(message)s')
_LOGGER = logging.getLogger(__name__)


def turn_on_zones(x: Russound):
    for zone in range(1, 5):
        turn_on_zone(x, zone)


def turn_on_zone(x: Russound, zone):
    x.set_power('1', zone, '1')
    print("Power status zone", zone, "is", x.get_power('1', zone))


def turn_off_zones(x: Russound):
    for zone in range(1, 5):
        turn_off_zone(x, zone)


def turn_off_zone(x: Russound, zone: int):
    x.set_power('1', zone, '0')
    print("Power status zone", zone, "is", x.get_power('1', zone))


def set_volumes(x: Russound, volume_level: int):
    for zone in range(1, 5):
        set_volume(x, volume_level, zone)


def set_volume(x: Russound, volume_level: int, zone: int):
    x.set_volume('1', zone, volume_level)
    print("Volume on zone", zone, "is", x.get_volume('1', zone))


def set_sources(x: Russound, source: int):
    for zone in range(1, 5):
        set_source(x, source, zone)


def set_source(x: Russound, source: int, zone: int):
    x.set_source('1', zone, source)
    print("Source on zone", zone, "is", x.get_source('1', zone))


if __name__ == "__main__":
    controller = Russound(IP_ADDRESS, PORT)
    controller.connect()
    print(controller.is_connected())

    #turn_on_zones(controller)
    #set_volumes(controller, 90)
    set_sources(controller, 2)

    # turn_off_zones(controller)

    # turn_on_zone(controller, 1)
    # turn_on_zone(controller, 2)
    # turn_on_zone(controller, 3)
    # turn_on_zone(controller, 4) # Main Bedroom

    # turn_off_zone(controller, 1)
    # turn_off_zone(controller, 2)
    # turn_off_zone(controller, 3)
    # turn_off_zone(controller, 4) # Main Bedroom
