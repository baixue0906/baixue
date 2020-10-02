import pytest
from Lib.Lib_common.get_exceldata import *
from Lib.Lib_api.api_teacherInfo import teacherInfo
from Lib.Lib_api.api_getOpterToken import *
import allure

@allure.feature('教师信息模块')
@allure.story('修改教师接口')
@pytest.mark.parametrize("inData,repsData",get_excelData2('Updateteacher','Update',9,11))

class Test_updateTeacher:
    def setup_class(self):
        self.tmptoken = TeacherList().test_gettmptoken()
        self.opterToken = TeacherList().test_gettoken()

    def test_updateTeacher(self,inData,repsData):
        res = teacherInfo().api_updateTeacher(self.opterToken,inData)
        assert res['message'] == repsData['message']

if __name__ == '__main__':
    pytest.main(['-s', 'test_updateTeacher.py'])
