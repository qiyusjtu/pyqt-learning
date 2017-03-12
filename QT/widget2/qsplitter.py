#!/usr/bin/env python
# -*- coding: utf-8 -*-
# YuQi created
__mtime__ = '2017/3/12'
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# YuQi created
__mtime__ = '2017/3/12'

import sys
from PyQt4 import QtGui,QtCore


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        hbox = QtGui.QHBoxLayout(self)
        topleft = QtGui.QFrame(self)
        # 使用带样式的框架
        topleft.setFrameShape(QtGui.QFrame.StyledPanel)

        topright = QtGui.QFrame(self)
        # 使用带样式的框架
        topright.setFrameShape(QtGui.QFrame.StyledPanel)

        bottom = QtGui.QFrame(self)
        # 使用带样式的框架
        bottom.setFrameShape(QtGui.QFrame.StyledPanel)

        splitter1 = QtGui.QSplitter(QtCore.Qt.Horizontal)
        splitter1.addWidget(topleft)
        splitter1.addWidget(topright)

        splitter2 = QtGui.QSplitter(QtCore.Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        hbox.addWidget(splitter2)
        self.setLayout(hbox)

        self.setWindowTitle('Splitter')
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("Cleanlooks"))

        self.setGeometry(250,200,350,250)
def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())

if __name__ =='__main__':
    main()
