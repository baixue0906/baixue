import pytest
import requests
import allure
from commonlib.read_exc import Read_exc

@allure.feature("PC获取课程列表")
class Test_get_formal_courses:

    @allure.title("用户未登录")
    def test_001(self):
        result = Read_exc()
        data = result.read_exc("PC获取课程列表")
        for i in range(0,1):
            url = data[i]["请求地址"]
            res = requests.get(url = url)
            r = res.json()
            print(r)
            assert r["errorNo"] == int(data[i]["errorNo"])
            assert r["error"] == data[i]["预期结果"]

    @allure.title("获取课程列表成功")
    def test_002(self,login_old):
        result = Read_exc()
        data = result.read_exc("PC获取课程列表")
        for i in range(1,2):
            url = data[i]["请求地址"]
            header = {"cookie":login_old}
            print(header)
            res = requests.get(url = url,headers = header)
            r = res.json()
            print(r)



if __name__ == "__main__":
    pytest.main(["-s","test_get_formal_courses.py"])