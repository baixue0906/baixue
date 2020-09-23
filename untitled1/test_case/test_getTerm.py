import pytest
import allure
import requests
from common.get_excel import Read_exc

@allure.feature ("公共获取学期模块")
class Test_getCourse:

    @allure.title("获取学期模块成功")
    def test_001(self):
        data = Read_exc().read_exc("getTerm")
        for i in range(0, 5):
            url = data[i]["请求地址"]
            params = {
                'subject': data[i]["subject"],
                'grade': data[i]["grade"],
                'version': data[i]["version"],
                'studyYear': data[i]["studyYear"]
            }

            r = requests.get(url=url,params=params)
            print(r.json())
            assert r.json()["code"] == int(data[i]["code"])
            assert r.json()["message"] == data[i]["预期结果"]

if __name__ == "__main__":
    pytest.main = (["-s", "test_getTerm.py"])

