import  configparser
import os


#获取config配置文件
def getConfig(section,key):
    config=configparser.ConfigParser()
    path=os.path.split(os.path.realpath(__file__))[0]+'\dbconfig.ini'
    print("=========="+path)
    filename='dbconfig.ini';
    config.read(path,encoding='utf-8')
    return config.get(section,key)


print(getConfig("easyweb_new_trans","dbname"))