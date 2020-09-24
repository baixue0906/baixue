import os

import pytest

if __name__ == "__main__":
    # pytest.main(['../cases/test_01.py','../cases/test_02.py'])
    pytest.main(['../cases/test_Getgoodslist.py','--html=../report0830/report0830.html','--junitxml=../report0830/report0830.xml','--alluredir','../report0830/reportallure/']) #生成HTML格式的报告，报告生成的路径
    #allure generate ./report0830/reportallure/ -o ./report0830/allurereporthtml1/ --clean
    #allure generate ./reportallure/ -o ./allurereporthtml/ --clean
    os.system('allure generate ../report0830/reportallure/ -o ../report0830/allurereporthtml2/ --clean')

