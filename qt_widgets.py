from PyQt6 import QtWidgets as qtw
from PyQt6.QtCore import *
from PyQt6.QtGui import *


# Subclass QMainWindow to customise your application's main window
class MainWindow(qtw.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.setWindowTitle("My Awesome App")

        layout = qtw.QVBoxLayout()

        layout.addWidget(qtw.QLabel("Widget Demo"))

        self.combo = qtw.QComboBox()
        self.combo.addItems(["One", "Two", "Three", "Four"])
        layout.addWidget(self.combo)

        layout.addWidget(qtw.QCheckBox("Choose this"))
        layout.addWidget(qtw.QCheckBox("and this?"))

        layout.addWidget(qtw.QLineEdit("Type here"))

        layout.addWidget(qtw.QRadioButton("This one?"))
        layout.addWidget(qtw.QRadioButton("Or this one?"))

        self.slider = qtw.QSlider(Qt.Orientation.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setValue(80)
        layout.addWidget(self.slider)

        layout.addWidget(qtw.QPushButton("Ok"))
        layout.addWidget(qtw.QPushButton("Cancel"))
        
        widget = qtw.QWidget()
        widget.setLayout(layout)
        
        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)


# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = qtw.QApplication([])

window = MainWindow()
window.show() # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec()


# Your application won't reach here until you exit and the event 
# loop has stopped.
