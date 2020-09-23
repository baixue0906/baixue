import requests
import unittest
import time
from common import HTMLTestReport


class Get(unittest.TestCase):
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
        Get.TMPTOKEN = opterTmpToken
        print(opterTmpToken)

    # 获取正式token，opterToken
    def test_gettoken(self):
        url = 'https://jdapi.jd100.com/uc/v1/sys/opterToken'
        params = {'opterTmpToken': Get.TMPTOKEN}
        r = requests.get(url=url, params=params)
        opterToken = r.json().get('data')['opterToken']
        Get.TOKEN = opterToken
        print(opterToken)

    #获取教师资质信息，校验结果是否返回success
    def test_getQualificationInfo(self):
            url = 'https://jdapi.jd100.com/coursemgr/v1/getQualificationInfo'
            para = {'opterToken':Get.TOKEN}
            r = requests.get(url=url, params=para)
            assert r.json()['message'] == 'Success'
            print(r.json())

    # 获取教师资质信息，校验接口返回的老师资质相关信息是否正确
    def test_getQualificationInfo(self):
        url = 'https://jdapi.jd100.com/coursemgr/v1/getQualificationInfo'
        para = {'opterToken': Get.TOKEN}
        r = requests.get(url=url, params=para)
        assert r.json()['data'][2]['teacher_name'] == '测试勿扰老师'
        assert r.json()['data'][2]['certificate_url'] == 'https://jdspace.jd100.com/teachers/5c5f5d11-13f2-4ce0-8959-5e2ab23f22be.jpg'
        assert r.json()['data'][2]['teacher_url'] == 'https://jdspace.jd100.com/teachers/be6195dc-5f78-4661-b4dd-6ac709994498.jpg'
        assert r.json()['data'][2]['teacher_certificate'] == '111111111111111'

    def tearDown(self):
        pass

def Run():
        suite = unittest.TestSuite()
        # 执行顺序是安装加载顺序：先执行test_case2，再执行test_case1
        suite.addTest(Get('test_gettmptoken'))
        suite.addTest(Get('test_gettoken'))
        suite.addTest(Get('test_getQualificationInfo'))
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