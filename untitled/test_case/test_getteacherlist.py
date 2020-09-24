import pytest
import allure
import requests
from Lib.Lib_common.get_excel import Read_exc
from Lib.Lib_common.get_token import TeacherList

@allure.feature ("获取教师列表")
class Test_getteacherlist:

    @allure.title("获取教师列表成功")
    def test_001(self):
        data = Read_exc().read_exc("Teacherlist")
        tmptoken = TeacherList().test_gettmptoken()
        opterToken = TeacherList().test_gettoken()
        for i in range(0,1):
            url = data[i]["请求地址"]
            headers= {'opterToken': opterToken}
            r = requests.get(url=url, headers=headers)
            assert r.json()["code"] == int(data[i]["code"])
            assert r.json()["message"] == data[i]["预期结果"]

    @allure.title("获取教师列表缺少必要参数")
    def test_002(self):
        data = Read_exc().read_exc("Teacherlist")
        result = TeacherList()
        result.test_gettmptoken()
        opterToken = result.test_gettoken()
        for i in range(1,2):
            url = data[i]["请求地址"]
            headers= {'opterToken': ''}
            r = requests.get(url=url, headers=headers)
            assert r.json()["code"] == int(data[i]["code"])
            assert r.json()["message"] == data[i]["预期结果"]

    @allure.title("获取教师列表token失效")
    def test_003(self):
        data = Read_exc().read_exc("Teacherlist")
        result = TeacherList()
        result.test_gettmptoken()
        opterToken = result.test_gettoken()
        for i in range(2, 3):
            url = data[i]["请求地址"]
            headers = {'opterToken': '123'}
            r = requests.get(url=url, headers=headers)
            assert r.json()["code"] == int(data[i]["code"])
            assert r.json()["message"] == data[i]["预期结果"]

if __name__ == "__main__":
    pytest.main = (["-s","test_getteacherlist.py"])

