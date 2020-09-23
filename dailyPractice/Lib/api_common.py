# api_teacherinfo
# 2020/9/12
import json
import requests

class teacherInfo:

    def api_addTeacher(self,opterToken,inData):
        url="https://jdapi.jd100.com/coursemgr/v1/addTeacherInfo"
        headers= {"Content-Type":"application/x-www-form-urlencoded","opterToken": opterToken}
        data = json.loads(inData)
        reps =requests.post(url=url,headers=headers,data=data)
        return reps.json()

    def api_teacherList(self,opterToken):
        url = 'https://jdapi.jd100.com/coursemgr/v1/getTeacherList'
        headers= {"opterToken": opterToken}
        reps = requests.get(url=url, headers=headers)
        return reps.json()

if __name__ == '__main__':
    #result= teacherInfo().api_addTeacher("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MDAxNDIzNTQsImlhdCI6MTYwMDA1NTk1NCwibmJmIjoxNjAwMDU1ODM0LCJzeXN0eXBlIjoiIiwidXNlcl9pZCI6IiJ9.ZR8BGdO9KgO0yhqAdpux42mjJS2NbVDQ8bbhu8aRheY",'{\n"display_name":"添加一号",\n"real_name":"真是一号",\n"tech_subject":"科目一号",\n"tech_grade":"高一"\n}')
    result = teacherInfo().api_teacherList('{"opterToken": 123}')
    print(result)