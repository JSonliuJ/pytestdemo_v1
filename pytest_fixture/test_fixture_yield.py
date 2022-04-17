# -- encoding: utf-8 --
# @time:    	2022/4/12 22:45
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com
import pytest


# 作用域:module是在模块之前执行，模块之后执行
@pytest.fixture(scope="module")
def open():
    print("打开浏览器")
    yield # 区分前后置
    print("执行teardown !")
    print("关闭浏览器")


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
