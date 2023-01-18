from PyQt6.QtWidgets import QVBoxLayout, QLineEdit, QPushButton, QMainWindow, QWidget, QApplication

# Subclass QMainWindow to customise your application's main window
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Signal Demo")
        self.resize(400, 10)
        layout = QVBoxLayout()

        # Create some widgets
        self.name_edit = QLineEdit("Enter your name")
        self.ok_btn = QPushButton("Ok")
        self.cancel_btn = QPushButton("Cancel")

        # Add them to the layout
        layout.addWidget(self.name_edit)
        layout.addWidget(self.ok_btn)
        layout.addWidget(self.cancel_btn)

        # Slot functions within __init__ 
        def ok_clicked():
            print("Ok")

        def text_changed_function(text):
            print(f"Inside __init__: {text}")

        # Connect the signals
        self.ok_btn.clicked.connect(ok_clicked)
        self.cancel_btn.clicked.connect(self.cancel_clicked)

        self.name_edit.textEdited.connect(text_changed_function)
        self.name_edit.textEdited.connect(self.text_changed_method)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

    # Slot methods
    def cancel_clicked(self):
        print("Cancel")

    def text_changed_method(self, text):
        print(f"Method: {text}")



app = QApplication([])

window = MainWindow()
window.show()

app.exec()
