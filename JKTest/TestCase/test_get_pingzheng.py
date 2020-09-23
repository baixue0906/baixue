import requests
import json
import pytest
import allure
def get_pingzheng():
    s= requests.session()
    url  = "http://172.16.0.147:3039/eqpass/v1/getCertificate"
    r = s.get(url)
    return (r.text)

@allure.feature("获取上传凭证")
@pytest.mark.parametrize("expected",[("https://upload-z1.qiniup.com")])
def test_get_pingzheng1(expected):
    a= get_pingzheng()
    a= json.loads(a)
    print(a)
    assert expected == a['data']['qiniuUrl']

