
import requests
import json
import pytest
import allure
from Commonlib.common import login
s = requests.session()


@allure.feature("获取个人信息")
@allure.story("用户未登录无法获取用户信息")
@pytest.mark.parametrize("expected",["用户未登录"])
def test_get_info1(expected):
    url = "http://172.16.0.147:3039/eqpass/v1/user"
    r = s.get(url)
    a = r.text
    a = json.loads(a)
    #print(expected)
    print(a['message'])
    assert expected == a['message']


@allure.feature("获取个人信息")
@allure.story("用户登录可以获取用户信息")
@pytest.mark.parametrize("expected",[("逗逗")])
def test_get_info2(expected):
    url = "http://172.16.0.147:3039/eqpass/v1/user"
    m = login(s)
    print(m)
    #s.headers.update(m)
    k = s.get(url)
    a = k.text
    a = json.loads(a)
    #print(a)
    #print(a['data']['user']['realName'])
    assert expected == a['data']['user']['realName']











