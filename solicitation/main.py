import sys

from PyQt5.QtWidgets import QApplication
from .database import createConnection
from .views import Window

def main ():
    app = QApplication(sys.argv)
    if not createConnection("solicitation_viewer.sqlite"):
        sys.exit(1)
    win = Window()
    win.show()
    sys.exit(app.exec())
    
