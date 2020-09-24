print('------准备环境------')
#------1、环境确认-------
#------2、操作Excel-----
#1-请求参数----读取
import xlrd
from common.test_getlist001 import Getlist

excelDir = '../data/testcase.xls'
#打开excel文件 ,formatting_info=True保持原样式
workBook = xlrd.open_workbook(excelDir,formatting_info=True)
sheets = workBook.sheet_names()#获取所有的表名
workSheet = workBook.sheet_by_name('商品列表')#需要执行的sheet表

#取数据
#cellData = workSheet.row_values(1)
cellData = workSheet.cell(1,4).value
#print(cellData,type(cellData))

res=Getlist(cellData)
print(res)

#断言 if assert
if res['message']=='Success':
    info='pass'
else:
    info='fail'


# #2-测试结果--写入
#w文件不存在--新建excel---写入---xlwt
#文件本身存在---另存写新excel----xlutils
from xlutils.copy import copy
#1-拷贝excel对象
newWorkBook = copy(workBook)
#2-取拷贝的excel的sheet 下标
newSheet = newWorkBook.get_sheet(0)
#3-写入数据--info--newSheet.write(行下标，列下标，内容)
newSheet.write(1,11,info)
#4-保存Excel对象
newWorkBook.save('../data/res.xls')



