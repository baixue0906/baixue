# loginTest
# 2020/9/29
# loginTest
# 2020/9/26
import requests
import hashlib

def get_md5(psw):
        '''MD5加密操作，将字符串加密'''
        md5 = hashlib.md5()  # 实例化对象
        md5.update(psw.encode('utf-8'))  # 加密操作
        return md5.hexdigest()

def login(inData,getToken=True):
        url = 'http://121.41.14.39:8082/account/sLogin'
        inData['password']=get_md5(inData['password'])
        data = inData
        r = requests.post(url = url, data = data)
        # print(r.text),请求返回的是str类型
        # print(r.json())，请求返回的是一个字典
        # print('请求的URL:---->', r.request.url)
        # print('请求的body:---->', r.request.body)
        # print('请求的头:---->', r.request.headers)
        # print(r.raw)
        # print(r.json()['data']['token'])

        #便于后续的有依赖关系的接口，需要不同的返回信息调用
        if getToken:
                return r.json()['data']['token']
        else:
                return r.json()

result = login({'username':'sq0060','password':'470318'})
print(result)

