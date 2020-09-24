import pytest
import requests
import allure
import time
from commonlib.read_exc import Read_exc

@allure.feature("赠送用户免费正式课")
class Test_get_formal_courses:

    @allure.title("赠送用户免费正式课")
    def test_001(self,login_new):
        result = Read_exc()
        data = result.read_exc("赠送用户免费正式课")
        for i in data:
            url = i["请求地址"]
            token = login_new
            header = {"Content-Type":i["Content-Type"],
                      "token":token}
            body = {"give_guid":i["give_guid"]}
            res = requests.post(url = url,headers = header,data = body)
            r = res.json()
            print(r)
            assert r["code"] == int(i["code"])
            assert r["message"] == i["预期结果"]
        time.sleep(120)




if __name__ == "__main__":
    pytest.main(["-s","test_get_formal_courses.py"])