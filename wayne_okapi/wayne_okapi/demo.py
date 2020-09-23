import xlwings, json, traceback
from Http import *
import shutil, time
from operation_excel import OperationExcel
import unittest
import jsonpath
import HTMLTestReportCN
from HtmlTestRunner import HTMLTestRunner

html_result = {}
html_result['cases'] = []
success = 0
failed = 0
skip = 0

opera = OperationExcel(file_name='./cases.xls', sheet_id=1)
n = opera.get_lines
# 报告 用例条数
html_result["total"] = n - 1
print("执行用例条数:", n)
DATA = {}


class run(unittest.TestCase) :
    def test_run(self) :
        for i in range(1, n) :
            data = opera.get_row_values(i)
            html_result['environment'] = {"根路径" : "http://118.24.91.97:9000/api/", "启用全局Session" : "TRUE"},
            # print('data', data)
            url = data[2]
            # 报告 用例开始时间
            start_time = time.strftime('%H:%M:%S', time.localtime(time.time()))
            html_result["start_time"] = start_time
            try :
                if data[0] and data[2] and data[3] :
                    client = Http(url=data[2], method=data[3], body_type=data[4].lower(), timeout=5)
                # 获取依赖字段所处的列表位置--行数  list.index('data')
                if data[5] and data[6] :
                    index1 = opera.get_col_value(0).index(data[5])
                    d = opera.get_row_values(index1)
                    client1 = Http(url=d[2], method=d[3], body_type=d[4], timeout=5)
                    if d[7] :
                        client1.set_header(json.loads(d[7]))
                    if d[8] :
                        client1.set_body(json.loads(d[8]))
                    client1.send()
                    # 依赖接口返回数据  # 数据依赖 {"city":"$.city"}
                    oper_data = client1.send()
                    # 参数路径
                    path = list(eval(data[6]).values())[0]
                    # jsonpath 获取返回值中此path下的参数值
                    new_str = list(jsonpath.jsonpath(eval(oper_data), path))[0]
                    print('new_str', new_str)

                if data[7] :
                    try :
                        client.set_headers(json.loads(data[7]))
                    except Exception :
                        print("请求头执行错误")

                if data[8] :
                    try :
                        if data[6] :
                            data_body = data[8].replace(path, new_str)
                            print('data-->type', type(data))
                        else :
                            data_body = data[8]
                        client.set_body(json.loads(data_body))
                    except Exception:
                        # 报告写入excel
                        opera.write_value(i, 10, "请求正文格式不正确")
                        print('跳过：请求正文格式不正确')
                        continue

                client.send()
                print('{a}：用例执行结果--》{b}：'.format(a=data[1], b=client.res_body))
                if data[9] :
                    checks = data[9].replace('\n', '')
                    for check in checks.split(';') :
                        if check.startswith('响应状态码') :
                            check = check.replace('响应状态码', 'check_status_code')
                        elif check.startswith('响应时间小于') :
                            check = check.replace('响应状态码', 'check_response_less_than')
                        elif check.startswith('Json字段检查') :
                            check = check.replace('Json字段检查', 'check_json_path_value')
                        else :
                            continue
                        eval('client.' + check)
                        print(eval('client.' + check))
                        # client.check_json_path_value("$.total", 276.24)

                    opera.write_value(i, 10, client.res_body)
            except :
                print("用例文件加载失败")


if __name__ == '__main__' :
    # unittest.main()
    #先构造测试集,实例化测试套件
    suite = unittest.TestSuite()
    # 执行顺序是安装加载顺序：先执行test_case2，再执行test_case1
    suite.addTest(run('test_run'))
    fp = open('./wayne.html', 'wb')  # 根目录下
    HTMLTestReportCN.HTMLTestRunner(stream=fp, title='测试用例', description='接口自动化',tester='Wayne').run(suite)
