import requests
from Lib.Lib_common.compareDatabase import OperationMysql

class UserToken():
    # 获取临时TmpToken
    def test_gettmptoken(self):
        #通过数据库查询对应的用户
        # sql = "SELECT id from W_UserBaseInfo WHERE mobile = '18800000099'"  #通过手机号查询userID
        sql = "SELECT id from W_UserBaseInfo WHERE username = 'JD1600479191588755'" #通过用户名查询userID
        a = OperationMysql().search_one(sql)
        userid= a[0]['id']
        # print(userid)

        url = 'https://jdapi.jd100.com/uc/v1/getTmpToken'
        headers = {'Content-Type': 'application/x-www-form-urlencoded','uid': str(userid)}
        r = requests.post(url=url, headers=headers)
        tmptoken= r.json()['data']['tmpToken']
        return tmptoken

    # 获取正式token，Token
    def test_gettoken(self):
        url = 'https://jdapi.jd100.com/uc/v1/getToken'
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = {'tmp_token':UserToken().test_gettmptoken()}
        r = requests.post(url=url, headers=headers,data=data)
        token = r.json()['data']['token']
        return token

if __name__ == "__main__":
    tmptoken = UserToken().test_gettmptoken()
    Token= UserToken().test_gettoken()
    print(Token)
