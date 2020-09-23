import pytest
import requests
from commonlib.read_exc import Read_exc
from commonlib.db_connect import DB_Connect
import allure


@allure.feature("营销产品线用户留单接口")
class Test_RetainPage:

    @allure.title("用户留单")
    def test_001(self):
        db_sql = DB_Connect()
        sql = "DELETE FROM `W_RetainPageUser` WHERE `mobile`='19900002536'"
        sql_result = db_sql.db_connect(sql)    #清理数据库，删除留单信息
        print(sql_result)

        result = Read_exc()
        data = result.read_exc("留单接口")   #读取留单接口表内容
        for i in data:
            url = i["请求地址"]
            header = {"Content-Type": i["headers"]}
            body = {"mobile":i["mobile"],
                    "invite_code": i["invite_code"],
                    "ab_test": i["ab_test"]}
            res = requests.post(url = url,headers = header,data = body)
            r = res.json()
            print(r)

            assert r["code"] == int(i["code"])
            assert r["message"] == i["预期结果"]



if __name__ == "__main__":
    pytest.main(["-s","test_retainpage.py"])



