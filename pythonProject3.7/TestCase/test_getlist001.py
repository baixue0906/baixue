import requests
import pytest

class Testgetlist:

    def Getlist(platform,grade,page,num,goodsType):
        url = 'https://jdapi.jd100.com/mall/v1/goods/getList'
        params = {
                    'platform': platform,
                    'grade': grade,
                    'page': page,
                    'num': num,
                    'goodsType': goodsType
                }
        r = requests.get(url=url, params=params)
        return r.json()['message']




@pytest.mark.parametrize(
    "platform,grade,page,num,goodsType,expected",
            [
                ('1','g','1','1','0','Success'),
                ('','g','1','1','0','缺少必要的参数')
            ]
        )

def test_01(platform,grade,page,num,goodsType,expected):
    assert Testgetlist.Getlist(platform, grade,page,num,goodsType) == expected

if __name__ == '__main__':
    pytest.main(['test_getlist001.py'])




