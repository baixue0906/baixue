# login
# 2020/9/29
import requests
import hashlib
from configs.config import HOST

def get_md5(psw):
        '''MD5加密操作，将字符串加密'''
        md5 = hashlib.md5()  # 实例化对象
        md5.update(psw.encode('utf-8'))  # 加密操作
        return md5.hexdigest()

class Login:
    def login(self,inData,getToken=True):
            url = f'{HOST}/account/sLogin'
            inData['password']=get_md5(inData['password'])
            data = inData
            r = requests.post(url = url, data = data)
            if getToken:
                    return r.json()['data']['token']
            else:
                    return r.json()

if __name__ == '__main__':
    result = Login().login({'username':'sq0060','password':'470318'})
    print(result)


