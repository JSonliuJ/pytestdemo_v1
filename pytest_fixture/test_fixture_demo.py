# -- encoding: utf-8 --
# @time:    	2022/4/12 22:05
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com
import pytest
import os
import sys

# local_path = os.path.dirname(os.path.split(os.path.abspath(__file__))[0])
# print(local_path)
# sys.path.append(local_path)
class TestFixTureDemo01:

    def test_case01(self,login):
        print("需要先登录")

    def test_case02(self):
        print("不需要登录")

    def test_case03(self,login):
        print("后登录")

    @pytest.mark.usefixtures("login")
    def test004(self):
        print("usefixture方式调用")

if __name__ == '__main__':
    pytest.main()