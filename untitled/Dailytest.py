# # import requests
# #
# # url='https://jdapi.jd100.com/course/v1/common/getCourse'
# # params = {
# #                 'studyYears': 2019,
# #                 'subject': 2,
# #                 'grades': "高一",
# #                 'version': "人教版",
# #                 'gradeType': 0,
# #                 'courseType': 1
# #             }
# # r = requests.get(url=url,params=params)
# # #print(r.json())
# # print('r.json()={}'.format(r.json()))
# # print(f'r.json()={r.json()}')
# #print(f'{r.json() =}')
#
# # print('leads_id={}'.format(leads_id))
# # print(f'leads_id={leads_id}')
# # print(f'{leads_id=}')
#
# print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))
# # 通过字典设置参数
# site = {"name": "菜鸟教程", "url": "www.runoob.com"}
# print("网站名：{name}, 地址 {url}".format(**site))
#
# # 通过列表索引设置参数
# my_list = ['菜鸟教程', 'www.runoob.com']
# print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的

# class Test_File(self):
#     def test_$FILE_NAME(self):
#         return_val = validate_data($FILE_NAME)
#         assert return_val

# get_userToken
# 2020/9/22
import requests

class UserToken():
    '''获取用户的正式token，正式环境需要通过登录api获取，测试环境可以通过UID转换获取'''

    def test_getuserToken(self):
        url = 'https://jdapi.jd100.com/uc/v1/login'
        headers = {'content-type':'application/x-www-form-urlencoded','sourcetype':'1001'}
        data = {
            'account':'crmceshi007',
            'login_type':'1',
            'user_pwd':'11111'
        }
        r = requests.post(url=url, headers=headers,data=data)
        d = r.json()
        # print(d)
        # for key,value in d.items():
        #     print("\nKey:",key)
        #     print("\nValue:",value)
        #     for key1,value1 in d['data'].items():
        #         print("\nKey1:", key1)
        #         print("\nValue1:", value1)
        # for name in d.keys():
        #     print(name)
        for name1 in d['data'].keys():
            print(list(name1))
            print(type(name1))


        return d


if __name__ == "__main__":
    d=UserToken().test_getuserToken()
    print(d)
