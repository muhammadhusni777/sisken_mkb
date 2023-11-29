from pyfirmata import Arduino, util
import pyfirmata
import time


if __name__ == '__main__':
    board = pyfirmata.Arduino('COM1')
    potensiometer = board.get_pin('a:0:i')
    led = board.get_pin('d:12:o')
    button = board.get_pin('d:5:i')
    lenPin = board.get_pin('d:6:p') 
    
    
    print("Communication Successfully started")
    it = util.Iterator(board)
    it.start()
    
    while True:
        lenPin.write(0.5)
        time.sleep(0.5)
        lenPin.write(0.0)
        pin.write(1)
        time.sleep(0.5)
        pin.write(0)
        time.sleep(0.5)
        print(potensiometer.read(), pin.read())