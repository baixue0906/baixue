import pytest
from Lib.Lib_common.get_exceldata import *
from Lib.Lib_api.api_commonData import courseData
import allure,os

@allure.feature('课程数据模块')
@allure.story('公共获取销售课')
@pytest.mark.parametrize("inData,repsData",get_excelData2('getCourse','Course',9,11))

def test_getCourse(inData,repsData):
    res = courseData().api_getCourse(inData)
    assert res['message'] == repsData['message']

# if __name__ == '__main__':
#     pytest.main(['-s', 'test_getCourse.py'])

if __name__ == '__main__':
    # pytest.main(['test_myShop.py','-s'])

    #----------删除pytest在../report/tmp生成的数据------
    for one in os.listdir('../report1/tmp'):#列出对应文件夹的数据
       if 'json' in one:
           os.remove(f'../report1/tmp/{one}')

    pytest.main(['test_getCourse.py', '-s', '--alluredir', '../report1/tmp'])
    os.system('allure serve ../report1/tmp')
