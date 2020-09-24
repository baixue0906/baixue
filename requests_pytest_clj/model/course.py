# encoding:utf-8
import urllib3,json
from util.runMethod import RunMethod
urllib3.disable_warnings()

class TestCourse():
    run = RunMethod()

    def getCourseSegment(self,method,url,header,courseCode,excepted):
        params = {
            "courseCode": courseCode,
        }
        header = json.loads(header)
        res = self.run.run_main(method,url,None,header,params)
        return res

    def getCourseSummary(self,method,url,header,grade,gradeType,excepted):
        params = {
            "grade": grade,
            "gradeType": gradeType
        }
        header = json.loads(header)
        res = self.run.run_main(method,url,None,header,params)
        return res

    def getCourseList(self,method,url,header,location,grade,version,gradeType,subject,excepted):
        params = {
            "location": location,
            "grade": grade,
            "version": version,
            "gradeType": gradeType,
            "subject": subject
        }
        header = json.loads(header)
        res = self.run.run_main(method,url,None,header,params)
        return res

    def getCourseList2(self,method,url,header,grade,subject,version,courseType,term,standard,location,excepted):
        params = {
            "grade": grade,
            "subject": subject,
            "version": version,
            "courseType": courseType,
            "term": term,
            "standard": standard,
            "location": location
        }
        header = json.loads(header)
        res = self.run.run_main(method,url,None,header,params)
        return res

    def getCourseList3(self,method,url,header,grade,subject,courseType,location,excepted):
        params = {
            "grade": grade,
            "subject": subject,
            "courseType": courseType,
            "location": location
        }
        header = json.loads(header)
        res = self.run.run_main(method,url,None,header,params)
        return res

    def getCourseCards(self,method,url,header,grade,excepted):
        params = {
            "grade": grade,
        }
        header = json.loads(header)
        res = self.run.run_main(method,url,None,header,params)
        return res

    def getCourseDetail(self,method,url,header,id,excepted):
        params = {
            "id": id,
        }
        header = json.loads(header)
        res = self.run.run_main(method,url,None,header,params)
        return res

    def getSubjectAndVersion(self,method,url,header,grade,location,excepted):
        params = {
            "grade": grade,
            "location": location
        }
        header = json.loads(header)
        res = self.run.run_main(method,url,None,header,params)
        return res

    def getSingleCourseDetail(self,method,url,header,courseCode,excepted):
        params = {
            "courseCode": courseCode,
        }
        header = json.loads(header)
        res = self.run.run_main(method,url,None,header,params)
        return res

    def getSpecialCourseDetail(self,method,url,header,courseCode,excepted):
        params = {
            "courseCode": courseCode,
        }
        header = json.loads(header)
        res = self.run.run_main(method,url,None,header,params)
        return res

    def getPackageCourseDetail(self,method,url,header,courseCode,excepted):
        params = {
            "courseCode": courseCode,
        }

        header = json.loads(header)
        res = self.run.run_main(method,url,None,header,params)
        return res

    def getCheckComment(self,login,method,url,header,courseCode,couseType,excepted):
        res_token = login
        header ={
            "token": res_token
        }
        params = {
            "courseCode": courseCode,
            "couseType": couseType

        }
        res = self.run.run_main(method,url,None,header,params)
        return res






