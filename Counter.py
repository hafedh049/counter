from PyQt5 import (QtGui,QtWidgets)
from sys import argv

class Counter(QtWidgets.QWidget):
    def __init__(self):
        super(Counter, self).__init__()
        boring_list = ["setFixedSize(800,600)","setWindowTitle('Counter')","setStyleSheet('background-color : black')"
        ,"setWindowIcon(QtGui.QIcon('3.jpg'))","label = QtWidgets.QLabel(self)","label.setFixedSize(800,300)",
        'tex = QtWidgets.QLineEdit("",self.label)','tex.setStyleSheet("color:gray;border:3px groove crimson;\
        border-radius:25px;padding:5px;font-size:13px")'
        ,'tex.resize(800,150)','tex.textChanged.connect(self.onPressed1)','tex.textChanged.connect(self.onPressed2)',
        'c1 = QtWidgets.QLabel(12*" " + "Number Of Characters = 0",self)','c1.resize(300,50)'
            ,'c1.move(self.width()//2 - 150,self.height()//2)'
        ,'c1.setStyleSheet("color:orange;background-color:transparent;border:3px groove cyan;border-right-color:black;\
        border-radius:25px;padding:5px;font-size:15px;font-family: Georgia, serif;")'
            ,'c2 = QtWidgets.QLabel(12*" " + "Number Of Words = 0", self)',
        'c2.setStyleSheet("color:magenta;background-color:transparent;border:3px groove cyan;border-right-color:black;\
        border-radius:25px;padding:5px;font-size:15px;font-family: Georgia, serif;")','c2.resize(300,50)',
        'c2.move(self.width()//2 - 150, self.height()//2 + self.c1.height()*2)']

        for _ in boring_list:
            exec(f'self.{_}')

    def onPressed1(self):
        self.c1.setText(12*" " + "Number Of Characters = " + str(len(self.tex.text())))

    def onPressed2(self):
        x = self.tex.text()
        if x:
            while "  " in x: x = x.replace("  "," ")
            self.c2.setText(12*" " + "Number Of Words = " + str(x.replace("  "," ").strip().count(" ") + 1))
        else:
            self.c2.setText(12 * " " + "Number Of Words = 0")

if __name__ == '__main__':
    MyApp = QtWidgets.QApplication(argv)
    Count = Counter()
    Count.show()
    MyApp.exec_()