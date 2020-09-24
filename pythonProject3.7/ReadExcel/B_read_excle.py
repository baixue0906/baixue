# coding:utf-8
import xlrd
from xlutils.copy import copy
from ReadExcel.A_data_config import global_var
import sys
import os

curPath = os.path.dirname(__file__)+'/test_excle.xlsx'
print(curPath)

# //==> read_excle 固定语法， 修改fail_name == excle名称即可

class Read_Excle():
    def __init__(self):
        self.fail_name =os.path.dirname(__file__)+'/test_excle.xls'   #获取excle
        self.sheet_id = 0
        self.data = self.get_data()


#打开excle后取值
    def get_data(self):
        data= xlrd.open_workbook(self.fail_name)
        tables = data.sheets()[self.sheet_id]
        return tables

    def get_lines(self):
        tables = self.data
        return tables.nrows

    def get_cell_value(self,rowx,colx):
        return self.data.cell_value(rowx,colx)

#写入数据方法
    def write_value(self,rows,colx,value):
        '''
        写入excle数据
        rows,colx,value
        '''
        read_data = xlrd.open_workbook(self.fail_name)   #打开excle
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(rows,colx,value)
        write_data.save(self.fail_name)

if __name__ == '__main__':
    opers = Read_Excle()
    print(opers.get_cell_value(1,2))
