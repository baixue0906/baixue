import requests

class TeacherList():
    TMPTOKEN = ''
    TOKEN = ''

    # 获取临时token，opterTmpToken
    def test_gettmptoken(self):
        url = 'https://jdapi.jd100.com/uc/core/v1/sys/opterTmpToken'
        params = {'sysID': '5'}
        r = requests.get(url=url, params=params)
        TeacherList.TMPTOKEN = r.json().get('data')['opterTmpToken']
        return TeacherList.TMPTOKEN

    # 获取正式token，opterToken
    def test_gettoken(self):
        url = 'https://jdapi.jd100.com/uc/v1/sys/opterToken'
        params = {'opterTmpToken': TeacherList.TMPTOKEN}
        r = requests.get(url=url, params=params)
        TeacherList.TOKEN = r.json().get('data')['opterToken']
        return TeacherList.TOKEN

if __name__ == "__main__":
    tmptoken = TeacherList().test_gettmptoken()
    opterToken= TeacherList().test_gettoken()
    print(opterToken)
