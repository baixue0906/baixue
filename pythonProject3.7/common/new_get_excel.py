# import xlrd
#
# class read():
#     def get_excel_row(self,sheet_name):
#         data=xlrd.open_workbook('../data/testcase.xlsx')
#         table=data.sheet_by_name(sheet_name)
#         result=table.row_values(1)[1]
#         return result
#
#
# if __name__ == "__main__":
#     case = read().get_excel_row("测试读取Excel")
#     case1=eval(case)
#     print(case)
#     print(case1)
#     print(type(case))
#     print(type(case1))

# a=[0,1,2]
# b={'key':1,'key2':2}
# c=(0,1,2)
# d={0,1,2}
# print("a的数据类型：",type(a))
# print("b的数据类型：",type(b))
# print("c的数据类型：",type(c))
# print("d的数据类型：",type(d))
# print(a[1])
# print(b['key2'])

a=1
assert  b