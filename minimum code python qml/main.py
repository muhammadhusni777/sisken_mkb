######  PROGRAM MEMANGGIL WINDOWS PYQT5 ##########################

####### memanggil library PyQt5 ##################################
#----------------------------------------------------------------#
from PyQt5.QtCore import * 
from PyQt5.QtGui import * 
from PyQt5.QtQml import * 
from PyQt5.QtWidgets import *
from PyQt5.QtQuick import *  
import sys
#----------------------------------------------------------------#

text = "hello world"
########## mengisi class table dengan instruksi pyqt5#############
#----------------------------------------------------------------#
class table(QObject):    
    def __init__(self, parent = None):
        super().__init__(parent)
        self.app = QApplication(sys.argv)
        self.engine = QQmlApplicationEngine(self)
        self.engine.rootContext().setContextProperty("backend", self)    
        self.engine.load(QUrl("main.qml"))
        sys.exit(self.app.exec_())
        
    @pyqtSlot(str)
    def button(self, message):
        global button_status
        print(message)
        button_status = message
        
    @pyqtSlot(result=str)
    def text(self):  return text
        
#----------------------------------------------------------------#

########## memanggil class table di mainloop######################
#----------------------------------------------------------------#    
if __name__ == "__main__":
    main = table()
    
#----------------------------------------------------------------#