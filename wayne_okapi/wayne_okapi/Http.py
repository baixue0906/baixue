#requests类库 封装 --- 1. 调用更简单    2.调用接口  测试接口 一体
#ddt   行为驱动开发   用户希望使用的 --- 开发

# 类常量--可选范围

#variable_regexp = r"\$([\w_]+)"

import requests, jsonpath
import config

class Method:
    GET = 'GET'
    POST = 'POST'

class BodyType:
    URL_ENCODE = 'url_encode'
    JSON = 'json'
    XML = 'xml'
    FILES = 'files'

class Http:

    Session = requests.session()


    def __init__(self, url, method='GET', body_type=None, timeout=5):
        self.url = url
        self.method = method
        self.body_type = body_type
        self.headers = {}
        self.body = {}
        self.params = {}
        self.res = None
        self.timeout = timeout
        self.flag = 0

    def set_header(self, key, value):
        self.headers[key] = value

    def set_headers(self, headers):
        if isinstance(headers, dict):
            self.headers = headers
        else:
            raise Exception('请求头请以字典形式传递')

    def set_params(self, params):
        if isinstance(params, dict):
            self.params = params
        else:
            raise Exception('URL参数列表请以字典形式传递')

    def set_body(self, body):
        if isinstance(body, dict):
            if self.body_type == 'url_encode':
                self.set_header("Content-Type", "application/x-www-form-urlencoded")
            elif self.body_type == 'json':
                self.set_header("Content-Type", "application/json")
            self.body = body
        else:
            raise Exception('请求正文请以字典形式传递')

    def send(self):
        if self.method == 'GET':
            if config.CONFIG.get('启用全局Session'):
                self.res = Http.Session.get(url=self.url, headers=self.headers, params=self.params, timeout=self.timeout)
            else:
                self.res = requests.get(url=self.url, headers=self.headers, params=self.params, timeout=self.timeout)
        elif self.method == 'POST':
            if self.body_type == 'url_encode':
                if config.CONFIG.get('启用全局Session'):
                    self.res = Http.Session.post(url=self.url, headers=self.headers, data=self.body, timeout=self.timeout)
                else:
                    self.res = requests.post(url=self.url, headers=self.headers, data=self.body, timeout=self.timeout)
            elif self.body_type == 'json':
                if config.CONFIG.get('启用全局Session'):
                    self.res = Http.Session.post(url=self.url, headers=self.headers, json=self.body, timeout=self.timeout)
                else:
                    self.res = requests.post(url=self.url, headers=self.headers, json=self.body, timeout=self.timeout)
            elif self.body_type == 'files':
                if config.CONFIG.get('启用全局Session'):
                    self.res = Http.Session.post(url=self.url, headers=self.headers, files=self.body, timeout=self.timeout)
                else:
                    self.res = requests.post(url=self.url, headers=self.headers, files=self.body, timeout=self.timeout)
            else:
                raise Exception('不支持的请求正文类型')
        else:
            raise Exception('不支持的请求方法类型')

    @property
    def status_code(self):
        if self.res:
            return self.res.status_code
        else:
            return None

    @property
    def res_times(self):
        if self.res:
            return round(self.res.elapsed.total_seconds()*1000)
        else:
            return None

    @property
    def res_body(self):
        if self.res:
            # return self.res.text
            return '返回值[{b}]'.format(b = self.res.text)

        else:
            return None

    def res_json(self):
        if self.res:
            return self.res.json()
        else:
            return None

    def json_value(self, path):
        if self.res:
            object = jsonpath.jsonpath(self.res_to_json(), path)
            if object:
                return object[0]
        return None


    def check_status_code(self, exp):
        try:
            assert self.status_code == exp
            return '响应状态正确'
        except:
            self.flag += 1
            return '响应状态码验证失败,预期结果：[{a}]，实际结果：[{b}]'.format(
                a=exp, b=self.status_code
            )

    def check_res_times_less_than(self, exp):
        try:
            assert self.res_times <= exp
            return '响应时间合法'
        except:
            self.flag += 1
            return '响应时间超长,预期结果：[{a}]，实际结果：[{b}]'.format(
                a=exp, b=self.res_times)


    #根据jsonpath表达式，获取json节点值，断言
    def check_json_value(self, path, exp):
        r = jsonpath.jsonpath(self.res_json(), path)
        if r:
            try:
                assert r[0] == exp
                return 'Json值检查正确'
            except:
                self.flag += 1
                return 'Json节点检查失败,预期结果：[{a}]，实际结果：[{b}]'.format(
                    a=exp, b=r[0])
        else:
            self.flag += 1
            return 'json节点{path}不存在'.format(path=path)

    def set_variable(self, key, path):
        r = jsonpath.jsonpath(self.res_json(), path)
        if r:
            config.CONFIG[key] = r[0]
if __name__ == '__main__':

    url = 'http://test-morder.huashenghaoche.com/hshcmorder/api/order/createOrder'

    header = {"token":"wangshuguang","tokentype":"app","Accept":"application/json, text/plain, */*","Content-Type":"application/json;charset=UTF-8"}
    icbc_body_create_order = {"carId" : "589", "provinceCode" : 500000, "cityCode" : 500100, "deptCode" : "050101",
                              "deptId" : "120007003001", "deptName" : "重庆永川门店", "licenseId" : 18, "licenseName" : "渝A",
                              "sid" : "",
                              "utm_source" : "A01_006_006", "startPercentPlus" : 0.1, "businessType" : "26",
                              "schemeCode" : "1ee8cd65-3f02-46fd-883f-e9c29f689a87", "leaseTerm" : 36,
                              "productId" : 819, "finalPayment" : 0,
                              "projectName" : "吴杰E分期36期方案-3新", "invest" : 161056, "downPayment" : 17900,
                              "monthPayment" : 5770, "order_channel" : 2, "color" : "红色"}
    print(type(icbc_body_create_order))
    client = Http(url=url, method='POST', body_type='json', timeout=5)
    client.set_headers(header)
    client.set_body(icbc_body_create_order)
    client.send()
    # client.check_res_time_less_than(200)
    # client.check_status_code(400)
    print(client.res_json())