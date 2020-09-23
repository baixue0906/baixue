import requests

import json

import pytest
#from Commonlib.common import login
import allure

s = requests.session()

def getConfig():
    url = "http://172.16.0.147:3039/eqpass/v1/getConfig"
    r = s.get(url)
    return r.text
@allure.feature("获取配置信息")
@allure.story("用户登录")
@pytest.mark.parametrize("expected",[("http://dayidata2.jiandan100.cn/")])
@pytest.mark.usefixtures("login_fixture")
def test_getconfig1(expected):
    a = getConfig()
    a= json.loads(a)
    #print(a)
    #print(expected)
    assert expected == a["data"]["userImgServer"]["domain"]
@allure.feature("获取配置信息")
@allure.story("用户未登录，无法获取")
@pytest.mark.parametrize("expected",[("")])
@pytest.mark.usefixtures("unlogin_fixture")
def test_getconfig2(expected):
    a = getConfig()
    a= json.loads(a)
    #print(a)
    #print(expected)
    assert expected == a["message"]







if __name__ == '__main__':
    s = requests.session()
    test_getconfig2()
    test_getconfig1()




