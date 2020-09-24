# api_teacherinfo
# 2020/9/12
import requests
import json

class teacherInfo:
    def api_getQualificationInfo(self):
        url='https://jdapi.jd100.com/coursemgr/v1/getQualificationInfo'
        reps =requests.get(url=url)
        return reps.json()

if __name__ == '__main__':
    result= teacherInfo().api_getQualificationInfo()
    print(result['message'])