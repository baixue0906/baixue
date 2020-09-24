# encoding:utf-8
import pytest,urllib3,requests,json
from config.conf import config_file
from model.coupon import *
from util.parseExcelFile import *
urllib3.disable_warnings()
class TestAddCoupon():
    run_excel = ParseExcel()
    coupon_add = TestUserCartget()
    sheet_name01 = run_excel.get_sheet_by_name('interface_api')
    run_data = run_excel.get_all_values_of_sheet(sheet_name01)[4]
    sheet_name02 = run_excel.get_sheet_by_name('addCart')
    coupon_data = run_excel.get_all_values_of_sheet(sheet_name02)

    list_run_data = []
    list_run_data.append(run_data)
    print(run_data)
    print(coupon_data)


    @pytest.mark.parametrize('appId,product',coupon_data)
    @pytest.mark.parametrize('method,url,header',list_run_data)
    def test_addCoupon(self,login,url,method,header,appId,product):
        res = self.coupon_add.addCoupon(login,url,method,header,appId,product)
        res_content =json.dumps(res).encode('utf-8').decode("unicode_escape")
        #assert 'Success' in res_content
        print(res)



if __name__ =='__main__':
    pytest.main('-v',['../case_cart/test_addCart.py'])
