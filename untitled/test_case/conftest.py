# conftest.py
# 2020/10/1 1:37 下午

#环境初始化操作
import pytest
from Lib.Lib_api.api_getOpterToken import *

# @pytest.fixture(scope='session',autouse=True)#整一个包都会执行，
# def start_demo(request):#这个一个运行该包下，任何一个test文件，都会一开始就执行的操作
#     print('---开始执行自动化测试---')
#
#     #数据清除操作:删除测试生成的垃圾数据
#     def fin():
#         print('---自动化测试---结束')
#     request.addfinalizer(fin)

#那么环境初始化，是否可以测试人员手动调用？---可以的
# @pytest.fixture(scope='function')
# def update_shop_init():#更新商铺的环境初始化
#     #1- 登录---setup_class---已经在类初始化做了--这边不需要做
#     print('---我的作用是教师列表的初始化操作---')
#     #1- 登录成功
#     token = Login().login({"username":"sq0001","password":"123456"},getToken=True)
#     #2- 列出商铺--id
#     shopId=MyShop(token).shop_list({'page':1,'limit':20})['data']['records'][0]['id']
#     #3-文件上传
#     imageInfo = MyShop(token).file_upload('123.png','../data/123.png')
#     return shopId,imageInfo#元组类型
