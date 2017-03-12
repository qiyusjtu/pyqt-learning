import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.resize(250,150)
        self.setWindowIcon(QtGui.QIcon('icons/safari.png'))
        self.setWindowTitle('myWindow')

        self.exit = QtGui.QAction(QtGui.QIcon('icons/mail.png'),"Exit",self)
        self.exit.setShortcut('ctrl+Q')
        self.connect(self.exit,QtCore.SIGNAL('triggered()'),QtCore.SLOT('close()'))
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(self.exit)
        menubar = self.menuBar()
        file = menubar.addMenu('&File')
        file.addAction(self.exit)
        textEdit = QtGui.QTextEdit()
        self.setCentralWidget(textEdit)


app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())
