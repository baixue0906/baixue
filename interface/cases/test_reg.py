import pytest
import requests
import allure
import time
from commonlib.read_exc import Read_exc

@allure.feature("注册接口测试")
class Test_reg:

    @allure.title("注册接口测试")
    def test_reg(self):
        result = Read_exc()
        data = result.read_exc("注册")

        for i in data:
            url = i["请求地址"]
            header = {"Content-Type":i["Content-Type"],
                      "sourceType":i["sourceType"]}
            body = {"mobile":i["mobile"],
                    "grade":i["grade"],
                    "grade_type":i["grade_type"],
                    "area_info":i["area_info"],
                    "user_name":i["user_name"],
                    "user_pwd":i["user_pwd"],
                    "invite_code":i["invite_code"],
                    "school":i["school"],
                    "verify_code_img":i["verify_code_img"]}
            res = requests.post(url = url , headers = header ,data = body)
            r =res.json()
            print(r)

            assert r["code"] == int(i["code"])
            assert r["message"] == i["预期结果"]
        time.sleep(120)

if __name__ == "__main__":
    pytest.main(["-s","test_reg.py"])