# test_login.py
# 2020/10/1 5:47 下午
from tools.getExcelData import *
from lib.apiLib.login import Login
import pytest

class TestLogin:
    @pytest.mark.parametrize('inData,respData',get_excelData2('登录模块','Login'))
    def test_login(self,inData,respData):
        resp=Login().login(inData,False)
        assert resp['msg']== respData['msg']

if __name__ == '__main__':
    pytest.main(['-s','test_login.py'])
