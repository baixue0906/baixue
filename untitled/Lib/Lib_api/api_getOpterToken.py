import requests
from configs.config import HOST

class TeacherList():

    # 获取临时token，opterTmpToken
    def test_gettmptoken(self):
        url = f'{HOST}/uc/core/v1/sys/opterTmpToken'
        params = {'sysID': '5'}
        r = requests.get(url=url, params=params)
        return r.json()['data']['opterTmpToken']

    # 获取正式token，opterToken
    def test_gettoken(self):
        url = f'{HOST}/uc/v1/sys/opterToken'
        params = {'opterTmpToken': TeacherList().test_gettmptoken()}
        r = requests.get(url=url, params=params)
        return r.json()['data']['opterToken']

if __name__ == "__main__":
    tmptoken = TeacherList().test_gettmptoken()
    opterToken= TeacherList().test_gettoken()
    print(opterToken)
