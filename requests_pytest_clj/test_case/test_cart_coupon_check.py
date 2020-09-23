# encoding:utf-8
import pytest,urllib3,requests,json
from config.conf import config_file
from util.runMethod import RunMethod
from util.parseExcelFile import *
from model.coupon import *
urllib3.disable_warnings()
class TestUserCheck():
    run = RunMethod()
    run_excel = ParseExcel()
    cart_resp_dict = TestUserCartget()

    sheet_name01 = run_excel.get_sheet_by_name('interface_api')
    run_cart_data = run_excel.get_all_values_of_sheet(sheet_name01)[5]
    run_data = run_excel.get_all_values_of_sheet(sheet_name01)[6]

    sheet_name02 = run_excel.get_sheet_by_name('cart_coupon_check')
    coupon_data = run_excel.get_all_values_of_sheet(sheet_name02)

    sheet_name03 = run_excel.get_sheet_by_name('cart_coupon')
    cart_data = run_excel.get_all_values_of_sheet(sheet_name03)

    list_run_data = []
    list_run_data.append(run_data)
    #print(list_run_data)
    list_run_data1 = []
    list_run_data1.append(run_cart_data)
    # print(list_run_data1)
    # print(cart_data)


    #@pytest.mark.parametrize('appId,userDiscountCouponId,userMoneyCouponId',coupon_data)
    @pytest.mark.parametrize('method,url,header',list_run_data)
    @pytest.mark.parametrize('appId,userDiscountCouponId,userMoneyCouponId,excepted',cart_data)
    @pytest.mark.parametrize('method1,url1,header1',list_run_data1)
    def test_getCheckInfo(self,login,method1,url1,header1,method,url,header,appId,userDiscountCouponId,userMoneyCouponId,excepted):
        res = self.cart_resp_dict.getCartCoupon(login,method1,url1,header1,appId,userDiscountCouponId,userMoneyCouponId,excepted)
        resp_cart = res['data']['activityList'][0]['productList']
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
        product = cart_resp_dictList
        #print(product)
        res_check = self.cart_resp_dict.getCheckInfo(login,method,url,header,appId,userDiscountCouponId,userMoneyCouponId,product)
        res_content =json.dumps(res_check).encode('utf-8').decode("unicode_escape")
        assert 'Success' in res_content
        print(res_check)


if __name__ =='__main__':
    pytest.main('-v',['../test_case/test_cart_coupon_check.py'])
