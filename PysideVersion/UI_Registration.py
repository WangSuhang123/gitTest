# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registration.ui'
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

class Ui_Registration(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.UserldEdit = QLineEdit(self.centralwidget)
        self.UserldEdit.setObjectName(u"UserldEdit")
        self.UserldEdit.setGeometry(QRect(220, 80, 271, 61))
        self.UserPassEdit = QLineEdit(self.centralwidget)
        self.UserPassEdit.setObjectName(u"UserPassEdit")
        self.UserPassEdit.setGeometry(QRect(220, 160, 271, 61))
        self.UserNameEdit = QLineEdit(self.centralwidget)
        self.UserNameEdit.setObjectName(u"UserNameEdit")
        self.UserNameEdit.setGeometry(QRect(220, 240, 271, 61))
        self.AgeEdit = QLineEdit(self.centralwidget)
        self.AgeEdit.setObjectName(u"AgeEdit")
        self.AgeEdit.setGeometry(QRect(220, 320, 271, 61))
        self.QQNumEdit = QLineEdit(self.centralwidget)
        self.QQNumEdit.setObjectName(u"QQNumEdit")
        self.QQNumEdit.setGeometry(QRect(220, 400, 271, 61))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 100, 81, 31))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(80, 170, 81, 31))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(80, 250, 81, 31))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(80, 340, 81, 31))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(80, 420, 81, 31))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(230, 490, 151, 51))
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
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u8d26\u53f7", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u5bc6\u7801", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u7528\u6237\u540d", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u5e74\u9f84", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"qq", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u6210\u529f\u6ce8\u518c", None))
    # retranslateUi

