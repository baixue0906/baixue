# encoding:utf-8
import pytest,urllib3
from config.conf import config_file
from util.runMethod import RunMethod
urllib3.disable_warnings()

run = RunMethod()
server_ip = config_file().server_ip()
@pytest.fixture(scope='session')
def login():
    url = server_ip + '/uc/v1/login'
    data = {
        "account": '15888453304',
        "user_pwd": '11111',
        "login_type":'1'
    }
    header ={
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4620.400 QQBrowser/9.7.13014.400",
        "X-Requested-With": "XMLHttpRequest",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "source": "web",
        "sourceType":"web"
    }
    #res = requests.post(url=url,data=data,headers=header,verify =False)
    res_token = run.post_main(url,data,header)['data']['token']
    #res_token =json.loads(res).encode('utf-8').decode("unicode_escape")
    #print(res_token)
    yield res_token


