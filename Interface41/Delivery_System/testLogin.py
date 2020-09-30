# import requests
import string
#
#
#
# def Login(inData):
#     url = 'http://121.41.14.39:8082/account/sLogin'
#     data = inData
#     r= requests.post(url = url,data=data)
#     return r.json()
#
# result = Login({'username':'sq0060','password':'470318'})
# print(result)
# yinka_bqs = ['s217053','s211266','s218735']
# # for i in yinka_bqs.columns[0:2]:
# #     var='{1}{0}{1}'.format(i,"'")
#     print(var)


# file = r'C:\Users\baixue\Desktop\test.txt'
# with open(file,encoding='UTF-8') as tools:
#     for line in tools:
#         line = line.strip()
#         l="'"+line+"'"+','
#         print(l)


while True:
    str = input("input:")
    print("'"+str.replace(",","','")+"'")




