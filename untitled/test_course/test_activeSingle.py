import pytest
from Lib.Lib_api.api_activeCourse import *
from Lib.Lib_common.get_loginuserToken import *
from Lib.Lib_common.compareDatabase import OperationMysql

class Test_getSingle:

    def setup_class(self):
        self.Token = UserToken().test_getuserToken()['token']

    def test_activeSingle(self):
        inData = {
                    "courseCode": "201090502",
                    "activeCode": "5836786331670340",
                    "textbookCode": "2010905022083",
                    "textbook": "安徽版",
                    "moduleSelect": True,
                    "termCode": [
                        "2010905022083410"
                    ]
                }

        res = Acitve().api_activeSingle(self.Token,inData)
        print(res)

if __name__ == '__main__':
    pytest.main(['-s', 'test_activeSingle.py'])
    #1111111