import pytest
import allure
import requests
from common.get_excel import Read_exc

@allure.feature ("获取教师资质列表")
class Test_getqualificationinfo:

    @allure.title("获取教师资质列表成功")
    def test_001(self):
        data = Read_exc().read_exc("Qualificationinfo")
        for i in range(1,1):
            url = data[i]["请求地址"]
            r = requests.get(url=url)
            assert r.json()["code"] == int(data[i]["code"])
            assert r.json()["message"] == data[i]["预期结果"]

if __name__ == "__main__":
    pytest.main = (["-s", "test_qualification.py"])

