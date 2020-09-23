# encoding:utf-8
import pytest,urllib3,json
from model.coupon import *
from util.parseExcelFile import *
from util.parseSql import *
from model.coupon import *

urllib3.disable_warnings()

class TestUserCartget():
    run_excel = ParseExcel()
    run_cart_list = TestUserCartget()
    sheet_name01 = run_excel.get_sheet_by_name('interface_api')
    run_data = run_excel.get_all_values_of_sheet(sheet_name01)[8]
    sheet_name02 = run_excel.get_sheet_by_name('cartList')
    cart_data = run_excel.get_all_values_of_sheet(sheet_name02)
    sql = Database(config_file().sql_conf())

    print(cart_data)
    list_run_data = []
    list_run_data.append(run_data)


    @pytest.mark.parametrize('appId,excepted',cart_data)
    @pytest.mark.parametrize('method,url,header',list_run_data)
    def test_getCartCoupon(self,login,method,url,header,appId,excepted):
        res = self.run_cart_list.getCartList(login,method,url,header,appId,excepted)
        res_content = json.dumps(res).encode('utf-8').decode("unicode_escape")
        assert excepted in res_content
        print(res_content)



if __name__ =='__main__':
    pytest.main('-v',['../test_case/test_cart_coupon.py'])
