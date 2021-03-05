import os
import sys
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from sphero_sdk import SpheroRvrObserver
from sphero_sdk import Colors
from sphero_sdk import RvrStreamingServices

rvr = SpheroRvrObserver()
forTheLoop = True
def ambient_light_handler(ambient_light_data):
    print('Accelerometer data response: ', ambient_light_data)
def main():
    """ This program demonstrates how to set the all the LEDs of RVR using the LED control helper.
    """
    rvr.wake()

    # Give RVR time to wake up
    time.sleep(2)
    try:
        rvr.sensor_control.add_sensor_data_handler(
            service=RvrStreamingServices.ambient_light,
            handler=ambient_light_handler
        )

        rvr.sensor_control.start(interval=250)

        rvr.led_control.set_all_leds_color(color=Colors.yellow)

        # Delay to show LEDs change
        time.sleep(1)

    except KeyboardInterrupt:
        print('\nProgram terminated with keyboard interrupt.')

    finally:
        rvr.close()

if forTheLoop == True:
    main()
