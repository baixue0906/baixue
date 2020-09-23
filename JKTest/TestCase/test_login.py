
import requests
import json
import pytest
import allure
def login(s,username,password,passwordEn,remember,role):
    url = "http://172.16.0.147:3039/eqpass/v1/login"
    par = {
        "username": username,
        "password": password,
        "passwordEn":passwordEn,
        "remember":remember,
        "role": role
    }
    r = s.post(url,json = par)
    return r.text


@allure.feature("登录")
@pytest.mark.parametrize("username,password,passwordEn,remember,role,expected",
                         [
                             ("ldd548686","11111","",True,"0",""),#学生登陆
                             ("ldd548686","1234567","",True,"0","用户名或密码错误"),#密码错误
                             ("ldd5486861111","11111","",True,"0","用户名或密码错误"),#用户名错误
                             ("teacheryanling","11111","",True,1,""),#老师登陆
                             ("teacheryanling","11111","",False,1,""),#老师登陆不记住密码
                             ("ldd548686","11111","",False,0,""),#学生登录，不记住密码
                             ("ldd548686","11111","",False,1,"教练不存在"),#教练不存在
                             ("ldd548686","11111","",False,0,""),#老师以学生身份登陆
                             ("ldd548686111111111111","11111","",True,0,"用户名/手机号不能超过20个字符，请重新输入"),
                             ("ldd548686123","11111111","",True,0,"用户名或密码错误"),
                             ("ldd548686","","",True,0,'"password" is not allowed to be empty'),
                             ("","11111","",True,0,'"username" is not allowed to be empty'),
                             ("ldd548686","11111","",True,"",'"role" must be a number'),
                             ("ldd548686","11111","0","","",'"remember" must be a boolean'),
                             ("ldd548686","11111","0",123,"",'"remember" must be a boolean'),
                             ("ldd548686","11111","0",True,234,''),
                             ("ldd548686","11111","",False,"0",""),#不记住密码
                             ("18332133285","11111","",True,"0",""),#手机号登录，正确密码
                             ("18332133285","111111","",True,"0","用户名或密码错误"),#手机号登录，错误密码
                             ("18332133278","11111","",True,"0","用户名或密码错误"),#错误手机号登录，正确密码
                             ("18332133285","111111","",False,"0","用户名或密码错误"),#手机号登录，错误密码,不记住密码
                             ("18332133278","11111","",False,"0","用户名或密码错误"),#错误手机号登录，正确密码，不记住密码
                         ]
                         )
def test_login1(username,password,passwordEn,remember,role,expected):
    s= requests.session()
    #login(s,username,password,passwordEn,remember,role)
    m = login(s,username,password,passwordEn,remember,role)
    m =json.loads(m)
    assert   m["message"] == expected




