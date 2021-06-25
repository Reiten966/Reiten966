# read an analog input and print the value to serial
import board
import time
import analogio
from digitalio import DigitalInOut, Direction

# from digitalio import DigitalInOut, Direction
from simpleio import map_range
import neopixel

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.1)

# declare analog input object
analog_in = analogio.AnalogIn(board.A1)

hallTrigger = DigitalInOut(board.A2)

hallTrigger.direction = Direction.INPUT

clear = (0, 0, 0)
color = (0, 0, 0)
pixels.fill(color)

# a smoothed value for our smooth function
smooth_val = analog_in.value

# make a function to do a weighted average
# def weightedSmooth(in_val, weight):
# weight float between 0.0 and 1.0
# in_value is the current reading of a shaky signal
# reference smooth_val as a global variable
# global smooth_val
# apply weight to in_val and apply reimaining weight to the output
# smooth_val = weight * in_val + ((1-weight) *smooth_val)
# return the new value
# return smooth_val


# repeat
while True:

    # gather input
    reading = analog_in.value

    # do calculation: scale 16-bit reading to 8-bit value

    # scaled_val = weightedSmooth(reading, 0.1)

    scaled_val = map_range(reading, 38000, 51000, 0, 150)

    scaled_val = int(scaled_val)

    print((reading, scaled_val, hallTrigger.value))

    if hallTrigger.value == True:
        pixels.fill(clear)
    else:
        color = (scaled_val, 0, 255)
        pixels.fill(color)
    
    
    # print output

    # sleep to prevent buffer overrun

    time.sleep(0.05)
