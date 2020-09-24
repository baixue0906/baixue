import pytest
import allure
import requests
from commonlib.read_exc import Read_exc

@allure.feature("获取入学年份接口测试")
class Test_getSchoolYear:

    @allure.title("获取入学年份")
    def test_getSchoolYear(self):
        result = Read_exc()
        data = result.read_exc("获取学年年份")
        for i in data:
            self.url = i["请求地址"]
            res = requests.get(url=self.url)
            r = res.json()
            print(r)

            assert r["code"] == int(i["code"])
            assert r["message"] == i["预期结果"]

if __name__ == "__main__":
    pytest.main = (["-s","test_getSchoolYear"])


