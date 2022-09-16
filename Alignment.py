import sys
from PyQt5.QtWidgets import (
    QApplication,
    QDialog,
    QDialogButtonBox,
    QFileDialog
    QFormLayout,
    QLineEdit,
    QVBoxLayout,
    QWidget,
    QHBoxLayout,
    QPushButton
)


app = QApplication([])
window = QWidget()
window.setWindowTitle("QHBoxLayout")
layout = QHBoxLayout()

window.setLayout(layout)
window.show()
sys.exit(app.exec())
