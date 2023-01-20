import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, \
    QPushButton, QVBoxLayout, QLineEdit, QColorDialog, QMessageBox, QFileDialog
import PyQt6.QtCore as qtc 

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Signals and Slots")

        layout = QVBoxLayout()

        # Create a button
        ok_btn = QPushButton("Ok")
        ok_btn.clicked.connect(self.ok_button_click)
        layout.addWidget(ok_btn)

        # Create another button
        quit_btn = QPushButton("Quit")
        quit_btn.clicked.connect(self.quit)
        layout.addWidget(quit_btn)

        # Create another button
        colour_btn = QPushButton("Colour")
        colour_btn.clicked.connect(self.colour_button_click)
        layout.addWidget(colour_btn)

        # Create another button
        open_btn = QPushButton("Open")
        open_btn.clicked.connect(self.open_btn_click)
        layout.addWidget(open_btn)

        # Create another button
        save_btn = QPushButton("Save")
        save_btn.clicked.connect(self.save_btn_click)
        layout.addWidget(save_btn)

        # Create the windows central widget
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def ok_button_click(self):
        pass

    def colour_button_click(self):
        pass

    def open_btn_click(self):
        pass

    def save_btn_click(self):
        pass

    def quit(self):
        pass
    



app = QApplication(sys.argv)

window = MainWindow(app)
window.show()

app.exec()
