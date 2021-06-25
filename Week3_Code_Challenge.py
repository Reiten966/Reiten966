# read an analog input and print the value to serial
import board
import time
import analogio

# from digitalio import DigitalInOut, Direction
from simpleio import map_range
import neopixel

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.1)

# declare analog input object
analog_in = analogio.AnalogIn(board.A1)

analog_in2 = analogio.AnalogIn(board.A2)

Red = 255
Green = 255
Blue = 0

color = (Red, Green, Blue)

pixels.fill(color)



# repeat
while True:

    # gather input
    reading = analog_in.value
    reading2 = analog_in2.value
    # do calculation: scale 16-bit reading to 8-bit value

    scaled_val = map_range(reading, 18000, 51000, 0, 255)
    scaled_val2 = map_range(reading2, 0, 65535, 0, 1.0)
    scaled_val = int(scaled_val)

    print(scaled_val2, reading)

    color = (Red - scaled_val, 0, scaled_val)

    pixels.brightness = scaled_val2

    pixels.fill(color)
    # print output

    # sleep to prevent buffer overrun

    time.sleep(0.05)
