import sys
from PyQt5.QtWidgets import QApplication,

app = QApplication(sys.argv)
win = QWidget()
win.setWindowTitle("PyQt5 GUI")
win.show()

sys.exit(app.exec_())
