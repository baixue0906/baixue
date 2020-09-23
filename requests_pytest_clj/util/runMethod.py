# coding: utf-8
import requests
import json
from util.excelReader import ExcelReader

class RunMethod():
    def post_main(self,url,data,header=None):
        res = None
        if header != None :
            if 'application/json' not in header:
                res = requests.post(url=url,data=data,headers=header,verify=False)
            else:
                res = requests.post(url=url,json=data,headers=header,verify=False)
        else:
            res = requests.post(url=url,data=data,verify=False)

        return res.json()


    def get_main(self,url,params=None,header=None):
        res = None
        #header = json.loads(header)
        if header != None and params !=None:
            res = requests.get(url=url, params=params, headers=header,verify=False)
        elif header != None and params ==None:
            res = requests.get(url=url, headers=header,verify=False)
        elif header == None and params !=None:
            res = requests.get(url=url,params=params,verify =False)
        else:
            res = requests.get(url=url, verify=False)
        return res.json()



    def run_main(self,method,url,data=None,header=None,params=None):
        res = None
        if method == 'post':
            res = self.post_main(url,data,header)
        else:
            res = self.get_main(url,params,header)
        return res
if __name__ =='__main__':
    run = RunMethod()
  #   data ={
  #   "account": "word001",
  #   "user_pwd": "11111",
  #   "login_type": "1"
  # }
  #   header ={"source": "web"}
  #   res = run.run_main('post','https://jdapi.jd100.com/uc/v1/login',data,header,None)
  #   print(json.dumps(res).encode('utf-8').decode('unicode_escape'))
  #   header = {"token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE4NzY4NzEwNzIsImlhdCI6MTU2OTI4NzA3MiwibmJmIjoxNTY5Mjg2OTUyLCJ1c2VyX2lkIjoiMzA0MDA2NjgifQ.GpmTBIsEqxREzEWjf9aGjTBndwY9w-m1C-McAzz-yKE"}
  #   url = "https://jdapi.jd100.com/uc/v1/getUserInfo"
  #   res = run.run_main('get',url,None,header,None)
  #   print(res)
  #
    url = "https://jdapi.jd100.com/ord/v2/user/orderList"
    header ={
"token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE4NzY4NzEwNzIsImlhdCI6MTU2OTI4NzA3MiwibmJmIjoxNTY5Mjg2OTUyLCJ1c2VyX2lkIjoiMzA0MDA2NjgifQ.GpmTBIsEqxREzEWjf9aGjTBndwY9w-m1C-McAzz-yKE"
}
    params = {
"appId":1 ,
"page": 1
}
    res = run.run_main('get',url,None,header,params)
    print(res)