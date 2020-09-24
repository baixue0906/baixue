# encoding:utf-8
import urllib3,json
from util.runMethod import RunMethod
urllib3.disable_warnings()

class TestUserCartget():
    run = RunMethod()

    def getCartCoupon(self,login,method,url,header,appId,userDiscountCouponId,userMoneyCouponId,excepted):
        res_token = login
        header ={
            "token": res_token
        }
        params = {
            "appId": appId,
            "userDiscountCouponId": userDiscountCouponId,
            "userMoneyCouponId": userMoneyCouponId
        }
        res = self.run.run_main(method,url,None,header,params)
        return res
    def getCartList(self,login,method,url,header,appId,excepted):
        res_token = login
        header ={
            "token": res_token
        }
        params = {
            "appId": appId,
        }
        res = self.run.run_main(method,url,None,header,params)
        return res
    def addCoupon(self,login,url,method,header,appId,product):
        res_token = login
        header ={
            "token": res_token,
            "content-type": "application/json"
        }
        data_json = {
            "appId": appId,
            "product": json.loads(product)
            #"product":product
        }
        #print(data_json['product'])

        data_json = json.dumps(data_json)
        res = self.run.run_main(method,url,data_json,header,None)
        #res_content = json.dumps(res).encode('utf-8').decode("unicode_escape")
        return res

    def crmCouponInfo(self,login,method,url,header,productList,userId,optUid,optType,isOld,diffOrderList,userDiscountCouponId,userMoneyCouponId):
        res_token = login
        header ={
            "token": res_token,
            "content-type": "application/json"
        }

        data_json = {
            "productList": json.loads(productList),
            "userId": userId,
            "optUid": optUid,
            "optType":optType,
            "isOld":isOld,
            "diffOrderList":json.loads(diffOrderList),
            "userDiscountCouponId":userDiscountCouponId,
            "userMoneyCouponId":userMoneyCouponId
        }
        data_json=json.dumps(data_json)
        res = self.run.run_main(method,url,data_json,header,None)
        return res
    def getCheckInfo(self,login,method,url,header,appId,userDiscountCouponId,userMoneyCouponId,product):
        res_token = login
        header ={
            "token": res_token,
            "content-type": "application/json"
        }
        data = {
            "appId": appId,
            #"product":json.loads(self.product),
            "product": product,
            "userDiscountCouponId": userDiscountCouponId,
            "userMoneyCouponId":userMoneyCouponId
        }
        data_json=json.dumps(data)
        res = self.run.run_main(method,url,data_json,header,None)
        #res_content = json.dumps(res).encode('utf-8').decode("unicode_escape")
        return res





