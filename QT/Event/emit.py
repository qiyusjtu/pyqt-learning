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
        self.connect(self,QtCore.SIGNAL('closeEmitApp()'),QtCore.SLOT('close()'))
        self.setWindowTitle('')
        self.resize(250,300)
    def mousePressEvent(self, QMouseEvent):
        self.emit(QtCore.SIGNAL('closeEmitApp()'))
app = QtGui.QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())
