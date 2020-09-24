
import json

import requests
from util.excelReader import ExcelReader



class SendRequest():
    def __init__(self):
        """
        :param env:
        """
        pass

    @staticmethod
    def reqest_api(host, url, method, header, data):
        global results
        test_url = host + url
        if not test_url.startswith('http://'):
            test_url = '%s%s' % ('https://', test_url)
            # print("uuurrrlll" + str(test_url))
            #logger.info("create the url for the test : %s" % test_url)
        try:
            if method == "post":
                if data is None or data == "":
                    if header is None or header == "":
                        results = requests.post(url=test_url)
                        #logger.info("send the post request for no headers")
                    else:
                        header_dict = json.loads(header)
                        results = requests.post(url=test_url, headers=header_dict)
                        #logger.info("send the post request with headers %s" % header)
                else:
                    if header is None or header == "":
                        data_dict = json.loads(data)
                        results = requests.post(url=test_url, data=data_dict)
                        #logger.info("send the post request with data %s" % data)
                    else:
                        header_dict = json.loads(header)
                        if "application/json" in header:
                            data_dict = json.loads(data)
                            results = requests.post(url=test_url, headers=header_dict, data=json.dumps(data_dict))
                            # logger.info("send the post request with headers %s" % header)
                            # logger.info("send the post request with json data %s" % data)
                        else:
                            data_dict = json.loads(data)
                            results = requests.post(url=test_url, headers=header_dict, data=data_dict)
                            # logger.info("send the post request with headers %s" % header)
                            # logger.info("send the post request with data %s" % data)

            if method == "get":
                if data is None or data == "":
                    if header is None or header == "":
                        results = requests.get(test_url)
                        # logger.info("send the get request for no headers")
                    else:
                        header_dict = json.loads(header)
                        results = requests.get(test_url, header=header_dict)
                        # logger.info("send the get request with headers %s" % header)
                else:
                    if header is None or header == "":
                        print(type(data))
                        results = requests.get(url=test_url, params=json.loads(data))
                        # print("urlllll" + str(test_url)+"\nparams"+str(data))
                    else:
                        header_dict = json.loads(header)
                        data_dict = json.loads(data)
                        results = requests.get(test_url, header=header_dict, data=data_dict)

            if method == "put":
                if data is None or data == "":
                    if header is None or header == "":
                        results = requests.put(url=test_url)
                    else:
                        header_dict = json.loads(header)
                        results = requests.put(url=test_url, headers=header_dict)
                else:
                    if header is None or header == "":
                        data_dict = json.loads(data)
                        results = requests.put(url=test_url, data=data_dict)
                    else:
                        header_dict = json.loads(header)
                        if "application/json" in header:
                            data_dict = json.loads(data)
                            results = requests.put(url=test_url, headers=header_dict, data=json.dumps(data_dict))
                        else:
                            data_dict = json.loads(data)
                            results = requests.put(url=test_url, headers=header_dict, data=data_dict)

            return results
        except Exception.__bases__:
            print("服务器访问失败")


if __name__ == "__main__":
    host = 'https://jdapi.jd100.com' # url
    data = "../test_datas/case.xlsx" # xlsx表
    op = ExcelReader(data, 0)
    li = op.get_excel_value()
    send = SendRequest()
    for l in li:
        print((send.reqest_api(host,l["url"],l["method"],l["headers"],l["data"])).text)

