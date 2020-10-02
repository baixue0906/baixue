import pytest
from Lib.Lib_common.get_exceldata import *
from Lib.Lib_api.api_commonData import courseData
import allure

@allure.feature('课程数据模块')
@allure.story('公共获取销售课')
@pytest.mark.parametrize("inData,repsData",get_excelData('getCourse',1,17,4,6))

def test_getCourse(inData,repsData):
    res = courseData().api_getCourse(inData)
    assert res['message'] == repsData

if __name__ == '__main__':
    pytest.main(['-s', 'test_getCourse.py'])
