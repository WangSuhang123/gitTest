# 导入必要模块
from datetime import time

from PySide6 import QtWidgets, QtCore
from PySide6.QtGui import QPixmap
from UI_Main import Ui_MainWindow  # 导入生成的 UI 类


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
        self.quitButton.clicked.connect(self.quit)
        self.screenshotButton.clicked.connect(self.screenshot)

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

    #退出到登录页面
    def quit(self):
        self.close()
        from Login import Login
        self.login = Login()
        self.login.show()

    # 截屏功能
    def screenshot(self):
        #获取整个屏幕的截图
        screenshot = QtWidgets.QApplication.primaryScreen().grabWindow(0)

        # Use time module to generate the timestamp
        #使用datetime获取当前时间戳
        import datetime
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        # Save screenshot with the timestamped filename
        screenshot.save(f'./screenshots/{timestamp}.png')

        # Show success message
        QtWidgets.QMessageBox.information(self, '提示', '截屏成功！')



# 主程序入口
if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
