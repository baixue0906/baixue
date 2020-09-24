# coding:utf-8

'''
根据excle中字段 进行返回
对应excle中字段参数化

'''

class global_var:
    number = '0'    #序号
    name = '1'      #姓名
    sex = '2'       #性别
    age = '3'       #年纪
    school = '4'    #学校
    seat = '5'      #座位


#返出序号
def test_number():
    return global_var.number

#返出姓名
def test_name():
    return global_var.name

#返出性别
def test_sex():
    return  global_var.sex

#返出年纪
def test_age():
    return global_var.age

#返出学校
def test_school():
    return global_var.school

#返回座位
def test_seat():
    return global_var.seat