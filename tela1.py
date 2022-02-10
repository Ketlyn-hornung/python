#tela1.py
#pip install pyqt5

from PyQt5.QtWidegets import *

app= QApplication([])

layout = QVBoxLayout()
layout.addWidget(QPushButton('Acima'))
layout.addWidget(QPushButton('Abaixo'))

Window= QWidget()
Window.setLayout(layout)
Window.show()

app.exec_()
