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
        self.label = QtGui.QLabel("Ubuntu",self)

        combo = QtGui.QComboBox(self)
        combo.addItem("Ubuntu")
        combo.addItem("Mandriva")
        combo.addItem("Fedora")
        combo.addItem("Red Hat")
        combo.addItem("Gentoo")

        combo.move(50,50)
        self.label.move(50,150)
        self.connect(combo,QtCore.SIGNAL('activated(QString)'),self.onActivated)


        self.setWindowTitle('QCombox')
        self.setGeometry(600,300,250,300)
    def onActivated(self,text):
        self.label.setText(text)
        self.label.adjustSize()


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())

if __name__ =='__main__':
    main()
