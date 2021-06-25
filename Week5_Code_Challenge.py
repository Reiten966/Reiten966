# read an analog input and print the value to serial
import board
import time
import analogio
import touchio

# from digitalio import DigitalInOut, Direction
from simpleio import map_range
import neopixel


touchPin1 = touchio.TouchIn(board.A1)
touchPin2 = touchio.TouchIn(board.A2)
touchPin3 = touchio.TouchIn(board.A3)
touchPin4 = touchio.TouchIn(board.A4)
touchPin5 = touchio.TouchIn(board.A5)
touchPin6 = touchio.TouchIn(board.A6)
touchPin7 = touchio.TouchIn(board.TX)

touchPins = [
    touchPin1,
    touchPin2,
    touchPin3,
    touchPin4,
    touchPin5,
    touchPin6,
    touchPin7,
]

touchVals = [False, False, False, False, False, False, False]

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.1)


# red values
red = 20
redStep = 20

# blue values
blue = 20
blueStep = 20

# green values
green = 20
greenStep = 20

color = (red, green, blue)
CLEAR = (0, 0, 0)

# declare analog input object
ledMode = 0
buttonPre = False



# repeat
while True:

    for x in range(7):
        touchVals[x] = touchPins[x].value
        print(touchVals, buttonPre, ledMode, red)
        # see if the button has changed
    
    if touchVals[0] != buttonPre:
            # reset the previous value
            buttonPre = touchVals[0]
            if touchVals[0] == True:
                ledMode += 1
                if ledMode > 1:
                    ledMode = 0
    if ledMode == 1:
        pixels.fill(color)
    else:
        pixels.fill(CLEAR)
    
    if touchVals[1] == True:
        if red < 235:
            red = red + redStep
            color = (red, green, blue)

        elif red > 255:
            red = 255
        time.sleep(0.01)
    if touchVals[2] == True:
        if red > 20:
            red = red - redStep
            color = (red, green, blue)

        elif red < 20:
            red = 20
        time.sleep(0.01)

    if touchVals[3] == True:
        if green < 235:
            green = green + greenStep
            color = (red, green, blue)

        elif green > 255:
            green = 255
        time.sleep(0.01)
    if touchVals[4] == True:
        if green > 20:
            green = green - greenStep
            color = (red, green, blue)

        elif green < 20:
            green = 20
        time.sleep(0.01)

    if touchVals[5] == True:
        if blue < 235:
            blue = blue + blueStep
            color = (red, green, blue)

        elif blue > 255:
            blue = 255
        time.sleep(0.01)
    if touchVals[6] == True:
        if blue > 20:
            blue = blue - blueStep
            color = (red, green, blue)
        elif blue > 255:
            blue = 255
        time.sleep(0.01)
    
    # print(touchVals)
    """
    if touchVal is True:
        pixels.fill(COLOR)
    else:
        pixels.fill(CLEAR)
    """

    time.sleep(0.05)
