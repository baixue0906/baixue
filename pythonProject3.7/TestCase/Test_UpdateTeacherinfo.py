import requests
import unittest
import time
from common import HTMLTestReport


class Update(unittest.TestCase):
    GUID=''
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
        Update.TMPTOKEN = opterTmpToken
        print(opterTmpToken)

    # 获取正式token，opterToken
    def test_gettoken(self):
            url = 'https://jdapi.jd100.com/uc/v1/sys/opterToken'
            params = {'opterTmpToken': Update.TMPTOKEN}
            r = requests.get(url=url, params=params)
            opterToken = r.json().get('data')['opterToken']
            Update.TOKEN = opterToken
            print(opterToken)

    # 正常添加老师获取新增老师的guid
    def test_AddTeacher(self):
            url = 'https://jdapi.jd100.com/coursemgr/v1/addTeacherInfo'
            headers = {'Content-Type': 'application/x-www-form-urlencoded', 'opterToken': Update.TOKEN}
            data = {'display_name': 'add08031', 'real_name': 'add08031', 'tech_subject': '语文','tech_grade':'初一'}
            r = requests.post(url=url, headers=headers, data=data)
            guid = r.json().get('data')['guid']
            Update.GUID=guid
            print(r.json())

    # 更新新增老师的信息，校验接口是否返回success，且更新的字段返回正确
    def test_UpdateTeacher1(self):
            url = 'https://jdapi.jd100.com/coursemgr/v1/updateTeacher'
            headers = {'Content-Type': 'application/x-www-form-urlencoded', 'opterToken': Update.TOKEN}
            data = {'guid': Update.GUID, 'display_name': 'edit08031', 'real_name': 'edit108031'}
            print(data)
            r = requests.post(url=url, headers=headers, data=data)
            assert r.json()['message'] == 'Success'
            assert r.json()['data']['displayName']=='edit08031'
            print(r.json())

    # 更新老师信息，未传必传参数老师guid，校验接口是否返回缺少参数的信息
    def test_UpdateTeacher2(self):
            url = 'https://jdapi.jd100.com/coursemgr/v1/updateTeacher'
            headers = {'Content-Type': 'application/x-www-form-urlencoded',
                       'opterToken': Update.TOKEN}
            data = {'guid': '', 'display_name': 'edit', 'real_name': 'edit1'}
            r = requests.post(url=url, headers=headers, data=data)
            assert r.json()['message'] == '缺少必要的参数'
            print(r.json())

    # 更新老师信息，传参guid为不存在的guid,校验接口是否返回错误提示
    def test_UpdateTeacher3(self):
            url = 'https://jdapi.jd100.com/coursemgr/v1/updateTeacher'
            headers = {'Content-Type': 'application/x-www-form-urlencoded',
                       'opterToken': Update.TOKEN}
            data = {'guid': '123', 'display_name': 'edit', 'real_name': 'edit1'}
            r = requests.post(url=url, headers=headers, data=data)
            assert r.json()['message'] == '该老师不存在'
            print(r.json())

    # 更新老师信息，未传必传参数optertoken，校验接口是否返回缺少参数的信息
    def test_UpdateTeacher4(self):
        url = 'https://jdapi.jd100.com/coursemgr/v1/updateTeacher'
        headers = {'Content-Type': 'application/x-www-form-urlencoded', 'opterToken': ''}
        data = {'guid':Update.GUID , 'display_name': 'edit08031', 'real_name': 'edit108031'}
        print(data)
        r = requests.post(url=url, headers=headers, data=data)
        assert r.json()['message'] == '缺少必要的参数'
        print(r.json())

    # 更新新增老师的信息，传参的key值有误，校验接口是否返回错误信息
    def test_UpdateTeacher5(self):
            url = 'https://jdapi.jd100.com/coursemgr/v1/updateTeacher'
            headers = {'Content-Type': 'application/x-www-form-urlencoded', 'opterToken': Update.TOKEN}
            data = {'guid': Update.GUID,
                    'displayname': 'editwrong'}
            print(data)
            r = requests.post(url=url, headers=headers, data=data)
            assert r.json()['message'] == 'Success'
            print(r.json())

    def tearDown(self):
        pass

def Run():
        suite = unittest.TestSuite()
        # 执行顺序是安装加载顺序：先执行test_case2，再执行test_case1
        suite.addTest(Update('test_gettmptoken'))
        suite.addTest(Update('test_gettoken'))
        suite.addTest(Update('test_AddTeacher'))
        suite.addTest(Update('test_UpdateTeacher1'))
        suite.addTest(Update('test_UpdateTeacher2'))
        suite.addTest(Update('test_UpdateTeacher3'))
        suite.addTest(Update('test_UpdateTeacher4'))
        suite.addTest(Update('test_UpdateTeacher5'))
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