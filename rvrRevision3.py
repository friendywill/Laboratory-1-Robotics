import os
import sys
import time
import asyncio

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from sphero_sdk import SpheroRvrObserver
from sphero_sdk import RvrStreamingServices
from sphero_sdk import SpheroRvrAsync
from sphero_sdk import Colors
from sphero_sdk import RvrLedGroups
from sphero_sdk import SerialAsyncDal

rvrOb = SpheroRvrObserver()

headlights = 128


def main():

    try:
        rvrOb.wake()

        # Give RVR time to wake up
        time.sleep(2)

        rvrOb.sensor_control.add_sensor_data_handler(
            service=RvrStreamingServices.ambient_light,
            handler=ambient_light_handler
        )
        global light_data = ambient_light_handler

        rvrOb.sensor_control.start(interval=250)

        while True:
            # Delay to allow RVR to stream sensor data
            time.sleep(1)

    except KeyboardInterrupt:
        print('\nProgram terminated with keyboard interrupt.')

    finally:
        rvrOb.sensor_control.clear()

        # Delay to allow RVR issue command before closing
        time.sleep(.5)

        rvrOb.close()
        
    light_data = int(float(value))
    if light_data > 255:
        light_data = 255


while True:
    if light_data != headlights:
        if headlights < light_data:
            headlights = headlights + 1
        else:
            headlights = headlights - 1

    await rvr.wake()

    # Give RVR time to wake up
    await asyncio.sleep(2)

    await rvr.set_all_leds(
        led_group=RvrLedGroups.all_lights.value,
        led_brightness_values=[color for _ in range(10) for color in Colors.off.value]
    )

    # Delay to show LEDs change
    await asyncio.sleep(1)

    await rvr.set_all_leds(
        led_group=RvrLedGroups.headlight_left.value | RvrLedGroups.headlight_right.value,
        led_brightness_values=[
            headlights, headlights, headlights,
            headlights, headlights, headlights
        ]
    )

    # Delay to show LEDs change
    await asyncio.sleep(1)

    await rvr.close()


if __name__ == '__main__':
    main()

    try:
        loop.run_until_complete(
            main2()
        )

    except KeyboardInterrupt:
        print('\nProgram terminated with keyboard interrupt.')

        loop.run_until_complete(
            rvr.close()
        )

    finally:
        if loop.is_running():
            loop.close()
