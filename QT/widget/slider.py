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
        slider = QtGui.QSlider(QtCore.Qt.Horizontal,self)
        slider.setFocusPolicy(QtCore.Qt.NoFocus)

        lcd = QtGui.QLCDNumber(self)
        vbox = QtGui.QVBoxLayout()

        self.connect(slider,QtCore.SIGNAL('valueChanged(int)'),self.changeValue)
        self.connect(slider,QtCore.SIGNAL('valueChanged(int)'),lcd,QtCore.SLOT('display(int)'))

        self.label = QtGui.QLabel(self)
        self.label.setPixmap(QtGui.QPixmap('../icons/photo.png'))

        vbox.addWidget(lcd)
        vbox.addWidget(slider)
        vbox.addWidget(self.label,alignment=QtCore.Qt.AlignCenter)
        self.setLayout(vbox)
        self.setWindowTitle('Slider')
        self.setGeometry(300,300,250,350)
    def changeValue(self,value):
        if value == 0:
            self.label.setPixmap(QtGui.QPixmap('../icons/safari.png'))
        elif value>0 and value <=30:
            self.label.setPixmap(QtGui.QPixmap('../icons/mail.png'))
        else:
            self.label.setPixmap(QtGui.QPixmap('../icons/music.png'))
app = QtGui.QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())
