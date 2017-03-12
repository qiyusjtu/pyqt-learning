import sys
from PyQt4 import QtGui

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example,self).__init__()

        self.initUI()
    def initUI(self):
        label1 = QtGui.QLabel('QYCode',self)
        label1.move(15,10)

        label2 = QtGui.QLabel('tutorial',self)
        label2.move(35,40)

        self.setWindowTitle('Absolute')
        self.resize(250,150)

app = QtGui.QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())
