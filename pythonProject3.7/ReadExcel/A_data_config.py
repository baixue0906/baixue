# coding:utf-8

'''
根据excle中字段 进行返回
对应excle中字段参数化

'''

class global_var:
    url = '0'    #请求地址
    method  = '1'      #请求方式
    platform = '2'       #性别
    grade = '3'       #年纪
    page = '4'    #学校
    num = '5'      #座位
    goodsType='6'
    code='7'
    expected='8'
    actual='9'

#返出序号
def test_url():
    return global_var.url

#返出姓名
def test_method():
    return global_var.method

#返出性别
def test_platform():
    return  global_var.platform

#返出年纪
def test_grade():
    return global_var.grade

#返出学校
def test_page():
    return global_var.page

#返回座位
def test_num():
    return global_var.num

def goodsType():
    return global_var.goodsType

def test_code():
    return global_var.code

def test_expected():
    return global_var.expected

#返回测试结果，实际结果
def test_actual():
    return global_var.actual