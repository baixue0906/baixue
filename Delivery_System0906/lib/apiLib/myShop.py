# myShop.py
# 2020/10/1 5:53 下午
import requests
from config.config import HOST
from lib.apiLib.login import Login

class MyShop:
    def __init__(self,token):
        self.headers= {'Authorization':token}

    def shop_list(self,inData):
        url = f'{HOST}/shopping/myShop'
        params = inData
        resp = requests.get(url=url,params=params,headers=self.headers)
        return resp.json()

    def file_upload(self,filename,fileDir):
        '''
        :param filename: 文件名
        :param fileDir: 文件路径
        :return: realFileName（编辑图片接口的图片名称）
        '''
        url = f'{HOST}/file'
        # 组装文件对象  (文件名，文件对象open(路径，打开方式)，文件类型)
        user_file= {'file':(filename,open(fileDir,'rb'),'image/png')}
        # 多个文件接口：{"文件名1":(),"文件名2":(),"文件名3":()}
        resp = requests.post(url=url,files=user_file,headers=self.headers)
        return resp.json()['data']['realFileName']

    def shop_update(self,inData,shopId,imageInfo):
        url = f'{HOST}/shopping/updatemyshop'
        inData['id']=shopId
        inData['image_path']= imageInfo
        inData['image']=f"{HOST}/file/getImgStream?fileName={imageInfo}"
        data = inData
        resp = requests.post(url=url,headers=self.headers,data=data)
        return resp.json()

if __name__ == '__main__':
    token= Login().login({'username': 'sq0060', 'password': '470318'},True)
    result = MyShop(token).shop_list({'page': 1, 'limit': 1})
    id = MyShop(token).shop_list({'page': 1, 'limit': 1})['data']['records'][0]['id']
    imageInfo = MyShop(token).file_upload('shopImage.jpeg',r'/Users/baixue/master/Delivery_System0906/data/shopImage.jpeg')
    print(imageInfo)