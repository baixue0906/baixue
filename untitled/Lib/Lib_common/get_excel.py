import xlrd

class Read_exc:
    def read_exc(self,case):
        book = xlrd.open_workbook("../../data/testcase.xlsx")  #测试用例的相对路径 ,打开Excel文件读取数据
        table = book.sheet_by_name(case)   #打开测试用例表格,通过名称获取book中的一个工作表
        row_num = table.nrows #行，获取该sheet中的有效行数
        col_num = table.ncols #列，获取该sheet中的有效列数
        #print("1.测试用例共有%d行，%d列"%(row_num,col_num))
        #print("2.测试用例共有{}行，{}列".format(row_num,col_num))
        print('3.测试用例共有{}行，{}列'.format(row_num,col_num))
        #print (f'4.测试用例共有{row_num}行，{col_num}列')  #传进来的参数就直接干到字符串里了
        #print("5.测试用例共有"f'{row_num}'"行"  ","  f'{col_num}'"列")
        key = table.row_values(0)   #第一行作为key值
        s = []

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

if __name__ == "__main__":
    result = Read_exc().read_exc("getTextbook")
    print(result)








