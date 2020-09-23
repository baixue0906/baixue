import pymysql
from database.configutils import getConfig
import datetime

DB = "easyweb_new_trans";
DBNAME = getConfig(DB, 'dbname')
DBHOST = getConfig(DB, 'dbhost')
DBUSER = getConfig(DB, 'dbuser')
DBPWD = getConfig(DB, 'dbpassword')
DBCHARSET = getConfig(DB, 'dbcharset')
DBPORT = getConfig(DB, "dbport")


class dbutils:

#构造函数
    def __init__(self,dbname=None, dbhost=None):
        if dbname is None:
            self._dbname=DBNAME
        else:
            self._dbname=dbname
        if dbhost is None:
            self._dbhost=DBHOST
        else:
            self._dbhost=dbhost
        self._dbuser = DBUSER
        self._dbpassword = DBPWD
        self._dbcharset = DBCHARSET
        self._dbport = int(DBPORT)
        self._conn = self.connectMySQL()
        if (self._conn):
            self._cursor=self._conn.cursor()


    #链接数据库
    def connectMySQL(self):
        conn=False
        try:
            conn=pymysql.connect(host=self._dbhost,
                                   user=self._dbuser,
                                   passwd=self._dbpassword,
                                   db=self._dbname,
                                   port=self._dbport,
                                   charset=self._dbcharset)
            cursor=conn.cursor()
        except:
            conn=False
        return conn

    #获取查询结果集
    def selectDB(self,phone):
        res=""
        if(self._conn):
            try:
                sql='select smscode from W_SmsMessageRecord where phone=%s order by id  desc limit 0,1'%phone;
                self._cursor.execute(sql)
                res=self._cursor.fetchall()
            except:
                res=False
        return res


  # 传课机制--paidcourse课程
    def selectPaidCourse(self, userid,activecode):
        res = ""
        if (self._conn):
            try:
                sql = 'select courseguid from W_R_Auth_PaidCourse a where a.userid=\"{0}\" and a.activecode=\"{1}\"'.format(userid,activecode);
                self._cursor.execute(sql)
                res = self._cursor.fetchall()
            except Exception as e:
                print(e)
                res = False
        return res

  # 传课机制--P码包含的课程
    def selectPackageContainsSale(self, package_guid):
        res = ""
        if (self._conn):
            try:
                sql = 'SELECT guid,name,courseinfo FROM W_SalesCoursePackageInfo WHERE guid=\"%s\" LIMIT 0, 1000' % package_guid;
                self._cursor.execute(sql)
                res = self._cursor.fetchall()
            except Exception as e:
                print(e)
                res = False
        return res

  # 传课机制--salecourse信息
    def selectSaleCourse(self, sale_guid):
        res = ""
        if (self._conn):
            try:
                sql = 'select a.guid,a.displayname,a.standard,b.standard_name from W_SalesCourseInfo a join W_StandardInfo b on a.standard=b.id where a.guid=\"%s\"'%sale_guid
                self._cursor.execute(sql)
                res = self._cursor.fetchall()
            except Exception as e:
                print(e)
                res = False
        return res

    #用户实际购买课程--crm购买课程走formalcard表
    def selectFormalcard(self, activecode):
        res = ""
        if (self._conn):
            try:
                sql = 'SELECT activecode,restrictdata FROM W_FormalCardInfo WHERE activecode=\"%s\" LIMIT 0, 1000' % activecode;
                self._cursor.execute(sql)
                res = self._cursor.fetchall()
            except Exception as e:
                print(e)
                res = False
        return res

    #查询用户auth表中的课程
    def selectAuthnotActive(self, userid):
            res = ""
            if (self._conn):
                try:
                    sql = 'SELECT course_code,standard FROM w_auth_course WHERE userid =\"%s\" LIMIT 0, 1000' %userid;
                    self._cursor.execute(sql)
                    res = self._cursor.fetchall()
                except Exception as e:
                    print(e)
                    res = False
            return res

    #激活具体的版本
    def selectAuthnotActive(self, userid):
            res = ""
            if (self._conn):
                try:
                    sql = 'SELECT course_code,standard FROM w_auth_course WHERE userid =\"%s\" LIMIT 0, 1000' %userid;
                    self._cursor.execute(sql)
                    res = self._cursor.fetchall()
                except Exception as e:
                    print(e)
                    res = False
            return res

    #激活版本--textbook
    def selectActiveCourse(self,course_code,standard,textbook ):
            res = ""
            if (self._conn):
                try:
                    sql = 'select moduleselectinfo from w_course_textbook a where a.course_code like \'{0}%\' and a.standard=\'{1}\' and a.textbook=\'{2}\''.format(course_code,standard,textbook);
                    self._cursor.execute(sql)
                    res = self._cursor.fetchall()
                except Exception as e:
                    print(e)
                    res = False
            return res

    #查询term
    def selectterm(self, course_code,term):
        res = ""
        if (self._conn):
            try:
                sql = 'select course_code from w_course_term a where a.course_code like \'{0}%\' and a.term=\'{1}\''.format(
                    course_code, term);
                self._cursor.execute(sql)
                res = self._cursor.fetchall()
            except Exception as e:
                print(e)
                res = False
        return res

    #得到最后的课程--level
    def getcourse(self,course_code ):
            res = ""
            if (self._conn):
                try:
                    sql = 'select salecourseguid from w_course_level  a where a.course_code like \'{0}%\''.format(course_code);
                    self._cursor.execute(sql)
                    res = self._cursor.fetchall()
                except Exception as e:
                    print(e)
                    res = False
            return res

    #查询数据-single
    def getsingle(self,course_code ):
            res = ""
            if (self._conn):
                try:
                    sql = 'select * from w_single_course  a where a.course_code= \'{0}\''.format(course_code);
                    self._cursor.execute(sql)
                    res = self._cursor.fetchall()
                except Exception as e:
                    print(e)
                    res = False
            return res
    #插入数据
    def insertauthcourse(self,**keys):
            res = ""
            if (self._conn):
                try:
                    sql = 'insert into w_auth_course(activecode,userid,course_code,auth_type,course_type,course_name,study_year,grade_name,subject_name,' \
                          'series,course,level_course,open_time,close_time,source_type,standard,state) ' \
                          'values(\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\')'.format(keys['activecode'],
                                                                                                                                                           keys['userid'],keys['course_code'],keys['auth_type'],keys['course_type'],keys['course_name'],keys['study_year'],keys['grade_name'],
                                                                                                                                                           keys['subject_name'],keys['series'],keys['course'],keys['level_course'],keys['open_time'],keys['close_time'],keys['source_type'],
                                                                                                                                                           keys['standard'],keys['state'])
                    print(sql)
                    self._cursor.execute(sql)
                    self._conn.commit()
                except Exception as e:
                    print(e)
                    res = False
            return res


    #关闭数据库
    def close(self):
        if(self._conn):
            try:
                if (type(self._cursor) == 'object'):
                    self._cursor.close()
                if (type(self._conn) == 'object'):
                    self._conn.close()
            except:
                print('Error: unable to fecth data')

if __name__=="__main__":
    dbhandle=dbutils()
    #single的code码
    course_code='201090502'
    res=dbhandle.getsingle(course_code)
    # open_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    close_time=(datetime.datetime.now()+datetime.timedelta(days=30)).strftime('%Y-%m-%d %H:%M:%S')
    # print(type(open_time))
    print(res[0][2],res[0][3],res[0][4],res[0][5],res[0][22])
    #需要传递的参数
    dbhandle.insertauthcourse(activecode="5836786331670340",userid='35668289',course_code=course_code,auth_type='1',course_type='10',course_name=res[0][2],study_year=res[0][3],
                              grade_name=res[0][4],subject_name=res[0][5],series=res[0][22],course='',level_course='',open_time=res[0][15],close_time=close_time,
                              source_type='1',standard='2',state='1')
    dbhandle.close()

# 35668257 baixue088



