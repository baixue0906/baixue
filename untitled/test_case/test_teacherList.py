import pytest
from Lib.Lib_common.get_exceldata import get_excelData2
from Lib.Lib_api.api_teacherInfo import teacherInfo
from Lib.Lib_common.get_token import *
import allure
from Lib.Lib_common.compareDatabase import OperationMysql

@allure.feature('教师信息模块')
@allure.story('教师列表')
class Test_teacherList:

    def setup_class(self):
        self.tmptoken = TeacherList().test_gettmptoken()
        self.opterToken = TeacherList().test_gettoken()

    def test_teacherList1(self):
        res = teacherInfo().api_teacherList({'opterToken':self.opterToken})
        print(res)
        assert res['message'] == 'Success'

    @pytest.mark.parametrize("inData,repsData", get_excelData2('Teacherlist1','List',8,11))
    def test_teacherList2(self,inData,repsData):
        res = teacherInfo().api_teacherList(inData)
        assert res['message'] == repsData['message']

    # 对比接口返回数据与数据库查询的数据对比
    def test_teacherList3(self):
        res = teacherInfo().api_teacherList({'opterToken':self.opterToken})
        GUID= res['data'][1]['guid']

        sql = ("SELECT * from W_TeacherInfo WHERE guid ='%s'"%(GUID))
        # sql = "SELECT * from W_TeacherInfo WHERE guid = f'{GUID}'"
        # sql = 'SELECT * from W_TeacherInfo WHERE guid ="'+GUID+'"'
        print(sql)
        a=OperationMysql().search_one(sql)
        print(a[0]['guid'])  # 打印数据库查询接口的字段值

        if res['data'][1]['techGrade'] == a[0]['tech_grade'] and res['data'][1]['realName'] == a[0]['real_name'] and res['data'][1][
            'guid'] == a[0]['guid'] and res['data'][1]['displayName'] == a[0]['teachername']:
            print('获取老师接口数据库数据对比成功')
        else:
            print("失败")

if __name__ == '__main__':
    pytest.main(['-s', 'test_teacherList.py'])
