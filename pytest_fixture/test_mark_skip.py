# -- encoding: utf-8 --
# @time:    	2022/4/12 23:30
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com
import pytest

@pytest.mark.skip()
def test_create_order001():
    pass

@pytest.mark.skipif(condition='if amount>0',reason='金额大于0执行')
def test_create_order002():
    pass
def test_login001():
    print("case001")

def test_register002():
    print("case002")

if __name__ == '__main__':
    pytest.main()