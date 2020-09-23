import pytest
import allure
import requests
import time
from commonlib.read_exc import Read_exc

@allure.feature("用户登录接口测试")
class Test_login():

    @allure.title("密码登录")
    def test_001(self):
        result = Read_exc()
        data = result.read_exc("登录")

        for i in range(0,5):
            url = data[i]["请求地址"]
            header = {"content-type":data[i]["Content-Type"],
                      "sourcetype":data[i]["sourcetype"]}
            body = {"account":data[i]["account"],
                    "login_type":data[i]["login_type"],
                    "user_pwd":data[i]["user_pwd"],
                    "verify_code_img":data[i]["verify_code_img"],
                    "verify_code_sms":data[i]["verify_code_sms"]}
            res = requests.post(url = url,headers = header, data = body)
            r = res.json()
            print(r)

            assert r["code"] == int(data[i]["code"])
            assert r["message"] == data[i]["预期结果"]
        time.sleep(120)

    @allure.title("验证码登录")
    def test_002(self):
        result = Read_exc()
        data = result.read_exc("登录")

        for i in range(5, 8):
            url = data[i]["请求地址"]
            header = {"content-type": data[i]["Content-Type"],
                      "sourcetype": data[i]["sourcetype"]}
            body = {"account": data[i]["account"],
                    "login_type": data[i]["login_type"],
                    "user_pwd": data[i]["user_pwd"],
                    "verify_code_img": data[i]["verify_code_img"],
                    "verify_code_sms": data[i]["verify_code_sms"]}
            res = requests.post(url=url, headers=header, data=body)
            r = res.json()
            print(r)

            assert r["code"] == int(data[i]["code"])
            assert r["message"] == data[i]["预期结果"]
        time.sleep(120)


if __name__ == "__main__":
    pytest.main(["-s","test_login.py"])

