##QtGui组件
    - QIcon 图标管理
    - QLabel 标签
    - QPushButton 按钮
    - QLineEdit 仅有一行的文本编辑框
    - QTextEdit 文本编辑框
    - QLCDNumber lcd数字显示
    - QSlider 滑块
    - QCheckBox 复选框，每段复选框被选中或者清除时都会发射信号`stateChanged()`
    - QProgressBar 进度条
    - QPixMap 是用于显示图像的组件
    - QLineEdit 用于单行文本编辑
#布局
##Absolute布局（不好）
##框布局
>使用QHBoxLayout和QVBoxLayout

两个分别对应于横向布局和纵向布局
```python
    okButton = QtGui.QPushButton("OK")
    cancelButton = QtGui.QPushButton("Cancel")
    hbox = QtGui.QHBoxLayout()
    hbox.addStretch(1)
    hbox.addWidget(okButton)
    hbox.addWidget(cancelButton)

    vbox = QtGui.QVBoxLayout()
    vbox.addStretch(1)
    vbox.addLayout(hbox)

    //设置窗体的总体布局
    self.setLayout(vbox)
```
##网格布局（最常用）
>使用`QGridLayout`

#信号与槽
`connect`方法有四个参数，`sender`是发送信号的对象，`signal`是发射的信号，`receiver`是接收信号的对象，`slot`是对信号反应的方法

#事件
- 使用`sender = self.sender()`可以获取到发送者的信息
- 使用`sender.text()`可以转换为文本
- `QtCore.QObject`继承的对象可以发射信号。如果点击按钮，将产生一个`clicked()`的信号

