import requests

class UserToken():

    def test_getuserToken(self):
        url = 'https://jdapi.jd100.com/uc/v1/login'
        headers = {'content-type':'application/x-www-form-urlencoded','sourcetype':'1001'}
        data = {
            'account':'crmceshi007',
            'login_type':'1',
            'user_pwd':'11111'
                }
        r = requests.post(url=url, headers=headers,data=data)
        userToken= r.json()['data']
        return userToken

if __name__ == "__main__":
    userToken = UserToken().test_getuserToken()['token']
    print(userToken)