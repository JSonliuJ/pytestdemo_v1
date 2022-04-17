# -- encoding: utf-8 --
# @time:    	2022/4/15 0:18
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com
import pytest
@pytest.mark.run(order=-10)
def test_register001():
    print("较大的负数执行")

@pytest.mark.run(order=-1)
def test_register002():
    print("较小的负数在较大负数后执行")


def test_register003():
    print("不标记处在中间执行")

@pytest.mark.run(order=5)
def test_recharge001():
    print("最小正整数执行后执行")

@pytest.mark.run(order=1)
def test_recharge002():
    print("在0后最小正整数执行")

@pytest.mark.run(order=0)
def test_login008():
    print("0先执行")
if __name__ == '__main__':
    pytest.main()