import pytest
import requests
from commonlib.read_exc import Read_exc


@pytest.fixture()
def login_old():
    result = Read_exc()
    data = result.read_exc("用户")
    for i in range(0, 1):
        s = requests.session()
        url = data[i]["请求地址"]
        header = {"Content-Type": data[i]["Content-Type"]}
        body = {"do":"signon",
                "un": data[i]["account"],
                "pwd": data[i]["user_pwd"],
                "r": "1"}
        res = s.post(url=url, headers=header, data=body)
        r = res.headers["Set-Cookie"]
        print(r)
        return r





@pytest.fixture()
def login_new():
    result = Read_exc()
    data = result.read_exc("用户")
    for i in range(1, 2):
        url = data[i]["请求地址"]
        header = {"content-type": data[i]["Content-Type"],
                  "sourcetype": data[i]["sourcetype"]}
        body = {"account": data[i]["account"],
                "login_type": data[i]["login_type"],
                "user_pwd": data[i]["user_pwd"]
                }
        res = requests.post(url=url, headers=header, data=body)
        r =res.json()
        print(r)
        token = r["data"]["token"]
        print(token)
        return token




