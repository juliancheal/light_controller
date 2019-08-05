#! /usr/bin/python3

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import requests #import async
import paho.mqtt.publish as publish

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

button_on = False
while True: # Run forever
        if GPIO.input(10) == GPIO.HIGH and button_on == False:
                    print(button_on)
                    button_on = True
                    print("Button is off!")
                    publish.single("cmnd/kitchen/power", "off", hostname="192.168.1.38",auth={'username':"mqtt", 'password':"mqtt"})
        if GPIO.input(10) == GPIO.LOW and button_on == True:
                    print(button_on)
                    button_on = False
                    print("Button is on")
                    publish.single("cmnd/kitchen/power", "on", hostname="192.168.1.38",auth={'username':"mqtt", 'password':"mqtt"})
