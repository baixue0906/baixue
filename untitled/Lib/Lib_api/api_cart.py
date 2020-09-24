# api_cart
# 2020/9/22
from Lib.Lib_common.get_userToken import *
import requests
import pytest

class JDweb:
    @pytest.fixture()
    def test_getuserToken(self):
        url = 'https://jdapi.jd100.com/uc/v1/login'
        headers = {'content-type':'application/x-www-form-urlencoded','sourcetype':'1001'}
        data = {
            'account':'crmceshi007',
            'login_type':'1',
            'user_pwd':'11111'
        }
        r = requests.post(url=url, headers=headers,data=data)
        userToken= r.json()['data']['token']
        return userToken

    def api_userCart(test_getuserToken):
        url='https://jdapi.jd100.com/ord/v2/user/cart'
        headers = {'content-type':'application/json; charset=UTF-8','token':UserToken().test_getuserToken()}
        params = {
            'appId': '1',
            'userDiscountCouponId': '0',
            'userMoneyCouponId': '0'
            }
        r = requests.get(url=url,params=params,headers=headers)
        m = r.json()['message']
        return m

if __name__ == '__main__':
    result = JDweb().api_userCart()
    print(result)