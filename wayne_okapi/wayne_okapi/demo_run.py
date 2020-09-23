



import xlwings, json ,traceback
from Http import *
import shutil, time
from operation_excel import OperationExcel
import unittest
import jsonpath
import re
from HtmlTestRunner import HTMLTestRunner
html_result = {}
html_result['cases'] = []
success = 0
failed = 0
skip = 0

opera = OperationExcel(file_name = './cases.xls',sheet_id=1)
n = opera.get_lines
#报告 用例条数
html_result["total"] = n-1
print("执行用例条数:", n)
DATA = {}
class run():
    def test_run(self):
        for i in range(1, n) :
            data = opera.get_row_values(i)
            html_result['environment'] = {"根路径": "http://118.24.91.97:9000/api/","启用全局Session": "TRUE"},
            # print('data', data)
            url = data[2]
            #报告 用例开始时间
            start_time = time.strftime('%H:%M:%S', time.localtime(time.time()))
            html_result["start_time"] = start_time
            try:
                if data[0] and data[2] and data[3] :
                    client = Http(url=data[2], method=data[3], body_type=data[4].lower(), timeout=5)




                if data[7] :
                    try :
                        client.set_headers(json.loads(data[7]))
                    except :
                        print("请求头执行错误")

                if data[8] :
                    try :
                        if data[6]:
                            # 数据依赖 {"city":"$.city"}
                            data_7 = opera.get_cell_value(3, 6)
                            path = list(eval(data[6]).values())[0]
                            new_str = list(jsonpath.jsonpath(eval(data_7), path))[0]
                            data = data[8].replace(path,new_str)
                            print('data-->type',type(data))
                        else:
                            data = data[8]
                        client.set_body(json.loads(data))
                    except :
                        # 报告写入excel
                        opera.write_value(i, 10, "请求正文格式不正确")
                        print('跳过：请求正文格式不正确')
                        continue


                client.send()
                print('{a}：用例执行结果--》{b}：'.format(a=data[1], b=client.res_body))
                if data[9]:
                    checks = data[9].replace('\n', '')
                    for check in checks.split(';'):
                        if check.startswith('响应状态码'):
                            check = check.replace('响应状态码', 'check_status_code')
                        elif check.startswith('响应时间小于'):
                            check = check.replace('响应状态码', 'check_response_less_than')
                        elif check.startswith('Json字段检查'):
                            check = check.replace('Json字段检查', 'check_json_path_value')
                        else:
                            continue
                        eval('client.' + check)
                        print(eval('client.' + check))
                            # client.check_json_path_value("$.total", 276.24)

                    opera.write_value(i,10,client.res_body)
            except:
                print("用例文件加载失败")
if __name__ == '__main__':
    run = run()
    run.test_run()
    # unittest.main()

    # 方案二如下：
    # #8.2.1先构造测试集,实例化测试套件
    # suite = unittest.TestSuite()
    # # 8.2.1.2将测试用例加载到测试套件中。
    # # 执行顺序是安装加载顺序：先执行test_case2，再执行test_case1
    # suite.addTest(run('test_run'))
    # # 8.2.2执行测试用例，实例化TextTestRunner类
    # # runner = unittest.TextTestRunner()
    # # # 8.2.2.2使用run()方法运行测试套件（即运行测试套件中的所有用例）
    # # runner.run(suite)
    # # file = "/Users/jw/Desktop/"+'wayne.html'
    # # fp = open('./wayne.html', 'wb')  # 根目录下
    # with open('./wayne.html', 'wb') as fp:
    #     desc = 'moban'
    #     title = '测试报告'
    #     title1 = title.encode()
    #     runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=title1, description=desc)  # 打印报告／执行
    #     runner.run(suite)