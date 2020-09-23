# encoding:utf-8
import urllib3,json
from util.runMethod import RunMethod
urllib3.disable_warnings()

class TestUser():
    run = RunMethod()

    def login(self,method,url,header,account,user_pwd,login_type,excepted):
        data = {
            "account": account,
            "user_pwd": user_pwd,
            "login_type": login_type
        }
        header =json.loads(header)
        res = self.run.run_main(method,url,data,header)
        return res

    def getUserInfo(self,login,method,url,header):
        res_token = login
        header ={
            "token": res_token
        }
        res = self.run.run_main(method,url,None,header,None)
        return res

    def getUserOrder(self,login,method,url,header,appId,page,excepted):
        res_token = login
        header ={
            "token": res_token
        }
        params = {
            "appId": appId,
            "page": page
        }
        res = self.run.run_main(method,url,None,header,params)
        # res_content = json.dumps(res).encode('utf-8').decode("unicode_escape")
        # assert excepted in res_content
        return res





