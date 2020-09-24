# coding:utf-8
from ReadExcel.B_read_excle import Read_Excle
from ReadExcel.C_run_excle import Getdata
import logging
class main:
    def __init__(self):
        self.data = Getdata()

    def run(self):
        rows_count  =self.data.get_case_lines()
        for i in range(1,rows_count):
            t_number  = self.data.get_number(i)   #获取序号
            t_name = self.data.get_name(i)        #获取姓名
            t_sex = self.data.get_sex(i)          #获取性别
            t_age = self.data.get_age(i)          #获取年纪
            # t_seat = self.data.get_seat(i)      #获取座位
            # print(t_number,t_name)
            try:
                if t_sex =="女":
                    self.data.get_seat(i,"一排")      #给excel中座位字段写值
                    print("一排写入成功")
                else:
                    self.data.get_seat(i,"二排")
                    print("二排写入成功")
            except:
                print("座位写入失败")

            # try:
            #     if t_age <=35:
            #         self.data.get_school(i,"测试小学")   #给excel中学校字段写值
            #         print("小学写入成功")
            #     elif t_age <=45:
            #         self.data.get_school(i,"测试中学")
            #         print("中学写入成功")
            #     else:
            #         self.data.get_school(i,"测试高中")
            #         print("高中写入成功")
            # except:
            #     print("失败",logging)


if __name__ =='__main__':
    a = main()
    a.run()



'''
            #学校类型：985 or 211
            if (xuexiao == 985 or xuexiao ==211 or xuexiao == "海外留学生")and paiming =='是' and ganbu =='是':
                self.data.get_jibie(i,"S")
            elif (xuexiao == 985 or xuexiao == 211 or xuexiao =="海外留学生") and paiming == '是'and ganbu == '否':
                self.data.get_jibie(i, "A+")
            elif (xuexiao == 985 or  xuexiao == 211 or xuexiao == "海外留学生") and paiming == '否'and ganbu == '是':
                self.data.get_jibie(i, "A+")
            elif (xuexiao == 985 or  xuexiao == 211 or xuexiao =="海外留学生") and paiming == '否' and ganbu == '否':
                self.data.get_jibie(i, "A")
            # 学校类型：一本
            elif xuexiao =='一本' and paiming =='是' and ganbu =='是':
                self.data.get_jibie(i, "A")
            elif xuexiao =='一本' and paiming =='是'and ganbu == '否':
                self.data.get_jibie(i, "B")
            elif xuexiao =='一本' and paiming =='否'and ganbu == '是':
                self.data.get_jibie(i, "B")
            elif xuexiao =='一本' and paiming =='否' and ganbu =='否':
                self.data.get_jibie(i, "C")
            # 学校类型：二本
            elif xuexiao =='二本'and paiming =='是' and ganbu =='是':
                self.data.get_jibie(i, "B")
            elif xuexiao =='二本'and paiming =='是' and ganbu =='否':
                self.data.get_jibie(i, "C")
            elif xuexiao =='二本'and paiming =='否' and ganbu =='是':
                self.data.get_jibie(i, "C")
            elif xuexiao =='二本' and paiming =='否' and ganbu =='否':
                self.data.get_jibie(i, "D")
            # 学校类型：三本
            elif xuexiao =='三本'and paiming =='是' and ganbu =='是':
                self.data.get_jibie(i, "C")
            elif xuexiao =='三本'and paiming =='是' and ganbu =='否':
                self.data.get_jibie(i, "D")
            elif xuexiao =='三本'and paiming =='否' and ganbu =='是':
                self.data.get_jibie(i, "D")
            elif xuexiao =='三本' and paiming =='否' and ganbu =='否':
                self.data.get_jibie(i, "D")

'''