# -- encoding: utf-8 --
# @time:    	2022/4/14 23:18
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com
import pytest
@pytest.mark.register
def test_register001():
    print("注册用例case001")

@pytest.mark.register
def test_register002():
    print("注册用例case002")

@pytest.mark.register
def test_register003():
    print("注册用例case003")

@pytest.mark.recharge
def test_recharge001():
    print("充值用例case001")

@pytest.mark.recharge
def test_recharge002():
    print("充值用例case002")

if __name__ == '__main__':
    pytest.main(['-m','recharge','-s','-v'])