# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from time import sleep
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestCart:

    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "baixue"
        caps["appPackage"] = "com.dangdang.buy2"
        caps["appActivity"] = ".StartupActivity"
        caps["noReset"] = "True"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        #隐式等待
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_001(self):

        el1 = self.driver.find_element(MobileBy.ID,"com.dangdang.buy2:id/home_search_bar_layout")
        el1.click()
        el2 = self.driver.find_element(MobileBy.ID,"com.dangdang.buy2:id/et_search")
        el2.send_keys("android")
        el3 = self.driver.find_element(MobileBy.XPATH,"//*[@text='android'and @resource-id='com.dangdang.buy2:id/tv_sug']")
        el3.click()
        el4 = self.driver.find_elements(MobileBy.ID,"com.dangdang.buy2:id/product_img_iv")[1]
        el4.click()
        el5 = self.driver.find_element(MobileBy.ID,"com.dangdang.buy2:id/tv_magic_btn_right")
        el5.click()

        sleep(5)
        #print(self.driver.page_source)
        #ele =self.driver.find_element(MobileBy.XPATH,"//*[@class='android.widget.Toast']")
        # print(ele.text)
        # assert '商品已成功加入购物车'== ele.text




