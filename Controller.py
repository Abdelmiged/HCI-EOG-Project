from PyQt5 import QtWidgets, QtGui, QtCore, Qt
import TestCases
from MainWindow import MainWindow
from PyQt5.Qt import Qt
import sys

class Controller:
    default_btn_style = """QPushButton{
                            background-color: black;
                            color: white;
                        }
                        
                        QPushButton:hover{
                            background-color: blue;
                        }
                        QPushButton:pressed{
                            background-color: red;
                        }"""
    def __init__(self):
        # self.app = QtWidgets.QApplication(sys.argv)
        self.map = {
            'current': '',
            'left': {
                'current': '7',
                'up': {
                    'current': '6',
                },
                'down': {
                    'current': '8',
                },
                'left': {
                    'current': 'x',
                }
            },
            'right': {
                'current': '4',
                'right': {
                    'current': '-',
                },
                'down': {
                    'current': '5',
                },
                'up': {
                    'current': '3',
                }
            },
            'up': {
                'current': '1',
                'right': {
                    'current': '2',
                },
                'left': {
                    'current': '0',
                },
                'up': {
                    'current': '+',
                }
            },
            'down': {
                'current': 'e',
                'right': {
                    'current': 'c',
                },
                'left': {
                    'current': '9',
                },
                'down': {
                    'current': '/',
                }
            }
        }
        self.current_btn = None
        self.curr_map = self.map
        # self.calc_flag = False
        self.equation = []
        self.ui = MainWindow()
        self.ui.lineEdit.setReadOnly(True)

        self.ui.op_e_btn.clicked.connect(lambda: self.ui.win.close())
        self.ui.op_c_btn.clicked.connect(lambda: self.ui.lineEdit.clear())

        self.ui.num_0_btn.clicked.connect(lambda: self.calc('0'))
        self.ui.num_1_btn.clicked.connect(lambda: self.calc('1'))
        self.ui.num_2_btn.clicked.connect(lambda: self.calc('2'))
        self.ui.num_3_btn.clicked.connect(lambda: self.calc('3'))
        self.ui.num_4_btn.clicked.connect(lambda: self.calc('4'))
        self.ui.num_5_btn.clicked.connect(lambda: self.calc('5'))
        self.ui.num_6_btn.clicked.connect(lambda: self.calc('6'))
        self.ui.num_7_btn.clicked.connect(lambda: self.calc('7'))
        self.ui.num_8_btn.clicked.connect(lambda: self.calc('8'))
        self.ui.num_9_btn.clicked.connect(lambda: self.calc('9'))

        self.ui.op_plus_btn.clicked.connect(lambda: self.calc('+'))
        self.ui.op_minus_btn.clicked.connect(lambda: self.calc('-'))
        self.ui.op_divide_btn.clicked.connect(lambda: self.calc('/'))
        self.ui.op_mult_btn.clicked.connect(lambda: self.calc('x'))

        # self.ui.lineEdit.textChanged.connect(lambda: self.calc())

    def action(self, direction: str):
        if self.current_btn is not None:
            self.current_btn.setStyleSheet(Controller.default_btn_style)
        if direction == 'blink':
            self.goto_btn(self.curr_map['current'])
            self.current_btn.click()
            self.curr_map = self.map
        else:
            if direction in self.curr_map.keys():
                self.curr_map = self.curr_map[direction]
                self.goto_btn(self.curr_map['current'])
                self.current_btn.setStyleSheet('background-color: blue;')
            else:
                print('Invalid direction')

    def calc(self, char):
        # print(char)
        if self.ui.lineEdit.text() == '':
            if int(char) in range(0, 10):
                self.ui.lineEdit.setText(self.ui.lineEdit.text() + char)
            else:
                print('Number required')
        elif self.ui.lineEdit.text()[-1] in ['+', '-', '/', 'x']:
            if int(char) in range(0, 10):
                # self.ui.lineEdit.setText(self.ui.lineEdit.text() + char)
                n1 = int(self.ui.lineEdit.text()[0:-1])
                n2 = int(char)
                # self.ui.lineEdit.clear()
                # equation = self.ui.lineEdit.text()
                if self.ui.lineEdit.text()[-1] == '+':
                    self.ui.lineEdit.setText(str(int(n1 + n2)))
                elif self.ui.lineEdit.text()[-1] == '-':
                    self.ui.lineEdit.setText(str(int(n1 - n2)))
                elif self.ui.lineEdit.text()[-1] == '/':
                    self.ui.lineEdit.setText(str(int(n1 / n2)))
                elif self.ui.lineEdit.text()[-1] == 'x':
                    self.ui.lineEdit.setText(str(int(n1 * n2)))
            else:
                print("number Required")
        elif int(self.ui.lineEdit.text()[-1]) in range(0, 10):
            if char in ['+', '-', '/', 'x']:
                self.ui.lineEdit.setText(self.ui.lineEdit.text() + char)
            else:
                print('Operation Required')

    def goto_btn(self, btn: str):
        match btn:
            case '0':
                self.current_btn = self.ui.num_0_btn
            case '1':
                self.current_btn = self.ui.num_1_btn
            case '2':
                self.current_btn = self.ui.num_2_btn
            case '3':
                self.current_btn = self.ui.num_3_btn
            case '4':
                self.current_btn = self.ui.num_4_btn
            case '5':
                self.current_btn = self.ui.num_5_btn
            case '6':
                self.current_btn = self.ui.num_6_btn
            case '7':
                self.current_btn = self.ui.num_7_btn
            case '8':
                self.current_btn = self.ui.num_8_btn
            case '9':
                self.current_btn = self.ui.num_9_btn
            case '+':
                self.current_btn = self.ui.op_plus_btn
            case '-':
                self.current_btn = self.ui.op_minus_btn
            case 'x':
                self.current_btn = self.ui.op_mult_btn
            case '/':
                self.current_btn = self.ui.op_divide_btn
            case 'e':
                self.current_btn = self.ui.op_e_btn
            case 'c':
                self.current_btn = self.ui.op_c_btn

    # def start(self):
    #     self.ui.win.show()
    #     sys.exit(self.app.exec_())

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.ui.win.show()
    dirs = TestCases.TestCase1()
    for dir in dirs:
        controller.action(dir)
    sys.exit(app.exec_())