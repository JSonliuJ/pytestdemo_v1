# -- encoding: utf-8 --
# @time:    	2022/4/12 20:59
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com
import logging
import pytest
logging.basicConfig(level=logging.DEBUG)


def setup_module():
    print("setup_module")


def teardown_module():
    print("teardown_module")


def setup_function():
    print("setup_function")


def teardown_function():
    print("teardown_function")


class TestSetUpTeardownClass():

    @classmethod
    def setup_class(cls):
        print("前置类方法")

    def setup_method(self):
       print("setup_method")

    def setup(self):
        print("前置方法")

    def test_login(self):
        print("测试方法")

    def teardown(self):
        print("后置方法")

    def teardown_method(self):
        print("teardown_method")

    @classmethod
    def teardown_class(cls):
        print("后置类方法")
if __name__ == '__main__':
    pytest.main()