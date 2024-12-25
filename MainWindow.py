from Ui_MainWindow import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

class MainWindow(Ui_MainWindow):
    def __init__(self):
        self.win = QtWidgets.QMainWindow()
        self.setupUi(self.win)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.win.show()
    sys.exit(app.exec_())
