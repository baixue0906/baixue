# test_myShop.py
# 2020/10/1 6:40 下午
import pytest
from lib.apiLib.login import Login
from lib.apiLib.myShop import MyShop
from tools.getExcelData import get_excelData2

class TestMyShop:
    def setup_class(self):
        self.token = Login().login({'username': 'sq0060', 'password': '470318'},True)

    @pytest.mark.parametrize('inData,respData',get_excelData2('我的商铺','listshopping'))
    def test_shop_list(self,inData,respData):
        resp = MyShop(self.token).shop_list(inData)
        if 'code' in resp:
            assert resp['code']==respData['code']
        else:
            assert resp['error']==respData['error']

    @pytest.mark.parametrize('inData,respData', get_excelData2('我的商铺', 'updateshopping'))
    def test_shop_update(self,inData,respData,update_shop_init):
        resp= MyShop(self.token).shop_update(inData,update_shop_init[0],update_shop_init[1])
        assert resp['code']==respData['code']


if __name__ == '__main__':
    pytest.main(['-s','test_myShop.py'])


