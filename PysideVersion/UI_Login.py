# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_Login(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.LoginButton = QPushButton(self.centralwidget)
        self.LoginButton.setObjectName(u"LoginButton")
        self.LoginButton.setGeometry(QRect(160, 390, 171, 81))
        self.RgisteredButton = QPushButton(self.centralwidget)
        self.RgisteredButton.setObjectName(u"RgisteredButton")
        self.RgisteredButton.setGeometry(QRect(430, 390, 171, 81))
        self.IDinsert = QLineEdit(self.centralwidget)
        self.IDinsert.setObjectName(u"IDinsert")
        self.IDinsert.setGeometry(QRect(140, 80, 521, 91))
        self.PassWordInsert = QLineEdit(self.centralwidget)
        self.PassWordInsert.setObjectName(u"PassWordInsert")
        self.PassWordInsert.setGeometry(QRect(140, 200, 521, 91))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 110, 101, 41))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 230, 101, 41))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.LoginButton.setText(QCoreApplication.translate("MainWindow", u"\u767b\u5f55", None))
        self.RgisteredButton.setText(QCoreApplication.translate("MainWindow", u"\u6ce8\u518c", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u8d26\u53f7", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u5bc6\u7801", None))
    # retranslateUi
