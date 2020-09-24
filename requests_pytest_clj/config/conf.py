# encoding:utf-8
import os
class config_file(object):
    def server_ip(self):
        #环境地址，保存在字典中
        server_address ={
            'test_ip' :'https://jdapi.jd100.com'
        }
        return server_address['test_ip']
    def sql_conf(self):
        #测试库配置
        sql_config ={
            'host': '192.168.20.156',
            'port': 3306,
            'user': 'test_user',
            'passwd': 'test_user!@#123',
            'db': 'easyweb_new_trans',
           # 'db': 'order_system',
            'charset': 'utf8'
        }
        #线上正式库配置
        # sql_config ={
        #     'host': '192.168.1.181',
        #     'port': 3306,
        #     'user': 'cuilianjing',
        #     'passwd': '#cuilianjing',
        #     'db': 'easyweb',
        #     'charset': 'utf8'
        # }



        return sql_config
    def dir_conf(self):
        # 项目根目录
        ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # 报告目录
        REPORT_DIR = os.path.join(ROOT_DIR, 'report')
        # 测试数据所在目录
        DATA_Path = os.path.join(ROOT_DIR, 'test_datas', 'tcData.xlsx')
        return ROOT_DIR, REPORT_DIR ,DATA_Path

