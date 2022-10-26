from PyQt5 import QtWidgets

import sys

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Whole Genome Viewer")
        l = QtWidgets.QLabel("Visualizer")
        l.setMargin(100)
        self.setCentralWidget(l)
        self.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    app.exec()
