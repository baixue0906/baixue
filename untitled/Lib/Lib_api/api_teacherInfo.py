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

    def api_updateTeacher(self,opterToken,inData):
        url=f'{HOST}/coursemgr/v1/updateTeacher'
        headers= {"Content-Type":"application/x-www-form-urlencoded","opterToken": opterToken}
        data = inData
        reps =requests.post(url=url,headers=headers,data=data)
        return reps.json()

    def api_getQualificationInfo(self):
        url=f'{HOST}/coursemgr/v1/getQualificationInfo'
        reps =requests.get(url=url)
        return reps.json()

if __name__ == '__main__':
    result= teacherInfo().api_updateTeacher('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MDE1Mzg4MTUsImlhdCI6MTYwMTQ1MjQxNSwibmJmIjoxNjAxNDUyMjk1LCJzeXN0eXBlIjoiIiwidXNlcl9pZCI6IiJ9.KJODZ65aIVuAZL_5TJFl-GhtVtyfFUTTbiVHCNrtnxs',{'guid': 'b915c7bc6d4a4344a76d4a69286d9c9e', 'display_name': '添加一号', 'real_name': '真是一号', 'tech_subject': '科目一号', 'tech_grade': '高一'})
    print(result)