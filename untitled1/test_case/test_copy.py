import pytest
import allure
import requests
from common.get_excel import Read_exc

class TestgetTerm:
    def getTerm(subject,grade,version,studyYear):
        url = 'https://jdapi.jd100.com/course/v1/common/getTerm'
        params = {
                    'subject': subject,
                    'grade': grade,
                    'version': version,
                    'studyYear': studyYear
                }
        r = requests.get(url=url, params=params)
        return r.json()['message']
@pytest.mark.parametrize("subject,grade,version,studyYear,expected",
                        [
                        ('数学','初中','人教版','2019','Success'),
                        ('','初中','人教版','2019','Parameter Invalid')
                        ]
                        )

def test_01(subject,grade,version,studyYear,expected):
    assert TestgetTerm.getTerm(subject,grade,version,studyYear) == expected

# if __name__ == '__main__':
#     pytest.main(['test_getlist001.py'])

