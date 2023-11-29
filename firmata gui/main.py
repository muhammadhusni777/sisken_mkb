######  PROGRAM MEMANGGIL WINDOWS PYQT5 ##########################
######    WRITTEN BY : MUHAMMAD HUSNI   ##########################
######      FOR EDUCATIONAL PURPOSE     ##########################
##################################################################



####### memanggil library PyQt5 ##################################
#----------------------------------------------------------------#
from PyQt5.QtCore import * 
from PyQt5.QtGui import * 
from PyQt5.QtQml import * 
from PyQt5.QtWidgets import *
from PyQt5.QtQuick import *  
import sys
import time

from pyfirmata import Arduino, util
import pyfirmata
#----------------------------------------------------------------#


##################################################################
#----------------deklarasi variabel------------------------------#
analog = 110
input1_color = "#df1c39"
input2_color = "#df1c39"

button1_status = "0"
button2_status = "0"
button3_status = "0"

analog_output = "0"


##################################################################
#----------------mengaktifkan komunikasi serial------------------#
import sys
import serial
import threading

serial_data = ""

transmit_time = 0
transmit_time_prev = 0

data_send = ""

print ("select your arduino port:")

def serial_ports():
    
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result
print(str(serial_ports()))

port = input("write port : ")


board = pyfirmata.Arduino(port)

analog_pin = board.get_pin('a:0:i')
led1 = board.get_pin('d:12:o')
led2 = board.get_pin('d:11:o')
led3 = board.get_pin('d:6:o')

pwmpin = board.get_pin('d:3:p') 

button1 = board.get_pin('d:5:i')
button2 = board.get_pin('d:4:i')

print("Communication Successfully started")
it = util.Iterator(board)
it.start()

            

########## mengisi class table dengan instruksi pyqt5#############
#----------------------------------------------------------------#
class table(QObject):
    global analog
    def __init__(self, parent = None):
        super().__init__(parent)
        self.app = QApplication(sys.argv)
        self.engine = QQmlApplicationEngine(self)
        self.engine.rootContext().setContextProperty("backend", self)    
        self.engine.load(QUrl("main.qml"))
        sys.exit(self.app.exec_())
    
    
    
    #####################TOMBOL QML KE PYTHON###################
    @pyqtSlot(str)
    def button1(self, message):
        global button1_status
        print(message)
        button1_status = message
        led1.write(int(button1_status))
        
        

        
    @pyqtSlot(str)
    def button2(self, message):
        global button2_status
        print(message)
        button2_status = message
        led2.write(int(button2_status))
        
        
        
    @pyqtSlot(str)
    def button3(self, message):
        print(message)
        global button3_status
        print(message)
        button3_status = message
        led3.write(int(button3_status))
        
    #####################SLIDER QML KE PYTHON###################
    @pyqtSlot(str)
    def analog_output(self, message):
        global analog_output
        analog_output=message
        
    
    ######################KIRIM DATA ANALOG KE GAUGE##############
    @pyqtSlot(result=float)
    def get_analog(self):  return round(analog,0)
    
    ####################KIRIM DATA WARNA STATUS BUTTON#############
    @pyqtSlot(result=str)
    def get_input1_color(self):  return input1_color
    
    @pyqtSlot(result=str)
    def get_input2_color(self):  return input2_color

#----------------------------------------------------------------#
###############################MEMBACA DATA SERIAL##################
def serial_read(num):
    global analog
    while True:
        pwmpin.write(float(float(analog_output)/100))
        
        if analog_pin.read() is not None:
            analog = float(analog_pin.read()) * 100    
        
        print(analog)
        
        
        
    '''
    global ser_bytes
    global decoded_bytes
    global serial_data
    global analog
    global data
    global input1_color
    global input2_color
    
    while True:
        try:
            ser_bytes = ser.readline()
            serial_data = (ser_bytes.decode('utf-8')[:-2])
            
            print(serial_data)
                
        except:
            serial_data = serial_data
            
        data = serial_data.split(":")
        
        analog = int(data[0])
        #print(analog)
        if (data[1] == "0"):
            input1_color = "#df1c39"
        else:
            input1_color = "#04f8fa"
            
        if (data[2] == "0"):
            input2_color = "#df1c39"
        else:
            input2_color = "#04f8fa"
            
    ''' 
#----------------------------------------------------------------#



########## memanggil class table di mainloop######################
#----------------------------------------------------------------#    
if __name__ == "__main__":
    
    
    
    t1 = threading.Thread(target=serial_read, args=(10,))
    t1.start()
    
    #t2 = threading.Thread(target=serial_write, args=(10,))
    #t2.start()
    
    main = table()
    
    
#----------------------------------------------------------------#