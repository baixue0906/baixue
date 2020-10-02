# api_teacherinfo
# 2020/9/12
import json
from Lib.Lib_api.api_getOpterToken import *
import requests
from configs.config import HOST

class teacherInfo:

    def api_teacherList(self,inData):
        url = f'{HOST}/coursemgr/v1/getTeacherList'
        headers = inData
        reps = requests.get(url=url, headers=headers)
        return reps.json()

    def api_addTeacher(self,opterToken,inData):
        url= f'{HOST}/coursemgr/v1/addTeacherInfo'
        headers= {"Content-Type":"application/x-www-form-urlencoded","opterToken": opterToken}
        data = inData
        reps =requests.post(url=url,headers=headers,data=data)
        return reps.json()

    def api_updateTeacher(self,opterToken,inData,teacherGuid):
        url=f'{HOST}/coursemgr/v1/updateTeacher'
        headers= {"Content-Type":"application/x-www-form-urlencoded","opterToken": opterToken}
        inData['guid']=teacherGuid
        data = inData
        reps =requests.post(url=url,headers=headers,data=data)
        return reps.json()

    def api_getQualificationInfo(self):
        url=f'{HOST}/coursemgr/v1/getQualificationInfo'
        reps =requests.get(url=url)
        return reps.json()

if __name__ == '__main__':
    result= teacherInfo().api_teacherList({'opterToken':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MDE2OTA2NjgsImlhdCI6MTYwMTYwNDI2OCwibmJmIjoxNjAxNjA0MTQ4LCJzeXN0eXBlIjoiIiwidXNlcl9pZCI6IiJ9.Bwn0B5Ye_8lyVTnTwi_KmGrQzCU8-w8MNQVWegB5Kf4'})
    print(result['data'][55])


