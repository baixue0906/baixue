import pytest
from Lib.api_common import teacherInfo
from Lib.readExcel import *
from Lib.getToken import *
import allure

class Test_teacherList:

    def setup_class(self):
        self.tmptoken = TeacherList().test_gettmptoken()
        self.opterToken = TeacherList().test_gettoken()

    @allure.feature('教师信息模块')
    @allure.story('教师列表')
    def test_teacherList1(self):
        res = teacherInfo().api_teacherList(self.opterToken)
        #print(res)
        assert res['message'] == 'Success'

    @allure.feature('教师信息模块')
    @allure.story('教师列表')
    @pytest.mark.parametrize("inData,repsData", get_excelData('Teacherlist2', 2, 4, 4, 6))
    def test_teacherList2(self,inData,repsData):
        data= json.loads(inData)
        res = teacherInfo().api_teacherList(data['opterToken'])
        assert res['message'] == repsData

if __name__ == '__main__':
    pytest.main(['-s', 'test_002.py'])
