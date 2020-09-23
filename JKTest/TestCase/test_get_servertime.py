import requests
import json
import pytest
import time
import allure
s = requests.session()
def get_servertime(s):
    url = "http://172.16.0.147:3039/eqpass/v1/serverTime"

    r = s.get(url)
    return r.text
T= time.time()*1000
T = str(T)
print(type(T))
@allure.feature("获取服务器时间")
@allure.story("用户未登录")
@pytest.mark.parametrize("expected",[T])
def test_get_servertime(expected):
    m = get_servertime(s)
    m = json.loads(m)
    assert expected ==m['data']['date']


@allure.feature("获取服务器时间")
@allure.story("用户登录")
@pytest.mark.parametrize("expected",[T])
@pytest.mark.usefixtures("login_fixture")
def test_get_servertime(expected):
    m = get_servertime(s)
    m = json.loads(m)
    assert expected ==m['data']['date']
