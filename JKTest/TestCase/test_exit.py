import requests
import json
import pytest
import pytest
import allure


s = requests.session()

def exit(username):
    url = "http://172.16.0.147:3039/eqpass/v1/teacher/exit"
    body = {
        "username":username
    }
    r = s.post(url,json= body)
    return r.text

@allure.feature("老师离开教室")
@allure.story("用户未登录")
@pytest.mark.parametrize("username,expected",[
    ("ldd548686","username is not defined"),
    ("teacheryanlinng","username is not defined"),
    ("","username is not defined"),
                                              ])
@pytest.mark.usefixtures("unlogin_fixture")
def test_exit1(username,expected):
    #m= unlogin_fixture
    a = exit(username)
    a= json.loads(a)
    #print(a)
    #print(expected)
    assert expected == a["message"]


@allure.feature("老师离开教室")
@allure.story("用户登录")
@pytest.mark.parametrize("username,expected",[
    ("liliok","username is not defined"),
    ("teacherlengjing","username is not defined"),
    ("","username is not defined"),
                                              ])
@pytest.mark.usefixtures("login_fixture")
def test_exit2(username,expected):
    #login(s)
    #s = login_fixture
    a = exit(username)
    a= json.loads(a)
    print(a)
    #print(expected)
    assert expected == a["message"]

if __name__ == '__main__':
    test_exit1()
    test_exit2()







if __name__ == '__main__':
    s = requests.session()
    test_exit1()
    test_exit2()




