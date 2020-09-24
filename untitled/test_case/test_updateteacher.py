import pytest
import allure
import requests
from Lib.Lib_common.get_excel import Read_exc
from Lib.Lib_common.get_token import TeacherList
from Lib.Lib_common.get_db import DB_Connect

@allure.feature ("更新老师")
class Test_updateteacher:

    @allure.title("更新老师成功")
    def test_001(self):
        cases = Read_exc().read_exc("Updateteacher")
        tmptoken = TeacherList().test_gettmptoken()
        opterToken = TeacherList().test_gettoken()
        guid=DB_Connect().db_connect("SELECT guid FROM `W_TeacherInfo` WHERE `teachername` = '添加一号'")[0]["guid"]
        for i in range(0, 1):
            url = cases[i]["请求地址"]
            headers = {'opterToken': opterToken,'Content-Type': cases[i]["Content-Type"]}
            data = {
                'guid':guid,
                'display_name': cases[i]["display_name"],
                'real_name': cases[i]["real_name"],
                'tech_subject': cases[i]["tech_subject"],
                'tech_grade': cases[i]["tech_grade"]
            }
            r = requests.post(url=url, headers=headers,data=data)
            assert r.json()["code"] == int(cases[i]["code"])
            assert r.json()["message"] == cases[i]["预期结果"]

    @allure.title("更新老师缺少必要参数")
    def test_002(self):
        cases = Read_exc().read_exc("Updateteacher")
        tmptoken = TeacherList().test_gettmptoken()
        opterToken = TeacherList().test_gettoken()
        for i in range(1, 2):
            url = cases[i]["请求地址"]
            headers = {'opterToken': opterToken, 'Content-Type': cases[i]["Content-Type"]}
            data = {
                'guid': '',
                'display_name': cases[i]["display_name"],
                'real_name': cases[i]["real_name"],
                'tech_subject': cases[i]["tech_subject"],
                'tech_grade': cases[i]["tech_grade"]
            }
            r = requests.post(url=url, headers=headers, data=data)
            assert r.json()["code"] == int(cases[i]["code"])
            assert r.json()["message"] == cases[i]["预期结果"]

if __name__ == "__main__":
    pytest.main = (["-s","test_updateteacher.py"])
    #py.test test/ --alluredir ./result/,在py.test执行测试的时候，指定–alluredir选项及结果数据保存的目录,./result/中保存了本次测试的结果数据
    #allure generate ./result/ -o ./report/ --clean ,将./result/目录下的测试数据生成测试报告页面：–clean选项目的是先清空测试报告目录，再生成新的测试报告。

