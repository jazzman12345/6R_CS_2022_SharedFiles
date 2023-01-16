from PyQt6.QtWidgets import QApplication, QVBoxLayout, QWidget, QLabel, QMainWindow
from PyQt6.QtCore import Qt



# Subclass QMainWindow to customise your application's main window
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Template Window")

        layout = QVBoxLayout()
        self.label = QLabel("Demo")
        layout.addWidget(self.label)
        
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
window.show()

# Start the event loop.
app.exec()


# Your application won't reach here until you exit and the event 
# loop has stopped.
