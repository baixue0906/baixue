import requests

import json

import pytest
import allure
s = requests.session()
def logout(s,username):
    url = "http://172.16.0.147:3039/eqpass/v1/logout"
    par = {
        "username": username
    }
    r = s.post(url,json = par)
    return r.text
@allure.feature("退出登录")
@pytest.mark.parametrize("username,expected",
                         [
                             ("ldd548686",""),#用户名正确
                             ("",""),#用户名为空
                             ("18332133281",""),#用户名为手机号
                             (111,""),#用户名类型错误
                             ("0987654321",""),#用户名不存在
                          ])
def test_logout1(username,expected):
    #logout(s,username)
    m = logout(s,username)
    m =json.loads(m)
    print(m)
    assert   m["message"] == expected