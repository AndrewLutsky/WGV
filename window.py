from PyQt5 import QtWidgets

import sys

def oFile():
    print("What file would you like to open?")
class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Whole Genome Viewer")
        self.setGeometry(0,0,1920,1080)
        #Open File Button
        ofile = QtWidgets.QPushButton(self)
        ofile.setText("Open File")
        ofile.clicked.connect(oFile)        

        #shows main window
        self.show()
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    
    app.exec()

class oFileWin(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Open File")




