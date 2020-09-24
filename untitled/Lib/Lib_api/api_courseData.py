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

if __name__ == '__main__':
    result= courseData().api_getVersion('{\n"subject":"数学",\n"grade":"初中",\n"gradeType":"0",\n"studyYears":"2019",\n"courseType":"1"\n}')
    print(result['message'])
    # print(type(result))
