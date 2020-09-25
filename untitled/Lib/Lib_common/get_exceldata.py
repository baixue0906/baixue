# read_excel
# 2020/9/12
#读取excel，生成包含元组的列表
import xlrd

def get_excelData(sheet_name,minrow,maxrow,col1,col2):
    workBook = xlrd.open_workbook(r"C:\Users\baixue\PycharmProjects\untitled\data\testcase.xlsx") #绝对路径
    workSheet = workBook.sheet_by_name(sheet_name)#需要执行的sheet表
    datalist=[]
    for cnt in range(minrow,maxrow):#用例读取起始行，到最终行
        cellData = workSheet.cell_value(cnt,col1)
        repscellData = workSheet.cell_value(cnt,col2)
        datalist.append((cellData,repscellData))
    return datalist
result=get_excelData('getTextbookDir',1,2,4,6)

print(result)