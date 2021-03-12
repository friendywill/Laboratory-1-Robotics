"""
Author: William Friend
Date created: 02/03/2021
Date last changed: 07/03/2021
Version: 1.04

This program takes the ambient light data from the Sphero RVR ambient light sensor,
then sets the brightness of the LED's inversely proportional to how bright the
environmnet is around it. For example, if the environmnet is bright, the LED's will dim
down, whether if it were dim, the LED's would get brighter.
"""
import os
import sys
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from sphero_sdk import SpheroRvrObserver
from sphero_sdk import Colors
from sphero_sdk import RvrStreamingServices
from sphero_sdk import RvrLedGroups

# This value is for the imfinite loop
forTheLoop = True
rvr = SpheroRvrObserver()

# This section provides the ambient light levels from the sensors.
def ambient_light_handler(ambient_light_data):
    #This print will be removed, it is only for debugging
    print('Ambient light data response: ', ambient_light_data)
    global ambient_light
    ambient_light = ambient_light_data

# This section asks the users for input of their prefered minimum and maximum ambient
# brigtness levels for the Sphero RVR ambient sensors.
def minimumAmbientLevel():
    print(
        "At what ambient light level, would you like the LED's to be their brightest?")
    global minimum_ambient_level
    try:
        minimum_ambient_level = float(input())
    except ValueError:
        print("That value was invalid!")
        minimumAmbientLevel()
def maximumAmbientLevel():
    print(
        "At what ambient light level, would you like the LED's to be their dimmest?")
    global maximum_ambient_level
    try:
        maximum_ambient_level = float(input())
        if maximum_ambient_level == minimum_ambient_level:
            print("The maximum and minimum ambient levels cannot equal the same value!")
            maximumAmbientLevel()
    except ValueError:
        print("That value was invalid!")
        maximumAmbientLevel()

    
# This reacts inversely proportional to the ambient light
def light_reactor():
    rvr.wake()

    # Give RVR time to wake up
    time.sleep(2)
    try:
        rvr.sensor_control.add_sensor_data_handler(
            service=RvrStreamingServices.ambient_light,
            handler=ambient_light_handler
        )

        rvr.sensor_control.start(interval=250)
        
        # This is the if statement that handles the brightness of the LED's
        # depending on the ambient brightness
        if ambient_light > maximum_ambient_level:
            ambient_light_level = maximum_ambient_level
        elif ambient_light < minimum_ambient_level:
            ambient_light_level = minimum_ambient_level
        else:
            ambient_light_level = ambient_light
            
        # This is the mathematical equation that inversley sets the LED's to the
        # ambient light level
        led_value_multiplier = 1 - ((ambient_light - minimum_ambient_level) 
                                    / maximum_ambient_level -minimum_ambient_level)
        led_value = led_value_multiplier * 255
        rvr.set_all_leds(
            led_group=RvrLedGroups.headlight_left.value | RvrLedGroups.headlight_right.value,
            led_brightness_values=[
                led_value, led_value, led_value,
                led_value, led_value, led_value
            ]
        )
        print("This is the LED value:", led_value)
        time.sleep(1)

    except KeyboardInterrupt:
        print('\nProgram terminated with keyboard interrupt.')
        rvr.close()
        forTheLoop = False
minimumAmbientLevel()
maximumAmbientLevel()
while forTheLoop == True:
    light_reactor()
