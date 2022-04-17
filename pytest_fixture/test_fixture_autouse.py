# -- encoding: utf-8 --
# @time:    	2022/4/12 22:45
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com
import pytest


@pytest.fixture(autouse=True)
def open():
    print("打开浏览器")


def test_search01(open):
    print("test_search01")
    raise NameError
    pass


def test_search02(open):
    print("test_search02")


def test_search03(open):
    print("test_search03")


if __name__ == '__main__':
    pytest.main(["-v" "-s" "test_search01"])
