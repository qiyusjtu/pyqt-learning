#!/usr/bin/env python
# -*- coding: utf-8 -*-
# YuQi created
__mtime__ = '2017/3/12'

from PyQt4 import QtGui,QtCore
import sys

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example,self).__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('CheckBox')

        self.cb = QtGui.QCheckBox('Show title',self)
        self.cb.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cb.move(10,10)
        self.cb.toggle()
        self.connect(self.cb,QtCore.SIGNAL('stateChanged(int)'),self.changeTitle)
    def changeTitle(self,value):
        if self.cb.isChecked():
            self.setWindowTitle('CheckBox')
        else:
            self.setWindowTitle('')

if __name__ =='__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
