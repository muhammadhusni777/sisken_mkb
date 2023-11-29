from pyfirmata import Arduino, util
import pyfirmata
import time


if __name__ == '__main__':
    board = pyfirmata.Arduino('COM1')
    pin = board.get_pin('a:0:i')
    print("Communication Successfully started")
    it = util.Iterator(board)
    it.start()
    
    while True:
        print(pin.read())