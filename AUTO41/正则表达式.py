# 正则表达式
# # 2020/9/16
# list = ['abcde','deabc','dabce']
# for one in list:
#     print(one)
# print(type(one))
#
# from selenium import webdriver
# webdriver.Chrome("")
GUID = 'djkdjkj'
sql1 = 'select * from W_teacherInfo where guid ="%s"'%(GUID)
sql = f'select * from W_teacherInfo where guid ="{GUID}"'
print(sql1,'\n',sql)