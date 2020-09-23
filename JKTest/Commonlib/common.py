import requests
import urllib3
import time



urllib3.disable_warnings()
#s =requests.session()
def login(s):
    url = "http://172.16.0.147:3039/eqpass/v1/login"
    h = {
        "Content-Type":"application/json"
    }
    par = {
        "username": "ldd548686",
        "password": "11111",
        "passwordEn": "",
        "remember": True,
        "role": "0"
    }
    r = requests.post(url,json = par,headers = h)
    #print(r.headers)
    return r.headers
def add_question(s):
    # m = login()
    # m1 = m['Set-Cookie']
    # print(m1)
    T = time.time()
    T = int(round(T * 1000))
    t = str(T)
    images = "ldd548686_"+t+"_JEYQuestion.jpg"

    url = "http://172.16.0.147:3039/eqpass/v1/addPhotoQuestion"
    h = {
        "Content-Type":"application/json",
        # 'Set-Cookie':m1
    }
    par = {
        "content":"123ssfff",
        "duration":0,
        "exerciseId":"2434756",
        "imageName":images,
        "originType":"secion",
        "schemeId":"115938",
        "scoreLevel":"C",
        "videoPos":0,
        "voiceName":""
    }

    r1 = requests.post(url,headers = h,json=par)
    print(r1.text)
    return r1.text








if __name__ == '__main__':
    s =requests.session()
    login(s)
    add_question(s)






