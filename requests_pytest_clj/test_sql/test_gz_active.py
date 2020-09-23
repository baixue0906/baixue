# encoding:utf-8
import pytest,urllib3,json
import pymysql.cursors
urllib3.disable_warnings()

class TestSelectSql():
    def select_all_ok(self,sql):
        try:
            conn = pymysql.connect(
                host='192.168.20.156',
                port=3306,
                user='test_user',
                passwd='test_user!@#123',
                db='easyweb_new_trans',
                charset='utf8',
                cursorclass=pymysql.cursors.DictCursor)
            connected = True
        except pymysql.Error as e:
            print('数据库连接失败:', end='')
        try:
            with conn.cursor() as cursor:
                cursor.execute(sql)
            conn.commit()
            return cursor.fetchall()
        except pymysql.Error as e:
            return e

    def test_paid(self):
        #查询用户买的正式课中的s课满足一键激活的所有内容
        res = self.select_all_ok('select * from W_SalesCourseInfo a, (select courseguid from W_R_Auth_PaidCourse'
                                     ' where userid = 35667393 and activemodule = 1 and isdeleted = 0 and structtype = 3 '
                                 'and isfuture = 0) b where a.guid =b.courseguid and  a.series =1 and '
                                     ' a.modelselectinfo !=" " and a.isvalid =1 and a.name not like "%中考%" and a.name like "%初%" ')
        #print(res)
        #遍历数据库表中查到的数据的modelselectinfo不为空的内容，默认激活X版本，找到最后激活后的课程id
        try:
            for i in res:
                if i['modelselectinfo'] != '':
                    #数据库中每个虚拟课对应的modelselectinfo是json格式，解析为中文
                    moduleinfo = i['modelselectinfo'].encode('utf-8').decode("unicode_escape")
                    print(moduleinfo)
                    #激活版本为第一个版本
                    moduleinfo = json.loads(moduleinfo)[0]['items']
                    required = moduleinfo[0]['required']
                    elective = moduleinfo[0]['elective']
                    #打印必须激活的的所有课程id
                    for a in required:
                        if a != '':
                            print(a['id'])
                            #print('required：'+a['id'])
                    #打印选择激活的最大激活数量的所有课程id
                    elective_list = []
                    elective_list.append(elective)
                    max = int(elective['max'])
                    for b in elective_list:
                        if max > 0:
                            for a in range(0,max):
                                print(b['data'][a]['id'])
                                #print(max,a,b['data'][a]['id'])
                                #print('elective：'+b['data'][a]['id'])








        except Exception as e :
            return e

if __name__ =='__main__':
    pytest.main('-v',['../test_case_course/test_gz_active.py'])




