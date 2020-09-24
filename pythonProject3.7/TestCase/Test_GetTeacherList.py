import time
import unittest
import requests
from common import HTMLTestReport
import jsonpath

class TeacherList(unittest.TestCase):
        TMPTOKEN = ''
        TOKEN = ''
        def setUp(self):
            pass
        # case1：获取临时token，opterTmpToken
        def test_gettmptoken(self):
            url = 'https://jdapi.jd100.com/uc/core/v1/sys/opterTmpToken'
            params = {'sysID': '5'}
            r = requests.get(url=url, params=params)
            TeacherList.TMPTOKEN=r.json().get('data')['opterTmpToken']
            print(TeacherList.TMPTOKEN)

        # case2：获取正式token，opterToken
        def test_gettoken(self):
            url = 'https://jdapi.jd100.com/uc/v1/sys/opterToken'
            params = {'opterTmpToken': TeacherList.TMPTOKEN}
            r = requests.get(url=url, params=params)
            TeacherList.TOKEN = r.json().get('data')['opterToken']
            print(TeacherList.TOKEN)

        #case3：验证获取教师列表是否成功返回success
        def test_GetTeacherList1(self):
                url ='https://jdapi.jd100.com/coursemgr/v1/getTeacherList'
                headers = {'opterToken': TeacherList.TOKEN}
                r = requests.get(url=url, headers=headers)
                assert r.json()['message'] == 'Success'
                print(r.json())

        #case4：验证传参不传optertoken，接口是否返回缺少参数的提示
        def test_GetTeacherList2(self):
                url ='https://jdapi.jd100.com/coursemgr/v1/getTeacherList'
                headers = {'opterToken': ''}
                r = requests.get(url=url, headers=headers)
                assert r.json()['message'] == '缺少必要的参数'
                print(r.json())

        #case5:验证传参传无效optertoken，接口是否返回错误提示
        def test_GetTeacherList3(self):
                url ='https://jdapi.jd100.com/coursemgr/v1/getTeacherList'
                headers = {'opterToken': '11'}
                r = requests.get(url=url, headers=headers)
                assert r.json()['message'] == 'token无效'
                print(r.json())

        #case6:验证获取教师列表，返回字段是否含有教师guid字段
        def test_GetTeacherList4(self):
                url ='https://jdapi.jd100.com/coursemgr/v1/getTeacherList'
                headers = {'opterToken': TeacherList.TOKEN}
                r = requests.get(url=url, headers=headers)
                self.assertIn('guid',r.text)
                print(r.text)

        #case7:验证获取教师列表，是否返回已存在的老师信息
        def test_GetTeacherList5(self):
                url ='https://jdapi.jd100.com/coursemgr/v1/getTeacherList'
                headers = {'opterToken': TeacherList.TOKEN}
                r = requests.get(url=url, headers=headers)
                teacherguid = jsonpath.jsonpath(r.json(), '$..guid')
                assert teacherguid == ['006e6fa6aa6049ba8d70853235b466fd']

        def tearDown(self):
                pass

def Run():
        suite = unittest.TestSuite()
        # 执行顺序是安装加载顺序：先执行test_case2，再执行test_case1
        suite.addTest(TeacherList('test_gettmptoken'))
        suite.addTest(TeacherList('test_gettoken'))
        suite.addTest(TeacherList('test_GetTeacherList1'))
        suite.addTest(TeacherList('test_GetTeacherList2'))
        suite.addTest(TeacherList('test_GetTeacherList3'))
        suite.addTest(TeacherList('test_GetTeacherList4'))
        suite.addTest(TeacherList('test_GetTeacherList5'))
        now = time.strftime("%Y-%m-%d_%H%M", time.localtime())
        filepath = './report/' + now + '.html' # 测试报告存放的位置
        fp = open(filepath, 'wb')
        runner = HTMLTestReport.HTMLTestRunner\
        (
        stream=fp,
        title='获取教师列表接口自动化测试报告',
        tester='白雪'
                )
        runner.run(suite)
        fp.close()

Run()