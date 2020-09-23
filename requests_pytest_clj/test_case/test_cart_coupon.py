# encoding:utf-8
import pytest,urllib3,json
from model.coupon import *
from util.parseExcelFile import *
from util.parseSql import *

urllib3.disable_warnings()

class TestUserCartget():
    run_excel = ParseExcel()
    run_cart_coupon = TestUserCartget()
    sheet_name01 = run_excel.get_sheet_by_name('interface_api')
    run_data = run_excel.get_all_values_of_sheet(sheet_name01)[5]
    sheet_name02 = run_excel.get_sheet_by_name('cart_coupon')
    coupon_data = run_excel.get_all_values_of_sheet(sheet_name02)
    sql = Database(config_file().sql_conf())

    print(run_data)
    list_run_data = []
    list_run_data.append(run_data)


    @pytest.mark.parametrize('appId,userDiscountCouponId,userMoneyCouponId,excepted',coupon_data)
    @pytest.mark.parametrize('method,url,header',list_run_data)
    def test_getCartCoupon(self,login,method,url,header,appId,userDiscountCouponId,userMoneyCouponId,excepted):
        res = self.run_cart_coupon.getCartCoupon(login,method,url,header,appId,userDiscountCouponId,userMoneyCouponId,excepted)
        resp_cart = res['data']['activityList'][0]['productList']
        paymoney = res['data']['payMoney']
        paymony_100 = paymoney//100
        print(paymony_100)
        # res_content = json.dumps(res).encode('utf-8').decode("unicode_escape")
        # assert excepted in res_content
        #sql = self.sql.select_one_ok('INSERT INTO coupon_bijiao(result) VALUES (%s)'%paymony_100)
        cart_resp_dictList = []
        for i in resp_cart:
            if i['isCheckout'] == 1:
                childrenList = i['childrenList']
                isCheckout = i['isCheckout']
                productCode = i['productCode']
                cart_resp_dict = {}
                cart_resp_dict['productCode'] = productCode
                cart_resp_dict['isCheckout'] = isCheckout
                cart_resp_dict['childrenList'] = childrenList
                cart_resp_dictList.append(cart_resp_dict)
        #print(cart_resp_dictList)


if __name__ =='__main__':
    pytest.main('-v',['../test_case/test_cart_coupon.py'])
