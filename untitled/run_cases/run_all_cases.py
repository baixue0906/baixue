import os
import pytest

if __name__ == "__main__":
    #pytest.main(['../test_case/test_getCourse.py']) #运行单个case
    pytest.main(['../test_case/','--html=../report/report.html','--junitxml=../report/report.xml','--alluredir','../report/allureresult/'])
    os.system('allure generate ../report/allureresult/ -o ../report/allurereporthtml/ --clean')
