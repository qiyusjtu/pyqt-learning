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
        pixmap = QtGui.QPixmap('../icons/music.png')
        label1 = QtGui.QLabel(self)
        label1.setPixmap(pixmap)

        hbox.addWidget(label1,alignment=QtCore.Qt.AlignCenter)
        self.setLayout(hbox)

        self.setWindowTitle('Haha')
        self.resize(250,300)

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())

if __name__ =='__main__':
    main()
