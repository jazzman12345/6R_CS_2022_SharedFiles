from PyQt6.QtWidgets import QApplication, QVBoxLayout, QWidget, QLabel, QComboBox, QCheckBox, QLineEdit, QRadioButton, QSlider, QPushButton, QMainWindow
from PyQt6.QtCore import Qt


# Subclass QMainWindow to customise your application's main window
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.setWindowTitle("My Awesome App")

        layout = QVBoxLayout()

        layout.addWidget(QLabel("Widget Demo"))

        self.combo = QComboBox()
        self.combo.addItems(["One", "Two", "Three", "Four"])
        layout.addWidget(self.combo)

        layout.addWidget(QCheckBox("Choose this"))
        layout.addWidget(QCheckBox("and this?"))

        layout.addWidget(QLineEdit("Type here"))

        layout.addWidget(QRadioButton("This one?"))
        layout.addWidget(QRadioButton("Or this one?"))

        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setValue(80)
        layout.addWidget(self.slider)

        layout.addWidget(QPushButton("Ok"))
        layout.addWidget(QPushButton("Cancel"))
        
        widget = QWidget()
        widget.setLayout(layout)
        
        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)


# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication([])

window = MainWindow()
window.show() # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec()


# Your application won't reach here until you exit and the event 
# loop has stopped.
