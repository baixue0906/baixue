# api_getCourse
# 2020/9/12
import requests
import json

class courseData:
    def api_getCourse(self,inData):
        url='https://jdapi.jd100.com/course/v1/common/getCourse'
        params = json.loads(inData)
        # print(params)
        reps =requests.get(url=url,params=params)
        return reps.json()

    def api_getTextbook(self,inData):
        url='https://jdapi.jd100.com/course/v1/common/getTextbook'
        params = json.loads(inData)
        # print(params)
        reps =requests.get(url=url,params=params)
        return reps.json()

    def api_getTerm(self,inData):
        url='https://jdapi.jd100.com/course/v1/common/getTerm'
        params = json.loads(inData)
        # print(params)
        reps =requests.get(url=url,params=params)
        return reps.json()

    def api_getVersion(self,inData):
        url='https://jdapi.jd100.com/course/v1/common/getVersion'
        params = json.loads(inData)
        # print(params)
        reps =requests.get(url=url,params=params)
        return reps.json()

    def api_getTextbookDir(self, inData):
        url = 'https://jdapi.jd100.com/course/v1/common/getTextbookDir'
        params = json.loads(inData)
        reps = requests.get(url=url, params=params)
        return reps.json()


if __name__ == '__main__':
    result= courseData().api_getTextbookDir('{\n"textbookid":"40610692",\n"platformid":"1"\n}')
    print(result)
    # print(type(result))
