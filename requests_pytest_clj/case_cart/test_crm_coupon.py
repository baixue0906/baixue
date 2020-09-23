# encoding:utf-8
import pytest
from model.coupon import *
from util.parseExcelFile import *
from util.parseSql import *
urllib3.disable_warnings()
class TestUserCartget():
    run = RunMethod()
    run_excel = ParseExcel()
    crm_coupon = TestUserCartget()
    sheet_name01 = run_excel.get_sheet_by_name('interface_api')
    run_data = run_excel.get_all_values_of_sheet(sheet_name01)[7]
    sheet_name02 = run_excel.get_sheet_by_name('crm_coupon')
    coupon_data = run_excel.get_all_values_of_sheet(sheet_name02)
    sql = Database(config_file().sql_conf())

    print(run_data)
    list_run_data = []
    list_run_data.append(run_data)
    #print(coupon_data)


    @pytest.mark.parametrize('productList,userId,optUid,optType,isOld,diffOrderList,userDiscountCouponId,userMoneyCouponId',coupon_data)
    @pytest.mark.parametrize('method,url,header',list_run_data)
    def test_crmCoupon(self,login,method,url,header,productList,userId,optUid,optType,isOld,diffOrderList,userDiscountCouponId,userMoneyCouponId):
        res = self.crm_coupon.crmCouponInfo(login,method,url,header,productList,userId,optUid,optType,isOld,diffOrderList,userDiscountCouponId,userMoneyCouponId)
        paymony = res['data']['payMoney']
        cdMoney = res['data']['cdMoney']
        mdMoney = res['data']['mdMoney']
        diffMoney = res['data']['diffMoney']
        mlMoney = res['data']['mlMoney']
        paymony_100 = paymony//100
        cdMoney_100 = cdMoney//100
        mdMoney_100 = mdMoney//100
        diffMoney_100 = diffMoney//100
        mlMoney_100 = mlMoney//100

        #print('paymony:'+str(paymony_100),'cdMoney:'+str(cdMoney_100),'mdMoney:'+str(mdMoney_100),'diffMoney:'+str(diffMoney_100),'mlMoney:'+str(mlMoney_100))
        print(paymony_100)
        #sql = self.sql.select_one_ok('INSERT INTO coupon_bijiao(result) VALUES (%s)'%paymony_100)


if __name__ =='__main__':
    pytest.main('-v',['../case_cart/test_crm_coupon.py'])
