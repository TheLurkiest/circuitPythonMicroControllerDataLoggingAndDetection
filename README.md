# circuitPythonMicroControllerDataLoggingAndDetection


RANDOM USEFUL INFO:
-------------------
A) this is designed to work with the circuitplayground express... I'm not sure how well it would work with other micro-controllers

B) make sure you have an HC-SR04 ultrasonic sensor hooked up, or you're going to get errors.  You can remove this detection
element from the code if unavailable to you.  It's pretty simple to hook up-- just follow the following steps:
1) A yellow wire connects the pin
marked “Gnd” on our sensor to
ground
2) A white wire supplies 5 volts
from our raspberry Pi, which in
turn is connected to a red wire
which connects to the pin
marked “Vcc” on our ultrasonic
sensor
3) An orange wire connects
GPIO20 to the pin on our sensor
marked “Trig”
4) Finally, in order to ensure that we receive the 3.3V needed to avoid damaging our equipment,
we use a system which incorporates a 2k ohm and a 1k ohm resistor. In between the 2 resistors
a yellow wire is placed, which connects to GPIO21. On one side of this 2 resistor system, a 
purple wire connects to the pin marked “Echo” on our sensor. On the other side, an orange wire
connects us back to ground.

C) Make sure you open up a spreadsheet/excel file before you start recording-- and make sure that you have selected a cell on the
spreadsheet before the recording starts-- otherwise the code will start automatically recording data onto whatever surface is
available

D) flick the center switch on the circuit playground express to toggle data recording/monitoring on/off


