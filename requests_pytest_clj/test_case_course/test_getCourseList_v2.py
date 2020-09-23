# encoding:utf-8
import pytest,urllib3,requests,json
from util.parseExcelFile import *
from model.course import TestCourse
urllib3.disable_warnings()
class TestGetCourseList2():
    course_segment = TestCourse()
    run_excel = ParseExcel()
    course_data =TestCourse()

    sheet_name01 = run_excel.get_sheet_by_name('interface_api')
    run_data = run_excel.get_all_values_of_sheet(sheet_name01)[11]
    sheet_name03 = run_excel.get_sheet_by_name('getCourseList_v2')
    course_list2 = run_excel.get_all_values_of_sheet(sheet_name03)
    list_run_data = []
    list_run_data.append(run_data)


    @pytest.mark.parametrize('grade,subject,version,courseType,term,standard,location,excepted',course_list2)
    @pytest.mark.parametrize('method,url,header',list_run_data)
    def test_getCourseList(self,method,url,header,grade,subject,version,courseType,term,standard,location,excepted):
        res = self.course_data.getCourseList2(method,url,header,grade,subject,version,courseType,term,standard,location,excepted)
        res_content = json.dumps(res).encode('utf-8').decode("unicode_escape")
        print(res_content)
        assert excepted in res_content


if __name__ =='__main__':
    pytest.main('-v',['../test_case/test_getCourseList_v2.py'])
