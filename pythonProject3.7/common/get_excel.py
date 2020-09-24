import xlrd

class Read_exc:

    def read_exc(self,sheet_name):
        #book = xlrd.open_workbook("/Users/baixue/Desktop/自动化学习/testcase.xlsx")  #测试用例的绝对路径
        excel_data = xlrd.open_workbook('../data/testcase.xlsx') #测试用例的相对路径 ,打开Excel文件读取数据
        table = excel_data.sheet_by_name(sheet_name)   #打开测试用例表格,通过名称获取book中的一个工作表
        row_num = table.nrows #行，获取该sheet中的有效行数
        col_num = table.ncols #列，获取该sheet中的有效列数
        print("测试用例共有%d行,%d列"%(row_num-1,col_num))
        key = table.row_values(0)   #第一行作为key值，
        s = [] #定义一个空列表

        if row_num <=1:
            print("测试用例为空，没有测试数据")

        else:
            j = 1
            for i in range(row_num - 1):
                d = {}
                values = table.row_values(j)
                for x in range(col_num):
                    d[key[x]] = values[x]
                j += 1
                s.append(d)     #遍历表格读取所有数据
            return s

    def get_sheet_by_name(self, sheet_name):
        """获取sheet对象"""
        sheet = self.wk[sheet_name]
        return sheet

    def get_all_values_of_sheet(self, sheet):
        """获取某一个sheet页的所有测试数据，返回一个元祖组成的列表"""
        max_row_num = self.get_row_num(sheet)
        column_num = self.get_cols_num(sheet)
        all_values = []
        for row in range(2, max_row_num + 1):
            row_values = []
            for column in range(1, column_num + 1):
                value = sheet.cell(row, column).value
                if value is None:
                    value = ''
                row_values.append(value)
            all_values.append(tuple(row_values))
        return all_values

if __name__ == "__main__":
    case = Read_exc().read_exc('商品列表')
    # case01= Read_exc.get_sheet_by_name('商品列表')
    # case1= Read_exc.get_all_values_of_sheet()
    print(case)
    # print(case1)
    # print(case01)








