# coding:utf-8
import A_data_config
from B_read_excle import Read_Excle
class Getdata:

    def __init__(self):
        self.opera_excel = Read_Excle()


    #去获取excle行数，就是case个数
    def get_case_lines(self):
        return self.opera_excel.get_lines()

    #获取excle中序号
    def get_number(self,rowx):
        number_x =int(A_data_config.test_number())
        number_y = self.opera_excel.get_cell_value(rowx,number_x)
        return number_y

    # 获取excle中姓名
    def get_name(self,rowx):
        name_x =int(A_data_config.test_name())
        name_y = self.opera_excel.get_cell_value(rowx,name_x)
        return name_y

    #获取excle中性别
    def get_sex(self,rowx):
        sex_x =int(A_data_config.test_sex())
        sex_y = self.opera_excel.get_cell_value(rowx,sex_x)
        return sex_y

    #获取excle中年纪
    def get_age(self,rowx):
        age_x =int(A_data_config.test_age())
        age_y = self.opera_excel.get_cell_value(rowx,age_x)
        return age_y

   #写入excle中学校
    def get_school(self,rowx,value):
        col =int(A_data_config.test_school())
        self.opera_excel.write_value(rowx,col,value)   #调用写入方法

    #写入excle中座位
    def get_seat(self, rowx, value):
        col = int(A_data_config.test_seat())
        self.opera_excel.write_value(rowx, col, value)  # 调用写入方法
