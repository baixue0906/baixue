# 2020/9/11
import pytest
from common.read_excel001 import *
from cases.Getlist001 import *

@pytest.mark.parametrize("inData,repsData",get_excelData('商品列表001',1,3,4,5))

def test_getlist(inData,repsData):
    res = Getlist().api_getlist(inData)
    assert res['message'] == repsData

if __name__ == '__main__':
    pytest.main(['test_Getgoodslist.py'])
