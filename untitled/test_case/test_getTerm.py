import pytest
from Lib.Lib_common.get_exceldata import *
from Lib.Lib_api.api_commonData import courseData
import allure

@allure.feature('课程数据模块')
@allure.story('获取学期模块')
@pytest.mark.parametrize("inData,repsData",get_excelData('getTextbook',1,8,4,6))
def test_getTerm(inData,repsData):
    res = courseData().api_getTextbook(inData)
    assert res['message'] == repsData

if __name__ == '__main__':
    pytest.main(['-s', 'test_getTextbook.py'])
