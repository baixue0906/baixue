import requests
import json
import pytest
import allure

s= requests.session()
def clientInfo(resolution,systemVersion,network,version):
    url = "http://172.16.0.147:3039/eqpass/v1/clientInfo"
    body = {
        "resolution":resolution,
        "systemVersion":systemVersion,
        "network":network,
        "version":version
    }
    r = s.post(url,json=body)
    return r.text

@allure.feature("获取客户端信息")
@pytest.mark.parametrize("resolution,systemVersion,network,version,expected",
                         [
                             ("1920*1080","Windows 10","wifi","1.0.1.1",""),
                             ("","Windows 10","wifi","1.0.1.1",'"resolution" is not allowed to be empty'),#其中一个参数为空
                             ("1920*1080","","wifi","1.0.1.1",""),
                             ("1920*1080","Windows 10","","1.0.1.1",""),
                             ("1920*1080","Windows 10","wifi","",""),
                             (1920*1080,"Windows 10","wifi","10。1",'"resolution" must be a string'),#类型错误
                             ("1920*1080",10,"wifi","10.1",'"systemVersion" must be a string'),#类型错误
                             ("1920*1080","Windows 10","有线","",''),#链接方式为有线
                         ])
def test_clientinfo1(resolution,systemVersion,network,version,expected):
    #统计客户端信息和系统版本信息
    c = clientInfo(resolution,systemVersion,network,version)
    c = json.loads(c)
    print(type(c))
    print(c)
    assert c["message"] == expected




# if __name__ == '__main__':
#     test_clientinfo1()




