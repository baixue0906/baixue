# encoding:utf-8
import pytest,urllib3,requests,json
from config.conf import config_file
from util.parseExcelFile import *
from util.parseSql import *
urllib3.disable_warnings()

class TestSelectSql():
    sql = Database(config_file().sql_conf())
    sheet_name = ParseExcel().get_sheet_by_name('test')
    login_data = ParseExcel().get_all_values_of_sheet(sheet_name)
    print(login_data)
    @pytest.mark.parametrize('id',login_data)
    def test_select(self,id):
        res = self.sql.select_one_ok('select username from W_UserBaseInfo where id= %s'%id)
        print(res)
if __name__ =='__main__':
    pytest.main('-v',['../test_case/sql.py'])
