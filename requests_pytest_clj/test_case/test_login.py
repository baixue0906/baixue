# encoding:utf-8
import pytest,urllib3,requests,json
from config.conf import config_file
from util.parseExcelFile import *
from util.runMethod import RunMethod
from model.user import TestUser
urllib3.disable_warnings()

class TestLoginCase():
    run_excel = ParseExcel()
    user_login = TestUser()
    sheet_name = run_excel.get_sheet_by_name('login')
    sheet_name02 = run_excel.get_sheet_by_name('interface_api')
    login_data = list(run_excel.get_all_values_of_sheet(sheet_name))
    run_data = run_excel.get_all_values_of_sheet(sheet_name02)[0]
    list_rundata = []
    list_rundata.append(run_data)
    print(list_rundata)
    print(login_data)


    @pytest.mark.parametrize('account,user_pwd,login_type,excepted',login_data)
    @pytest.mark.parametrize('method,url,header',list_rundata)
    def test_login(self,method,url,header,account,user_pwd,login_type,excepted):
        res = self.user_login.login(method,url,header,account,user_pwd,login_type,excepted)
        res_content =json.dumps(res).encode('utf-8').decode("unicode_escape")
        print(res_content)
        # if excepted in res_content:
        #     print("pass")
        #assert excepted in res_content
