# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainui.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.UploadImage = QPushButton(self.centralwidget)
        self.UploadImage.setObjectName(u"UploadImage")
        self.UploadImage.setGeometry(QRect(70, 360, 191, 101))
        self.HitOnes = QPushButton(self.centralwidget)
        self.HitOnes.setObjectName(u"HitOnes")
        self.HitOnes.setGeometry(QRect(310, 360, 191, 101))
        self.MakeZero = QPushButton(self.centralwidget)
        self.MakeZero.setObjectName(u"MakeZero")
        self.MakeZero.setGeometry(QRect(550, 360, 191, 101))
        self.Imagelabel = QLabel(self.centralwidget)
        self.Imagelabel.setObjectName(u"Imagelabel")
        self.Imagelabel.setGeometry(QRect(270, 80, 241, 151))
        self.numLabel = QLabel(self.centralwidget)
        self.numLabel.setObjectName(u"num")
        self.numLabel.setGeometry(QRect(350, 270, 91, 31))
        #增加一个退出按钮
        self.quitButton = QPushButton(self.centralwidget)
        self.quitButton.setObjectName(u"quitButton")
        self.quitButton.setGeometry(QRect(70, 480, 191, 101))
        #新增一个截屏按钮
        self.screenshotButton = QPushButton(self.centralwidget)
        self.screenshotButton.setObjectName(u"screenshotButton")
        self.screenshotButton.setGeometry(QRect(310, 480, 191, 101))

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
        self.UploadImage.setText(QCoreApplication.translate("MainWindow", u"上传图片", None))
        self.HitOnes.setText(QCoreApplication.translate("MainWindow", u"敲一敲", None))
        self.MakeZero.setText(QCoreApplication.translate("MainWindow", u"清零", None))
        self.Imagelabel.setText(QCoreApplication.translate("MainWindow", u"图片", None))
        self.numLabel.setText(QCoreApplication.translate("MainWindow", u"功德", None))
        self.quitButton.setText(QCoreApplication.translate("MainWindow", u"退出", None))
        self.screenshotButton.setText(QCoreApplication.translate("MainWindow", u"截屏", None))


