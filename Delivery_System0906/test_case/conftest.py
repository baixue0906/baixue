# conftest.py
# 2020/10/1 8:09 下午
import pytest
from lib.apiLib.login import Login
from lib.apiLib.myShop import MyShop

@pytest.fixture(scope='function')
def update_shop_init():
    token = Login().login({'username': 'sq0060', 'password': '470318'}, True)
    shopId= MyShop(token).shop_list({'page': 1, 'limit': 1})['data']['records'][0]['id']
    imageInfo=MyShop(token).file_upload('shopImage.jpeg',r'/Users/baixue/master/Delivery_System0906/data/shopImage.jpeg')
    return shopId,imageInfo