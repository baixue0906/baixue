# loginTest
# 2020/9/26
import requests
import hashlib

def get_md5(psw):
        '''MD5加密操作，将字符串加密'''
        md5 = hashlib.md5()  # 实例化对象
        md5.update(psw.encode('utf-8'))  # 加密操作
        return md5.hexdigest()

def login(inData):
        url = 'http://121.41.14.39:8082/account/sLogin'
        inData['password']=get_md5(inData['password'])
        data = inData
        r = requests.post(url = url, data = data)
        return r.json()

result = login({'username':'sq0060','password':'470318'})
print(result)

