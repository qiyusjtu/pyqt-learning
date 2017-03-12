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
        self.label = QtGui.QLabel(self)
        edit = QtGui.QLineEdit(self)
        edit.move(60,100)
        self.label.move(60,40)
        self.connect(edit,QtCore.SIGNAL('textChanged(QString)'),self.onChanged)

        self.setWindowTitle('QLineText')
        self.setGeometry(250,200,350,250)

    # text接收信号传来的参数
    def onChanged(self,text):
        self.label.setText(text)
        # 调整标签长度为字符串长度
        self.label.adjustSize()
app = QtGui.QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())
