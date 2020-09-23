import pytest
from Lib.Lib_common.get_exceldata import *
from Lib.Lib_api.api_teacherInfo import teacherInfo
from Lib.Lib_common.get_token import *
import allure
from Lib.Lib_common.compareDatabase import OperationMysql

@allure.feature('教师信息模块')
@allure.story('添加教师接口')


class Test_addTeacher:
    def setup_class(self):
        self.tmptoken = TeacherList().test_gettmptoken()
        self.opterToken = TeacherList().test_gettoken()

    @pytest.mark.parametrize("inData,repsData", get_excelData('Addteacher', 1, 6, 5, 7))
    def test_addTeacher1(self,inData,repsData):
        res = teacherInfo().api_addTeacher(self.opterToken,inData)
        assert res['message'] == repsData

    @pytest.mark.parametrize("inData,repsData", get_excelData('Addteacher', 1, 2, 5, 7))
    def test_addTeacher2(self,inData,repsData):
        res = teacherInfo().api_addTeacher(self.opterToken,inData)
        GUID= res['data']['guid']
        print(GUID)

        sql = 'SELECT * from W_TeacherInfo WHERE guid ="'+GUID+'"'
        print(sql)
        a=OperationMysql().search_one(sql)
        print(a[0]['guid'])  # 打印数据库查询接口的字段值

        if res['data']['techGrade'] == a[0]['tech_grade'] and res['data']['realName'] == a[0]['real_name'] and res['data'][
                    'guid'] == a[0]['guid'] and res['data']['displayName'] == a[0]['teachername']:
            print('添加老师接口数据库数据对比成功')
        else:
            print("失败")

if __name__ == '__main__':
    pytest.main(['-s', 'test_addTeacher.py'])
