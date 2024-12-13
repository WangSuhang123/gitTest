# 导入必要模块
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPixmap
from testmuyu import Ui_MainWindow  # 导入生成的 UI 类


# 定义主窗口类
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.num = 0

        # 初始化界面
        self.numLabel.setText(str(self.num))
        self.UploadImage.clicked.connect(self.uploadImage)
        self.HitOnes.clicked.connect(self.hitOnes)
        self.MakeZero.clicked.connect(self.makeZero)

    # 上传图片功能
    def uploadImage(self):
        imagePath = QtWidgets.QFileDialog.getOpenFileName(self, "上传图片", "", "Image Files (*.jpg *.png *.jpeg)")[0]
        if imagePath:
            pixmap = QPixmap(imagePath)
            self.Imagelabel.setPixmap(pixmap)
            self.Imagelabel.setScaledContents(True)  # 图片自适应标签大小

    # 点击 "敲一敲" 按钮，计数加1
    def hitOnes(self):
        self.num += 1
        self.numLabel.setText(str(self.num))

    # 点击 "清零" 按钮，计数重置为0
    def makeZero(self):
        self.num = 0
        self.numLabel.setText(str(self.num))


# 主程序入口
if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
