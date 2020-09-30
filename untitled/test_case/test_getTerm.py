import pytest
from Lib.Lib_common.get_exceldata import *
from Lib.Lib_api.api_commonData import courseData
import allure,os

@allure.feature('课程数据模块')
@allure.story('获取学期模块')
@pytest.mark.parametrize("inData,repsData",get_excelData('getTextbook',1,8,4,6))
def test_getTerm(inData,repsData):
    res = courseData().api_getTextbook(inData)
    assert res['message'] == repsData

if __name__ == '__main__':
    pytest.main(['-s', 'test_getTextbook.py'])
    # #-s:输出打印信息； -q  简化输出
    # #--alluredir =../report/tmp---生成allure报告需要的源数据
    # pytest.main(['test_getTerm.py','-s','--alluredir','../report/tmp'])
    # #allure generate---生成报告
    # #方案二：allure serve---起服务----自动打开浏览器---一般设置默认浏览器
    # os.system('allure serve ../report/tmp')
    # #生成报告