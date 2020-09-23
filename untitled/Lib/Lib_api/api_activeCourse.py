from Lib.Lib_common.get_loginuserToken import *
import requests

class Acitve:

    def api_getSingle(self,token,inData):
        url = 'https://jdapi.jd100.com/istudy/v1/activate/getSingle'
        headers = {'token': token}
        params = {'courseCode':inData}
        reps = requests.get(url=url, headers=headers,params=params)
        return reps.json()

    def api_activeSingle(self,token,inData):
        url = 'https://jdapi.jd100.com/istudy/v1/activate/activeSingle'
        headers = {'Content-Type':'application/json','token': token}
        json = inData
        reps = requests.post(url=url,json=json,headers=headers)
        return reps.text

if __name__ == '__main__':
    result= Acitve().api_activeSingle()
    print(result)