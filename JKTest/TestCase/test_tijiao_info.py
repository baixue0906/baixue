import requests

import json

import pytest
import allure

s =requests.session()
def tijiao_info(serviceId,camera,microphone,voice,time,whiteBoard):
    url = "http://172.16.0.147:3039/eqpass/v1/diagnoseresult/result"
    h = {
        "Content-Type":"application/json"
    }
    par = {
        "serviceId": serviceId,
        "camera": camera,
        "microphone": microphone,
        "voice": voice,
        "time": time,
        "whiteBoard": whiteBoard,
    }
    r = s.post(url, json=par,headers = h)
    return r.text
@pytest.mark.parametrize('serviceId,camera,microphone,voice,time,whiteBoard,expected',
                         [
                             ("","1","1","1","周六全天",'true',''),#服务id为空
                             (2222,"1","1","1","周六全天",'true','"serviceId" must be a string'),#服务id类型错误
                             ("","1","1","1","",'','diagnoseresult validation failed: whiteBoard: Cast to Boolean failed for value \"\" at path \"whiteBoard\"'),#手写板参数错误
                             ("","","1","1","周六全天",'true','"camera" is not allowed to be empty'),#摄像头参数为空
                             ("","","","","",'','"camera" is not allowed to be empty'),#所有信息为空
                             ("",123,"","","",'','"camera" must be a string'),#摄像头信息参数错误
                             ("",False,"","","",'','"camera" must be a string'),#摄像头信息参数错误
                             ("","1","","","",'','"microphone" is not allowed to be empty'),#麦克风参数为空
                             ("","1",True,"","",'','"microphone" must be a string'),#麦克风参数类型错误
                             ("","1","1","","",'','"voice" is not allowed to be empty'),#耳机参数为空
                             ("","1","1",123,"",'','"voice" must be a string'),#耳机参数类型错误
                             ("","1","1",True,"",'','"voice" must be a string'),#耳机参数类型错误
                             ("","1","1","1","",'1',''),#帮助时间为空
                             ("","1","1","1",114,'1','"time" must be a string'),#帮助时间类型错误
                             ("1","1","1","1","周五10:30-12:30",'1','')
                         ]
                         )
@allure.feature("提交硬件信息")
@allure.story("异常情况")
def test_tijiao_info1(serviceId,camera,microphone,voice,time,whiteBoard,expected):
    #s = unlogin_fixture
    a = tijiao_info(serviceId,camera,microphone,voice,time,whiteBoard)
    a = json.loads(a)
    a = a["message"]
    assert  a == expected


@pytest.mark.parametrize('serviceId,camera,microphone,voice,time,whiteBoard,expected',
                         [
                             ("1","1","1","1","随时",'true',"")
                         ]
                         )
@allure.feature("提交硬件信息")
@allure.story("正常情况")
def test_tijiao_info2(serviceId,camera,microphone,voice,time,whiteBoard,expected):
    #s = unlogin_fixture
    a = tijiao_info(serviceId,camera,microphone,voice,time,whiteBoard)
    a = json.loads(a)
    a = a["message"]
    assert  a == expected



