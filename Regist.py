#使用registration.py里面的oyqt5界面进行注册功能的开发
import MysqlConnect
from registration import Ui_Registration
from PyQt5 import QtWidgets
import sys

class Registration(QtWidgets.QMainWindow, Ui_Registration):
    def __init__(self, parent=None):
        super(Registration, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.register)


    def register(self):
        # 注册功能的实现
        #获取输入在界面中的信息
        UserID = self.UserldEdit.text()
        UserPass = self.UserPassEdit.text()
        UserName = self.UserNameEdit.text()
        UserAge = self.AgeEdit.text()
        UserQQ = self.QQNumEdit.text()

        #打印获取到的信息
        print("UserID:", UserID)
        print("UserPass:", UserPass)
        print("UserName:", UserName)
        print("UserAge:", UserAge)
        print("UserQQ:", UserQQ)

        #将获取到的信息写入数据库里面
        #数据库已经在MysqlConnect.py连接
        #执行SQL语句进行注册
        #注册成功后返回到登录界面
        conn = MysqlConnect.connect_mysql()
        cursor = conn.cursor()
        sql = "INSERT INTO userinfo(UserID, UserPass, UserName, Age, QQNum) VALUES (%s,%s,%s,%s,%s)"
        try:
            cursor.execute(sql, (UserID, UserPass, UserName, UserAge, UserQQ))
            conn.commit()
            QtWidgets.QMessageBox.information(self, "提示", "注册成功！")
            #注册成功后关闭注册界面
            self.close()
            #登录界面打开
            from Login import Login
            self.login = Login()
            self.login.show()
            print("注册成功！打开页面成功")

        except:
            QtWidgets.QMessageBox.warning(self, "警告", "注册失败！")
            #如果失败，打印出错误信息
            # print(cursor.execute(sql, (UserID, UserPass, UserName, UserAge, UserQQ)))
            conn.rollback()
        conn.close()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myWin = Registration()
    myWin.show()
    sys.exit(app.exec_())

