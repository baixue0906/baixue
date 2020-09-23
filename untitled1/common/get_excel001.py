# -*- coding: utf-8 -*-
import os
import xlrd


class ExcelReader():
    def __init__(self,filename,sheet):
        self.filename = filename
        self.sheet = sheet

    def get_excel_value(self):
        #路径参数化
        base_dir = str(os.path.dirname(os.path.dirname(__file__)))
        base_dir = base_dir.replace('\\', '/')
        file_path = base_dir + '/data/' + self.filename
        # print(str(file_path))
        # 读取excel
        excel = xlrd.open_workbook(file_path)
        # 获取特定的sheet
        worksheet = excel.sheet_by_index(int(self.sheet))
        # 获取sheet行数
        nrows = worksheet.nrows

        # 取表头
        keys = []
        for l in range(worksheet.ncols):
            keys.append(str(worksheet.cell(0, l).value))
        # print(keys)

        # 获取所有数据
        result = []
        # 获取所有列数
        ncols = worksheet.ncols
        # 按row循环
        # 第一行为表头，略过，从第二行开始读取
        for i in range(1, nrows):
            tmp = {}
            # 按column循环
            for l in range(ncols):
                tmp[keys[l]] = worksheet.cell(i, l).value
            result.append(tmp)
        return result


if __name__ == "__main__":
    op = ExcelReader("../data/testcase.xlsx",8)
    print(op.get_excel_value())