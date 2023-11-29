#!/usr/bin/env python3
from pyfirmata import Arduino, util
import pyfirmata
import time


if __name__ == '__main__':
    board = pyfirmata.Arduino('COM1')
    pin = board.get_pin('d:13:o')
    print("Communication Successfully started")
    it = util.Iterator(board)
    it.start()
    
    while True:
        pin.write(1)
        time.sleep(0.5)
        pin.write(0)
        time.sleep(0.5)
