import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

import asyncio
from sphero_sdk import SpheroRvrAsync
from sphero_sdk import SerialAsyncDal
from sphero_sdk import RvrStreamingServices


loop = asyncio.get_event_loop()

rvr = SpheroRvrAsync(
    dal=SerialAsyncDal(
        loop
    )
)


async def ambient_light_handler(ambient_light_data):


async def main():
	def ambient():
		# This program demonstrates how to enable a single sensor to stream.

		await rvr.wake()

		# Give RVR time to wake up
		await asyncio.sleep(2)

		await rvr.sensor_control.add_sensor_data_handler(
			service=RvrStreamingServices.accelerometer,
			handler=ambient_light_handler
		)

		await rvr.sensor_control.start(interval=250)

		# The asyncio loop will run forever to allow infinite streaming.
	
		# This program demonstrates how to set the all the LEDs.
	async def led():

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
			led_group=RvrLedGroups.all_lights.value,
			led_brightness_values=[color for x in range(10) for color in [255, 255, 255]]
		)

		# Delay to show LEDs change
		await asyncio.sleep(1)

		await rvr.close()
	
	def reactor():
		


if __name__ == '__main__':
    try:
        asyncio.ensure_future(
            main()
        )
        loop.run_forever()

    except KeyboardInterrupt:
        print('\nProgram terminated with keyboard interrupt.')

        loop.run_until_complete(
            asyncio.gather(
                rvr.sensor_control.clear(),
                rvr.close()
            )
        )

    finally:
        if loop.is_running():
            loop.close()