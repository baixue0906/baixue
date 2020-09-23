from Http import Http
import time

class Run():

    def serch(self):

        url = 'https://xiaojieapi.cn/API/rkl.php'
        method = 'GET'
        headers = {"Accept":"application/json, text/plain, */*","Content-Type":"application/json;charset=UTF-8"}
        client = Http( url, method='GET', body_type=None, timeout=5)
        client.set_headers(headers)
        client.send()
        res = client.res_json()
        print(res)
        return res



if __name__ == '__main__':
    Run().serch()

