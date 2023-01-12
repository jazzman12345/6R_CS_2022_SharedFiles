import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QLineEdit, QWidget, QLayout, QHBoxLayout
from PyQt5.QtCore import Qt



# Subclass QMainWindow to customise your application's main window
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My Awesome App")

        widget = QLabel("Blah")

        widget.setAlignment(Qt.AlignCenter)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
