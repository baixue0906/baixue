import pytest
# from Lib.Lib_common.get_exceldata import *
from Lib.Lib_api.api_teacherInfo import teacherInfo
import allure
from Lib.Lib_common.compareDatabase import OperationMysql

@allure.feature('教师信息模块')
@allure.story('获取教师资质信息')
def test_getQualificationInfo1():
    res = teacherInfo().api_getQualificationInfo()
    assert res['message'] == 'Success'

@allure.story('获取教师资质信息')
def test_getQualificationInfo2():
    res = teacherInfo().api_getQualificationInfo()
    teacherName= res['data'][0]['teacher_name']
    # print(teacherName)

    # sql = "SELECT * from W_TeacherInfo WHERE real_name ='%s'" %(teacherName)
    sql = f'SELECT * from W_TeacherInfo WHERE real_name ="{teacherName}"'
    # sql = 'SELECT * from W_TeacherInfo WHERE guid ="'+GUID+'"'
    # print(sql)
    a = OperationMysql().search_one(sql)
    # print(a)  # 打印数据库查询的结果

    if res['data'][0]['teacher_name'] == a[0]['real_name'] :
        print('获取教师资质接口数据库数据对比成功')
    else:
        print("失败")


if __name__ == '__main__':
    pytest.main(['-s', 'test_getQualificationInfo.py'])
