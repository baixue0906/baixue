# Getlist001
# 2020/9/12
import requests
import json

class Getlist:
    def api_getlist(self,inData):
        url='https://jdapi.jd100.com/mall/v1/goods/getList'
        params = json.loads(inData)
        # print(params)
        reps =requests.get(url=url,params=params)
        return reps.json()

if __name__ == '__main__':
    result= Getlist().api_getlist('{"platform": "1","grade": "g","page": "1","num": "1","goodsType": "1"}')
    print(result['message']) #需要断言的结果返回的message值
    # print(type(result))