import pytest
import allure
import requests
from common.get_excel import Read_exc

@allure.feature ("公共获取销售课")
class Test_getCourse:

    @allure.title("获取销售课成功")
    def test_001(self):
        data = Read_exc().read_exc("getCourse")
        for i in range(0, 16):
            url = data[i]["请求地址"]
            params = {
                    'studyYears': data[i]["studyYears"],
                    'subject': data[i]["subject"],
                    'grades': data[i]["grades"],
                    'version': data[i]["version"],
                    'gradeType': data[i]["gradeType"],
                    'courseType': data[i]["courseType"]
                }
            r = requests.get(url=url,params=params)
            print(r.json())
            assert r.json()["code"] == int(data[i]["code"])
            assert r.json()["message"] == data[i]["预期结果"]

if __name__ == "__main__":
    pytest.main = (["-s", "test_getCourse.py"])

