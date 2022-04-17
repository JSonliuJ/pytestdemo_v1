# -- encoding: utf-8 --
# @time:    	2022/4/12 23:30
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com
import pytest
'''
使用场景: 标记某测试函数会失败
xfail(condition=None, reason=None, raises=None, run=True, strict=False)
常用参数：
   condition：预期失败的条件，必传参数
   reason：失败的原因
使用方法:
    @pytest.mark.xfail(condition, reason="xxx")
'''
@pytest.mark.xfail()
def test_create_order001():
    pass

def test_create_order002():
    pass
def test_login001():
    print("case001")

def test_register002():
    print("case002")

if __name__ == '__main__':
    pytest.main()