import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QMenuBar, QStatusBar
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import QPointF, QRect, QMetaObject, QCoreApplication
from PyQt6 import uic
import io
import random


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1119, 896)
        self.centralwidget = QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QRect(260, 300, 501, 151))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 1119, 19))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Создать круг"))


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)
        self.x = 1120
        self.y = 900
        self.reg = 0

    def run(self):
        self.reg = 1
        self.update()

    def paintEvent(self, event):
        if self.reg:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
        self.reg = 0

    def draw_flag(self, qp):
        qp.setBrush(QColor(random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256)))
        r = random.randrange(1, self.y // 2)
        qp.drawEllipse(QPointF(random.randrange(0, self.x), random.randrange(0, self.y)), r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())