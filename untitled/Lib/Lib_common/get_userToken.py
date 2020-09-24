# get_userToken
# 2020/9/22
import requests

class UserToken():
    '''获取用户的正式token，正式环境需要通过登录api获取，测试环境可以通过UID转换获取'''

    def test_getuserToken(self):
        url = 'https://jdapi.jd100.com/uc/v1/login'
        headers = {'content-type':'application/x-www-form-urlencoded','sourcetype':'1001'}
        data = {
            'account':'crmceshi007',
            'login_type':'1',
            'user_pwd':'11111'
        }
        r = requests.post(url=url, headers=headers,data=data)
        userToken= r.json()
        return userToken

if __name__ == "__main__":
    userToken = UserToken().test_getuserToken()
    print(userToken)