import pytest
import allure
import requests
from common.get_excel import Read_exc

@allure.feature ("获取版本数据")
class Test_getCourse:

    @allure.title("获取版本数据成功")
    def test_001(self):
        data = Read_exc().read_exc("getVersion")
        for i in range(0, 10):
            url = data[i]["请求地址"]
            params = {
                'subject': data[i]["subject"],
                'grade': data[i]["grade"],
                'gradeType': data[i]["gradeType"],
                'studyYears': data[i]["studyYears"],
                'courseType': data[i]["courseType"]
            }

            r = requests.get(url=url,params=params)
            print(r.json())
            assert r.json()["code"] == int(data[i]["code"])
            assert r.json()["message"] == data[i]["预期结果"]

if __name__ == "__main__":
    pytest.main = (["-s", "test_getVersion.py"])

