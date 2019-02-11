import time
import board


import adafruit_hcsr04

#sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D9, echo_pin=board.D6)
countSonar=0
#while countSonar<100:
    #try:
        #print((sonar.distance,))
        #countSonar=countSonar+1
    #except RuntimeError:
        #print("Retrying!")
#time.sleep(0.1)
#

print("testing stuff 4")

# Circuit Playground Express Data Time/Light Intensity/Temp
# Log data to a spreadsheet on-screen
# Open Spreadsheet beforehand and position to start (A,1)
# Use slide switch to start and stop sensor 
# Time values are seconds since board powered on (relative time)

from digitalio import DigitalInOut, Direction, Pull
import analogio
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
import adafruit_thermistor

from adafruit_circuitplayground.express import cpx

import math
import array


import audiobusio

from adafruit_circuitplayground.express import cpx

#while True:
#    print("testing to see if things work")

cpx.detect_taps = 2

TcountT=0
tapsNow=0
while TcountT<10:
    if cpx.tapped:
        tapsNow=1
        #print("Tapped!")
    else:
        tapsNow=0
        #print("no tap")
    TcountT=TcountT+1


def mean(values):
    return sum(values) / len(values)


def normalized_rms(values):
    minbuf = int(mean(values))
    sum_of_samples = sum(
        float(sample - minbuf) * (sample - minbuf)
        for sample in values
    )

    return math.sqrt(sum_of_samples / len(values))


mic = audiobusio.PDMIn(
    board.MICROPHONE_CLOCK,
    board.MICROPHONE_DATA,
    sample_rate=16000,
    bit_depth=16
)
samples = array.array('H', [0] * 160)
mic.record(samples, len(samples))

mCount=4
while mCount>0:
    mic.record(samples, len(samples))
    magnitude = normalized_rms(samples)
    #print(((magnitude),))
    #time.sleep(0.1)
    mCount=mCount-1



#77777777777777777777777777777777777777777777777777777777777777777777777777777777777777

aCount=0
while aCount<10:
    x, y, z = cpx.acceleration
    #print(x, y, z)
    aCount=aCount+1
    #time.sleep(0.1)
#77777777777777777777777777777777777777777777777777777777777777777777777777777777777777


# Switch to quickly enable/disable

#switch = DigitalInOut(board.SLIDE_SWITCH)
switch = cpx._switch


switch.pull = Pull.UP

# light level
#light = analogio.AnalogIn(board.LIGHT)
light = cpx._light
# temperature
#thermistor = adafruit_thermistor.Thermistor(board.TEMPERATURE, 10000, 10000, 25, 3950)
thermistor = cpx._temp

# Set the keyboard object!
# Sleep for a bit to avoid a race condition on some systems
print("Observation and Theft Prevention Mode Activated!")
time.sleep(3)
if (switch.value == False):
    print("Observation Recording Mode is currently switched ON")
else:
    print("Observation Recording Mode is currently switched OFF")

print("flick the center switch on your microcontroller to toggle this mode on and off")
print("-------------------------------------------------------------------------------")
time.sleep(4)

kbd = Keyboard()
layout = KeyboardLayoutUS(kbd)  # US is only current option...

#led = DigitalInOut(board.D13)   # Set up red LED "D13"
led = cpx._led




led.direction = Direction.OUTPUT











def slow_write(string):   # Typing should not be too fas8t for
    for c in string:      # the computer to be able to accept
        layout.write(c)
        time.sleep(0.2)   # use 1/5 second pause between characters





print("Time\tLight\tTemperature\tSoundMagnitude\tTapsRecorded\tDistance\tTotalTilt")  # Print column headers

print("----\t----\t-----------\t--------------\t------------\t--------\t---------")

if (switch.value == False):
    output = "Time\tLight\tTemperature\tSound Magnitude\tTaps Recorded\tDistance To Detection\tTotal tilt"
    print(output)         # Print to serial monitor
    slow_write(output)    # Print to spreadsheet

    kbd.press(Keycode.DOWN_ARROW)  # Code to go to next row
    time.sleep(0.01)
    kbd.release_all()
    for _ in range(6):
        kbd.press(Keycode.LEFT_ARROW)
        time.sleep(0.015)
        kbd.release_all()
        time.sleep(0.025)  # Wait a bit more for Google Sheets



oldX=111
oldY=111
oldZ=111

while True:
    mic.record(samples, len(samples))
    magnitude = normalized_rms(samples)
    #print("Sound: ",((magnitude),),"\tDistance: ", (sonar.distance,))
    time.sleep(0.1)


    tapsNow=0
    if cpx.tapped:
        tapsNow=1
        print("Tapped!")
    else:
        tapsNow=0
        #print("no tap")



    x, y, z = cpx.acceleration
    if(oldX>100):
        oldX=x
        oldY=y
        oldZ=z

    tiltX=oldX-x
    tiltY=oldY-y
    tiltZ=oldZ-z
    totalTilt=(abs(tiltX) + abs(tiltY) + abs(tiltZ))

    #if(totalTilt>2):
    #    print("x tilt: ",tiltX,"\ty tilt: ",tiltY,"\tz tilt: ",tiltZ)

    if switch.value:    # If the slide switch is on, don't log
        continue
    else:
        print("Monitoring...")
    if (magnitude<99 and tapsNow == 0 and sonar.distance >= 200 and totalTilt < 3):    # If the sound too quiet, don't log unless we detect taps or ultrasonic thing
        continue
    else:
        print("Possible intruder detected!")


    # Turn on the LED to show we're logging
    led.value = True
    temp = thermistor.temperature  # In Celsius



    # if you want Fahrenheit, uncomment the line below
    # temp = temp * 9 / 5 + 32
    # Format data into value 'output'
    light.value=cpx._light.light
    output = "%0.1f\t%d\t%0.1f\t%0.1f\t%d\t%0.1f\t%0.1f" % (time.monotonic(), light.value, temp, magnitude, tapsNow, sonar.distance, totalTilt)
    print(output)         # Print to serial monitor
    slow_write(output)    # Print to spreadsheet

    kbd.press(Keycode.DOWN_ARROW)  # Code to go to next row
    time.sleep(0.01)
    kbd.release_all()
    for _ in range(6):
        kbd.press(Keycode.LEFT_ARROW)
        time.sleep(0.015)
        kbd.release_all()
        time.sleep(0.025)  # Wait a bit more for Google Sheets

    led.value = False
    # Change 0.1 to whatever time you need between readings
    time.sleep(0.1)
