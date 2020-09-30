# read_excel
# 2020/9/12
#读取excel，生成包含元组的列表
import xlrd,json

def get_excelData(sheet_name,minrow,maxrow,col1,col2):
    '''
    :param sheet_name: 表名
    :param minrow: 获取用例的首行
    :param maxrow: 获取用例的最后一行
    :param col1:获取需要参数化的列数
    :param col2:获取预期结果的列数
    :return:
    '''
    workBook = xlrd.open_workbook(r"C:\Users\baixue\PycharmProjects\untitled\data\testcase.xlsx") #绝对路径123
    workSheet = workBook.sheet_by_name(sheet_name)#需要执行的sheet表
    datalist=[]
    for cnt in range(minrow,maxrow):#用例读取起始行，到最终行
        cellData = workSheet.cell_value(cnt,col1)
        repscellData = workSheet.cell_value(cnt,col2)
        datalist.append((cellData,repscellData)) #返回的数据为字符串类型，可以转换成字典类型，json.loads()
    return datalist


#可以自动识别用例数
def get_excelData2(sheetName,caseName,col1,col2):
    '''
    :param sheetName: 表名
    :param caseName: 某一个接口的用例名称
    :param col1: 需要参数化的列
    :param col2: 响应预期结果的列
    :return:
    '''
    resList = []
    #1-excel表路径
    excelDir = r'C:\Users\baixue\PycharmProjects\untitled\data\testcase.xlsx'
    #2- 打开excel对象--formatting_info=True  保持样式
    workBook = xlrd.open_workbook(excelDir)
    # workSheetNames = workBook.sheet_names()#获取所有的表名
    # print(workSheetNames)
    #3- 获取某一个指定的表
    workSheet = workBook.sheet_by_name(sheetName)
    #4- 读取一列数据
    # print(workSheet.col_values(0))
    idx=0#开始的下标
    for one in workSheet.col_values(0):
        if caseName in one:
            reqBodyData = workSheet.cell(idx,col1).value#请求body
            respData =  workSheet.cell(idx,col2).value#响应数据
            resList.append((json.loads(reqBodyData),json.loads(respData)))#封装一个列表里嵌套元组,将Excel表里的数据转化成字典格式
        idx += 1#
    return resList


if __name__ == '__main__':
    # result = get_excelData2('Updateteacher','Update',9,11)
    # print(result)
    # for one in get_excelData2('Teacherlist1','list'):
    #         print(one)
    result = get_excelData('getCourse',1,17,4,6)
    print(result)