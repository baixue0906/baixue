import pymysql

class DB_Connect():
    def db_connect(self,sql):
        db = pymysql.connect(host = "192.168.20.156",
                             port = 3306,
                             user = "test_user",
                             passwd="test_user!@#123",
                             db="easyweb_new_trans")  # 链接测试库
        cur = db.cursor(pymysql.cursors.DictCursor)    # 创建游标
        data = cur.execute(sql)   # 执行sql语句
        sql_result = cur.fetchall()
        db.commit()
        db.close()
        return sql_result

if __name__ == "__main__":
    result = DB_Connect()
    sql = "SELECT * FROM `W_RetainPageUser` WHERE `mobile` = '19900002536'"
    resu = result.db_connect(sql)
    print(resu)





