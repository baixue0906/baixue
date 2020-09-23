import pytest
from Lib.Lib_common.get_exceldata import *
from Lib.Lib_api.api_commonData import courseData
import allure

@allure.feature('课程数据模块')
@allure.story('公共获取教材')
@pytest.mark.parametrize("inData,repsData",get_excelData('getTerm',1,6,4,6))

def test_getTextbook(inData,repsData):
    res = courseData().api_getTerm(inData)
    assert res['message'] == repsData

if __name__ == '__main__':
    pytest.main(['-s', 'test_getTerm.py'])
