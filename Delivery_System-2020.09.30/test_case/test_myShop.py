#-*- coding: utf-8 -*-
#@File    : test_myShop.py
#@Time    : 2020/9/28 21:28
#@Author  : xintian
#@Email   : 1730588479@qq.com
#@Software: PyCharm
from lib.apiLib.myShop import MyShop
from lib.apiLib.login import Login
import pytest,os
from tools.getExcelData import get_excelData2
class TestMyShop:#测试类---逻辑关系
    def setup_class(self):#每一个类下面所有的方法调用只运行一次
        self.token = Login().login({'username':'sq0001','password':'123456'},getToken=True)
    #定义测试方法
    @pytest.mark.parametrize('inData,respData',get_excelData2('我的商铺','listshopping'))
    def test_shop_list(self,inData,respData):#列出商铺
        res = MyShop(self.token).shop_list(inData)#商铺列出方法
        # print('body：--->', inData)
        print('实际响应结果：--->',res)
        if 'code' in res:#判断反映里是否有code这个键
            assert res['code'] == respData['code']
        else:#没有code这个键，
            assert res['error'] == respData['error']


    #2- 测试类--接口方法
    # @pytest.mark.usefixtures('update_shop_init')  # 使用初始化---不能使用返回值
    @pytest.mark.parametrize('inData,respData',get_excelData2('我的商铺','updateshopping'))
    def test_shop_update(self,inData,respData,update_shop_init):#列出商铺
        res = MyShop(self.token).shop_update(inData,update_shop_init[0],update_shop_init[1])#商铺列出方法
        #shopId,imageInfo---对应的---update_shop_init[0],update_shop_init[1]
        print('update_shop_init：--->', update_shop_init[0],update_shop_init[1])
        assert res['code'] == respData['code']


'''
pytest 输出的信息
    .    用例通过
    F    用例失败--没有语法报错
    E    语法错误

'''
if __name__ == '__main__':
   pytest.main(['test_myShop.py','-s'])
    #----------删除pytest在../report/tmp生成的数据------
   # for one in os.listdir('../report/tmp'):#列出对应文件夹的数据
   #     if 'json' in one:
   #         os.remove(f'../report/tmp/{one}')
   #
   # pytest.main(['test_myShop.py', '-s', '--alluredir', '../report/tmp'])
   # os.system('allure serve ../report/tmp')
