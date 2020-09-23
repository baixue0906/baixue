import requests
import json
import pytest
from Commonlib.common import login
import allure
s=requests.session()
def get_tmptoken():
    url = "http://172.16.0.147:3039/eqpass/v1/tmp/token"
    m = s.get(url)
    return m.text

@allure.feature("获取临时token")
@allure.story("用户未登录，无法获取token")
@pytest.mark.parametrize("expected",["用户未登录"])
#@pytest.mark.usefixtures("unlogin_fixture")
def test_get_tmptoken1(expected):
    a = get_tmptoken()
    a = json.loads(a)
    #print(a)
    assert expected == a['message']
@allure.feature("获取临时token")
@allure.story("用户登录，获取token")
@pytest.mark.parametrize("expected",[0])
def test_get_tmptoken2(expected):
    login(s)
    b = get_tmptoken()
    b = json.loads(b)
    print(b)
    assert expected == b['code']


