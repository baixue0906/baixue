# cookieTest
# 2020/9/28
# import requests
# def login(inData):
#      url = 'http://120.55.190.222:7080/api/mgr/loginReq'
#      data = inData
#      resp = requests.post(url=url,data=data)
#      print(resp.text)
#      #方案一：原生态cookie----如果后续的接口直接使用这个cookie，不增加其他参数--直接使用
#      print(resp.cookies)
#      #方案二：如果后续的接口使用这个cookie，再增加其他参数认证，重新封装cookies
#      print(resp.cookies['sessionid'])

#      return resp.cookies,resp.cookies['sessionid']
#
# #方案一：
# #原生态cookie
# cookie1 = login({'username':'auto','password':'sdfsdfsdf'})[0]
# #其他接口请求
# resp = requests.post('路径',cookies= cookie1)
#
# #方案二：
# session = login({'username':'auto','password':'sdfsdfsdf'})[1]
# user_cookie = {'sessionid':session,'token':'123456'}
# #其他接口请求
# resp = requests.post('路径',cookies = user_cookie)
#
#
# login({'username':'auto','password':'sdfsdfsdf'})

#https请求
import requests
requests.packages.urllib3.disable_warnings()
def login(inData):
     url = 'https://120.55.190.222/api/mgr/loginReq'
     data = inData
     resp = requests.post(url=url,data=data,verify=False)
     print(resp.text)

login({'username': 'auto', 'password': 'sdfsdfsdf'})

#字典---json,json.dumps()
#json---字典，json.loads()