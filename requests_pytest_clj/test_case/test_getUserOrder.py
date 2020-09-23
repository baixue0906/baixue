# encoding:utf-8
import pytest,urllib3,requests,json
from config.conf import config_file
from util.runMethod import RunMethod
from util.parseExcelFile import *
from model.user import TestUser
urllib3.disable_warnings()
class TestGetUserInfo(object):

    run_excel = ParseExcel()
    test_userord = TestUser()
    sheet_name01 = run_excel.get_sheet_by_name('interface_api')
    run_data = run_excel.get_all_values_of_sheet(sheet_name01)[2]
    sheet_name02 = run_excel.get_sheet_by_name('order')
    order_data = run_excel.get_all_values_of_sheet(sheet_name02)

    print(run_data)
    list_run_data = []
    list_run_data.append(run_data)


    @pytest.mark.parametrize('appId,page,excepted',order_data)
    @pytest.mark.parametrize('method,url,header',list_run_data)
    def test_getUserInfo(self,login,method,url,header,appId,page,excepted):
        res = self.test_userord.getUserOrder(login,method,url,header,appId,page,excepted)
        res_content = json.dumps(res).encode('utf-8').decode("unicode_escape")
        print(res_content)

        assert excepted in res_content


if __name__ =='__main__':
    pytest.main('-v',['../test_case/test_getUserOrder.py'])
