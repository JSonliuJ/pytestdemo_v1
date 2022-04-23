# -- encoding: utf-8 --
# @time:    	2022/4/16 18:07
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com
import pytest
import time

@pytest.fixture(scope='class')
def mysql_connect():
    pass

@pytest.mark.usefixtures('driver_init')
@pytest.mark.usefixtures('mysql_connect')
class TestReturnDemo001():

    def test_a(self):
        print("-------test_a----------")

    def test_b(self):
        print("-------test_b----------")

    def test_baidu001(self,driver_init): # driver_init = (driver,True)
        driver_init[0].find_element_by_id("kw").send_keys("pytest")
        driver_init[0].find_element_by_xpath('//input[@id="su"]').click()
        time.sleep(10)


# 方式1：@pytest.mark.usefixtures('定义的fixture函数')
# 方式2：def test_case(定义的fixture函数)