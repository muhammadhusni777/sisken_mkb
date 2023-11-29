#!/usr/bin/env python3
from pyfirmata import Arduino, util
from time import sleep

board = Arduino('COM1') # Change to your port
lenPin = board.get_pin('d:6:p') # PWM Pin
print("Starting to output PWM signal")
while True:
    for i in range(0, 101, 4):
        lenPin.write(i/100)
        sleep(0.05)
    sleep(1)
    for i in range(100, -1, -4):
        lenPin.write(i/100)
        sleep(0.05)
    sleep(1)