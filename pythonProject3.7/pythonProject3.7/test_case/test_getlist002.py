import pytest
import allure
import requests
from common.get_excel import Read_exc

@allure.feature("获取商品列表接口测试")
class Test_getlist():

    @allure.title("获取商品列表001")
    def test_001(self):
        result = Read_exc()
        data = result.read_exc("商品列表")

        for i in range(0,2):
            url = data[i]["请求地址"]
            params = {
                "platform": data[i]["platform"],
                "grade": data[i]["grade"],
                "page": data[i]["page"],
                "num": data[i]["num"],
                "goodsType": data[i]["goodsType"]}
            r = requests.get(url=url, params=params)
            print(r.json())
            assert r.json()['code'] == int(data[i]["code"])
            assert r.json()['message'] == data[i]["预期结果"]


if __name__ == "__main__":
    pytest.main(['../test_case/test_getlist002.py',])
