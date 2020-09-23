import pytest
from Lib.Lib_api.api_activeCourse import *
from Lib.Lib_common.get_loginuserToken import *
import json
from Lib.Lib_common.compareDatabase import OperationMysql

class Test_getSingle:

    def setup_class(self):
        self.Token = UserToken().test_getuserToken()['token']

    def test_getSingle(self):
        userid = UserToken().test_getuserToken()['userID']
        # print(userid)
        #用户单科待激活的课程
        sql = "SELECT course_code from w_auth_course WHERE userid ='%s' and is_choice_textbook = 0" % (userid)
        a = OperationMysql().search_one(sql)
        b =a[0]['course_code']
        print(b)
        res = Acitve().api_getSingle(self.Token, b)
        print(res)

if __name__ == '__main__':
    pytest.main(['-s', 'test_getSingle.py'])