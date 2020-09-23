import pytest
import allure
import requests
from common.get_excel import Read_exc
from common.get_token import TeacherList

@allure.feature ("添加老师")
class Test_addteacher:

    @allure.title("添加老师成功")
    def test_001(self):
        cases = Read_exc().read_exc("Addteacher")
        tmptoken = TeacherList().test_gettmptoken()
        opterToken = TeacherList().test_gettoken()
        for i in range(0, 1):
            url = cases[i]["请求地址"]
            headers = {'opterToken': opterToken,'Content-Type': cases[i]["Content-Type"]}
            data = {
                'display_name': cases[i]["display_name"],
                'real_name': cases[i]["real_name"],
                'tech_subject': cases[i]["tech_subject"],
                'tech_grade': cases[i]["tech_grade"]
            }
            r = requests.post(url=url, headers=headers,data=data)
            assert r.json()["code"] == int(cases[i]["code"])
            assert r.json()["message"] == cases[i]["预期结果"]

    @allure.title("添加老师缺少必要参数")
    def test_002(self):
        cases = Read_exc().read_exc("Addteacher")
        tmptoken = TeacherList().test_gettmptoken()
        opterToken = TeacherList().test_gettoken()
        for i in range(1, 5):
            url = cases[i]["请求地址"]
            headers = {'opterToken': opterToken,'Content-Type': cases[i]["Content-Type"]}
            data = {
                'display_name': cases[i]["display_name"],
                'real_name': cases[i]["real_name"],
                'tech_subject': cases[i]["tech_subject"],
                'tech_grade': cases[i]["tech_grade"]
            }
            r = requests.post(url=url, headers=headers,data=data)
            assert r.json()["code"] == int(cases[i]["code"])
            assert r.json()["message"] == cases[i]["预期结果"]


if __name__ == "__main__":
    pytest.main = (["-s","test_addteacher.py"])
