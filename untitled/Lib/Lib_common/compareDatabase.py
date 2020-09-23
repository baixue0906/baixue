import requests
import json
import pymysql

# 提取接口返回参数
class Run_Main():
    TOKEN = ''  # 定义一个属性，TOKEN

    def __init__(self, token):
        self.TOKEN = token

    def send_post(self, url, data):
        headers = {'Content-Type': 'application/x-www-form-urlencoded', 'opterToken': self.TOKEN}
        r=requests.post(url=url, data=data, headers=headers)
        res = r.json()
        return json.dumps(res, indent=2, sort_keys=True, ensure_ascii=False) #json.dumps()用于将字典形式的数据转化为字符串

    def send_get(self, url):
        headers = {'opterToken': self.TOKEN}
        res = requests.get(url=url, headers=headers).json()
        return json.dumps(res, indent=2, sort_keys=True, ensure_ascii=False)

    def run_main(self, url, method, data=None):
        if method == 'POST':
            res = self.send_post(url, data)
        else:
            res = self.send_get(url)
        return res


# 数据库查询结果
class OperationMysql:
    def __init__(self):
        self.conn = pymysql.connect(
            host='192.168.20.156',
            port=3306,
            user='test_user',
            passwd='test_user!@#123',
            db='easyweb_new_trans',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.conn.cursor()

    def search_one(self, sql):
        self.cur.execute(sql)
        result = self.cur.fetchall()
        # 关闭游标
        self.cur.close()
        # 关闭数据库
        self.conn.close()
        return result


# 关键字比较
if __name__ == '__main__':

    # 调用post接口，打印返回值,添加老师
    url = 'https://jdapi.jd100.com/coursemgr/v1/addTeacherInfo'
    data = {'display_name': 'test0807',
            'real_name': 'real0807',
            'tech_subject': '语文，数学',
            'tech_grade': '高一，高二'
            }
    token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1OTY4NTU0ODYsImlhdCI6MTU5Njc2OTA4NiwibmJmIjoxNTk2NzY4OTY2LCJzeXN0eXBlIjoiIiwidXNlcl9pZCI6IiJ9.hMphegQ0G7S1bs_CeMtr9COM1XfT3llhjyOwUcqutHI'
    run = Run_Main(token)  # 将类实例化为一个对象run
    res = run.run_main(url, 'POST', data)  # 类对象调用方法
    # 将返回结果格式化成字典
    b = json.loads(res) #json.loads()用于将字符串形式的数据转化为字典
    print(b['data']['techGrade'])  # 打印接口返回的字段值

    # 调用数据库方法，执行查询语句，输出查询结果
    op_mysql = OperationMysql()
    sql = "SELECT * from W_TeacherInfo WHERE teachername='test0807'"
    a = op_mysql.search_one(sql)
    print(a[0]['tech_grade'])  # 打印数据库查询接口的字段值

    if b['data']['techGrade'] == a[0]['tech_grade'] and b['data']['realName'] == a[0]['real_name'] and b['data'][
        'guid'] == a[0]['guid']:
        print('添加老师接口数据库数据对比成功')
    else:
        print("失败")


    # # 调用get接口，打印返回值，查询老师列表
    # url = 'https://jdapi.jd100.com/coursemgr/v1/getTeacherList'
    # token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1OTY4NTU0ODYsImlhdCI6MTU5Njc2OTA4NiwibmJmIjoxNTk2NzY4OTY2LCJzeXN0eXBlIjoiIiwidXNlcl9pZCI6IiJ9.hMphegQ0G7S1bs_CeMtr9COM1XfT3llhjyOwUcqutHI'
    # run = Run_Main(token) #类Run_Main实例化
    # res = run.run_main(url, 'GET')
    # # 将返回结果格式化成字典
    # b = json.loads(res)
    # # print(b['data'][2]['techGrade'])
    #
    # # 调用数据库方法，执行查询语句，输出查询结果
    # op_mysql = OperationMysql()
    # sql = "SELECT * from W_TeacherInfo WHERE teachername='王严'"
    # a = op_mysql.search_one(sql)
    # # print(a[0]['tech_grade'])
    #
    # if b['data'][2]['techGrade'] == a[0]['tech_grade']:
    #     print('查询老师接口数据库数据对比成功')
    # else:
    #     print("失败")

