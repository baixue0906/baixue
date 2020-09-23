import pytest
from Lib.api_common import teacherInfo
from Lib.readExcel import *
from Lib.getToken import *
import allure

@allure.feature('教师信息模块')
@allure.story('添加教师接口')
@pytest.mark.parametrize("inData,repsData",get_excelData('Addteacher2',1,6,5,7))

class Test_addTeacher:
    def setup_class(self):
        self.tmptoken = TeacherList().test_gettmptoken()
        self.opterToken = TeacherList().test_gettoken()

    def test_addTeacher(self,inData,repsData):
        res = teacherInfo().api_addTeacher(self.opterToken,inData)
        assert res['message'] == repsData

if __name__ == '__main__':
    pytest.main(['-s', 'test_001.py'])
