# login.py
# 2020/10/1 5:09 下午

import requests
import hashlib

def get_md5(psw):
    '''
    :param psw: 需要加密的字符串数据
    :return: 加密结果
    '''
    md5 = hashlib.md5()#实例化对象
    md5.update(psw.encode('utf-8'))#加密操作
    return md5.hexdigest()#调用hexdigest方法,获取加密结果

class Login():
    def login(self,inData,getToken=True):
        url = 'http://121.41.14.39:8082/account/sLogin'
        inData['password']=get_md5(inData['password'])
        data = inData
        resp = requests.post(url=url,data=data)
        if getToken:
            return resp.json()['data']['token']
        else:
            return resp.json()

if __name__ == '__main__':
    token= Login().login({'username': 'sq0001', 'password': '123456'},False)
    print(token)