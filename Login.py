#使用LoginUI.py里面的pyqt5界面进行登录功能的开发，然后将其与Login.py绑定，实现登录功能。登录成功后，将会进入主界面。
import sys
from PyQt5 import QtWidgets
import MysqlConnect
from LoginUI import Ui_Login
from main import MainWindow
from Regist import Registration

class Login(QtWidgets.QMainWindow, Ui_Login):
    def __init__(self):
        super(Login, self).__init__()
        self.setupUi(self)
        self.LoginButton.clicked.connect(self.login)
        self.RgisteredButton.clicked.connect(self.Register)

        #实例化主界面
        self.MainWindow = MainWindow()
        # 实例化注册界面
        self.Registration = Registration()


    def login(self):
        UserID = self.IDinsert.text()
        UserPass = self.PassWordInsert.text()
        # 这里需要连接数据库进行验证，如果验证成功，则进入主界面
        conn = MysqlConnect.connect_mysql()
        cursor = conn.cursor()
        sql = "SELECT * FROM userinfo WHERE UserId = %s AND UserPass = %s"
        cursor.execute(sql, (UserID, UserPass))
        result = cursor.fetchone()
        if result:
            #打印出登录成功的账号密码信息
            print("登录成功！UserID is ", UserID, "UserPass is ", UserPass)
            # 登录成功后，关闭登录界面，并运行main.py的主界面
            self.close()
            # 打开主界面
            self.MainWindow.show()
        else:
            # 登录失败，弹出提示框
            print("登录失败！")
            self.error_message = QtWidgets.QMessageBox()
            self.error_message.setIcon(QtWidgets.QMessageBox.Warning)

    def Register(self):
        #关闭当前登录界面
        self.close()
        # 点击注册按钮，打开注册界面
        self.Registration.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    login = Login()
    login.show()
    sys.exit(app.exec_())