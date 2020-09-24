import requests
import unittest
import time
from common import HTMLTestReport


class Add(unittest.TestCase):
    GUID = ''
    TMPTOKEN = ''
    TOKEN = ''

    def setUp(self):
        pass

    # 获取临时token，opterTmpToken
    def test_gettmptoken(self):
        url = 'https://jdapi.jd100.com/uc/core/v1/sys/opterTmpToken'
        params = {'sysID': '5'}
        r = requests.get(url=url, params=params)
        print(r.text)
        opterTmpToken = r.json().get('data')['opterTmpToken']
        Add.TMPTOKEN = opterTmpToken
        print(opterTmpToken)

    # 获取正式token，opterToken
    def test_gettoken(self):
        url = 'https://jdapi.jd100.com/uc/v1/sys/opterToken'
        params = {'opterTmpToken': Add.TMPTOKEN}
        r = requests.get(url=url, params=params)
        opterToken = r.json().get('data')['opterToken']
        Add.TOKEN = opterToken
        print(opterToken)

    #添加老师，校验接口是否返回success
    def test_add1(self):
            url = 'https://jdapi.jd100.com/coursemgr/v1/addTeacherInfo'
            headers = {'Content-Type': 'application/x-www-form-urlencoded', 'opterToken': Add.TOKEN}
            data = {'display_name': 'test0727', 'real_name': 'test0727realname', 'tech_subject': '语文，数学','tech_grade':'高一，高二'}
            r = requests.post(url=url, headers=headers, data=data)
            assert r.json()['message'] == 'Success'
            print(r.json())

     # 添加老师，传参不传opterToken，校验接口是否返回缺少参数
    def test_add2(self):  # 传参不传displayname
        url = 'https://jdapi.jd100.com/coursemgr/v1/addTeacherInfo'
        headers = {'Content-Type': 'application/x-www-form-urlencoded', 'opterToken': ''}
        data = {'display_name': 'displayname0804', 'real_name': 'realname0804', 'tech_subject': '语文', 'tech_grade': '初一'}
        r = requests.post(url=url, headers=headers, data=data)
        assert r.status_code == 200
        assert r.json()['message'] == '缺少必要的参数'
        print(r.json())

    #添加老师，传参不传display_name，校验接口是否返回缺少参数
    def test_add3(self):
                url = 'https://jdapi.jd100.com/coursemgr/v1/addTeacherInfo'
                headers = {'Content-Type': 'application/x-www-form-urlencoded', 'opterToken': Add.TOKEN}
                data = {'display_name': '', 'real_name': 'realname0804', 'tech_subject': '语文','tech_grade':'初一'}
                r = requests.post(url=url, headers=headers, data=data)
                assert r.status_code == 200
                assert r.json()['message'] == '缺少必要的参数'
                print(r.json())

    # 添加老师，传参不传real_name，校验接口是否返回缺少参数
    def test_add4(self):
                url = 'https://jdapi.jd100.com/coursemgr/v1/addTeacherInfo'
                headers = {'Content-Type': 'application/x-www-form-urlencoded', 'opterToken': Add.TOKEN}
                data = {'display_name': 'test0727', 'real_name': '', 'tech_subject': '语文','tech_grade':'初一'}
                r = requests.post(url=url, headers=headers, data=data)
                assert r.status_code == 200
                assert r.json()['message'] == '缺少必要的参数'
                print(r.json())

    # 添加老师，传参不传tech_subject，校验接口是否返回缺少参数
    def test_add5(self):
                url = 'https://jdapi.jd100.com/coursemgr/v1/addTeacherInfo'
                headers = {'Content-Type': 'application/x-www-form-urlencoded', 'opterToken': Add.TOKEN}
                data = {'display_name': 'test0727', 'real_name': 'test0727realname', 'tech_subject': '','tech_grade':'初一'}
                r = requests.post(url=url, headers=headers, data=data)
                assert r.status_code == 200
                assert r.json()['message'] == '缺少必要的参数'
                print(r.json())

    # 添加老师，传参不传tech_grade，校验接口是否返回缺少参数
    def test_add6(self):
                url = 'https://jdapi.jd100.com/coursemgr/v1/addTeacherInfo'
                headers = {'Content-Type': 'application/x-www-form-urlencoded', 'opterToken': Add.TOKEN}
                data = {'display_name': 'test0727', 'real_name': 'test0727realname', 'tech_subject': '语文','tech_grade':''}
                r = requests.post(url=url, headers=headers, data=data)
                assert r.status_code == 200
                assert r.json()['message'] == '缺少必要的参数'
                print(r.json())

    def tearDown(self):
        pass

def Run():
        suite = unittest.TestSuite()
        # 执行顺序是安装加载顺序：先执行test_case2，再执行test_case1
        suite.addTest(Add('test_add1'))
        suite.addTest(Add('test_add2'))
        suite.addTest(Add('test_add3'))
        suite.addTest(Add('test_add4'))
        suite.addTest(Add('test_add5'))
        suite.addTest(Add('test_add6'))
        now = time.strftime("%Y-%m-%d_%H%M", time.localtime())
        filepath = './report/' + now + '.html'  # 测试报告存放的位置
        fp = open(filepath, 'wb')
        runner = HTMLTestReport.HTMLTestRunner(
            stream=fp,
            title='接口自动化测试报告',
            tester='白雪'
        )
        runner.run(suite)
        fp.close()


Run()