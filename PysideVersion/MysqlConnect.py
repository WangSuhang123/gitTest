#连接mysql数据库，并进行一系列操作
import pymysql

#连接数据库
def connect_mysql():
    try:
        conn = pymysql.connect(host='localhost', user='root', password='123456', db='gittest', charset='utf8')
        print("连接数据库成功")
        return conn
    except:
        print("连接数据库失败")
        return None
#测试连接
# connect_mysql()

