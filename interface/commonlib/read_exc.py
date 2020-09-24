import xlrd

class Read_exc:
    def read_exc(self,case):
        book = xlrd.open_workbook(r"E:\interface\data\测试用例.xlsx")  #测试用例路径
        table = book.sheet_by_name(case)   #打开测试用例表格
        row_num = table.nrows
        col_num = table.ncols
        print("测试用例共有%d行,%d列"%(row_num,col_num))
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
    result = Read_exc()
    resu = result.read_exc("留单接口")
    print(resu)








