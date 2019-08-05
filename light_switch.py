from time import sleep
import RPi.GPIO as GPIO
from ky040.KY040 import KY040
import paho.mqtt.publish as publish


# Hallway
hall_clock_pin  = 21
hall_data_pin   = 20
hall_switch_pin = 16

# Landing
landing_clock_pin  = 26
landing_data_pin   = 19
landing_switch_pin = 13


def rotary_change_hall(direction):
    print("hall turned - " + str(direction))
    # publish.single("cmnd/kitchen/power", "off", hostname="192.168.1.38",auth={'username':"mqtt", 'password':"mqtt"})


def switch_pressed_hall():
    print("hall button pressed")
    publish.single("hallway/lifx/light/switch", "toggle", hostname="192.168.1.38",auth={'username':"mqtt", 'password':"mqtt"})

def rotary_change_landing(direction):
    print("landing turned - " + str(direction))
    # publish.single("cmnd/kitchen/power", "off", hostname="192.168.1.38",auth={'username':"mqtt", 'password':"mqtt"})


def switch_pressed_landing():
    print("landing button pressed")
    publish.single("landing/lifx/light/switch", "toggle", hostname="192.168.1.38",auth={'username':"mqtt", 'password':"mqtt"})

GPIO.setmode(GPIO.BCM)

hall_switch    = KY040(hall_clock_pin, hall_data_pin, hall_switch_pin, rotary_change_hall, switch_pressed_hall)
landing_switch = KY040(landing_clock_pin, landing_data_pin, landing_switch_pin, rotary_change_landing, switch_pressed_landing)

hall_switch.start()
landing_switch.start()

try:
    while True:
        sleep(0.1)
finally:
    hall_switch.stop()
    landing_switch.stop()
    GPIO.cleanup()
