
import sys
from PyQt6.QtWidgets import QStyle, QApplication, QTextEdit, QMainWindow, QHBoxLayout, QWidget, QPushButton, QVBoxLayout, QFileDialog, QMessageBox
from PyQt6.QtGui import QAction, QKeySequence
import PyQt6.QtCore as qtc

class MainWindow(QMainWindow):
    def __init__(self, parent_app):
        self.app = parent_app
        super().__init__()
        self.setWindowTitle("Mr Lomax's Menu Test")

        # # Create the menu
        open_action = QAction('Open', self)
        open_action.setShortcut(QKeySequence('Ctrl+O'))
        open_action.triggered.connect(self.open_text)
        save_action = QAction('Save', self)
        save_action.setShortcut('Ctrl+S')
        save_action.triggered.connect(self.save_text)

        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)
        file_menu.addSeparator()
        file_menu.addAction("Exit", self.quit)
        edit_menu = menubar.addMenu("Edit")
        edit_menu.addAction("Copy", self.open_text)



        main_layout = QVBoxLayout()
        #main_layout.addWidget(self.txt_main_text)
        #main_layout.addLayout(button_layout)

        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)
        self.show()

    def save_text(self):
        pass

    def open_text(self):
        pass

    def quit(self):
        dlg = QMessageBox.warning(self, "Quit?", "Are you sure", QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        print(dlg)
        if dlg == QMessageBox.StandardButton.Ok:
            self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow(app)
    app.exec()
