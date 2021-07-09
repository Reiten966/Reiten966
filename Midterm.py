# read an analog input and print the value to serial
import board
import time
import analogio
from digitalio import DigitalInOut, Direction
from simpleio import map_range
import neopixel

# pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=.1)

# declare analog input object
analog_in = analogio.AnalogIn(board.A1)

printer_state = DigitalInOut(board.A2)
printer_state.direction = Direction.INPUT

printer_communication = DigitalInOut(board.A3)
printer_communication.direction = Direction.OUTPUT
# color = (0, 0, 0)
# pixels.fill(color)

#make a function to do a weighted average
#def weightedSmooth(in_val, weight):
# weight float between 0.0 and 1.0
# in_value is the current reading of a shaky signal
#reference smooth_val as a global variable
#global smooth_val
#apply weight to in_val and apply reimaining weight to the output
#smooth_val = weight * in_val + ((1-weight) *smooth_val)
# return the new value
#return smooth_val


#list of average
diameter_List = []

#average diamter
deviation_List = []

#average
Average_diameter = 0
Average_deviation = 0

target_diameter = 1.75

accl_time = time.monotonic()

accl_int = 0.25

red1 = 0
green1 = 0
blue1 = 0
color1 = (0, 0, 0)

red2 = 0
green2 = 0
blue2 = 0

color2 = (0, 0, 0)

timeInterval = 1

# repeat
while True:
    if time.monotonic() >= accl_time:
        # resets the next time to read the accelerometer
        accl_time += accl_int

        # gather input
        reading = analog_in.value

        # do calculation: scale 16-bit reading to 8-bit value

        #scaled_val = map_range(reading, 43000, 50000, 0, 255)

        scaled_val = map_range(reading, 43960, 51000, 1.0, 3.0)

        # check if the filament is inserted
        if scaled_val > 1.6 and < 1.9:
            if len(diameter_List) < 20:
                #kick the last value out of the list
                diameter_List.append(scaled_val2)
            else:
                diameter_List.pop(0)
                #add to the list
                diameter_List.append(scaled_val2)
                #check if the # of items on the list is larger than the capacity

            if len(diameter_List) > 0:
                Average_diameter = sum(diameter_List)/len(diameter_List)

            # calculating the deviation from the 1.75 target
            deviation = abs(target_diameter - scaled_val)

            if len(deviation_List) < 20:
                #kick the last value out of the list
                diameter_List.append(deviation)
            else:
                diameter_List.pop(0)
                #add to the list
                diameter_List.append(deviation)

            if len(deviation_List) > 0:
                Average_deviation = sum(deviation_List)/len(deviation_List)

        # Filament is not inside, check if printer is running
        else:
            if printer_state.value == True:
            # send signal to pause the print
                printer_communication.value = True

            diameter_List = []
            deviation_List = []
            

            
        #Calculating the deviation of average from the target



        # print output
        print("The average is", Average_diameter)
        # show a local diameter deviation
        off_from_target = abs(target_diameter - Average_diameter)

        red1 = map_range(off_from_target, 0, 0.2, 0, 255)

        color1 = (red1, green1, blue1)

        pixel[0] = color1

        print("The deviation is", Average_deviation)
        # show a global diameter deviation
        red2 = map_range(Average_deviation, 0, 0.2, 0, 255)

        color2 = (red2, green2, blue2)

        pixel[1] = color2




    # sleep to prevent buffer overrun
