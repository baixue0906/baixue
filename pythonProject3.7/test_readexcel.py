# test_readexcel
# 2020/9/11

import pytest
import xlrd
import requests

def get_excelData():
    workBook = xlrd.open_workbook('../data/testcase.xlsx')
    workSheet = workBook.sheet_by_name('商品列表001')#需要执行的sheet表
    datalist=[]
    for cnt in range(1,3):
        cellData = workSheet.cell_value(cnt,4)
        repscellData = workSheet.cell_value(cnt,5)
        datalist.append((cellData,repscellData))
    return datalist

def Getlist(inData):
        url = 'https://jdapi.jd100.com/mall/v1/goods/getList'
        params = inData
        r = requests.get(url=url, params=params)
        return r.json()['message']


@pytest.mark.parametrize("inData,repsData",get_excelData())
def test_01(inData,repsData):
    assert Getlist(inData) == repsData

# print(Getlist(inData=))

# if __name__ == '__main__':
#     pytest.main(['test_getlist001.py'])
