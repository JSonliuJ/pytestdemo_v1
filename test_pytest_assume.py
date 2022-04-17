# -- encoding: utf-8 --
# @time:    	2022/4/11 23:08
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com
import pytest


def test_a():
    print("test_a方法")


class TestDemo01():
    def test_one(self):
        x = "this"
        pytest.assume("a" in x)
        pytest.assume("b" == x)
        pytest.assume("c" not in x)

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")

    def test_three(self):
        a = "hello "
        b = 'hello world'
        assert a not in b


class TestDemo02():
    def test_a(self):
        x = "this"
        assert "h" in x

    def test_b(self):
        x = "hello"
        assert hasattr(x, "check")

    def test_c(self):
        a = "hello "
        b = 'hello world'
        assert a not in b


if __name__ == '__main__':
    # 执行方式1——终端运行：pytest -v -s test_pytest.py::TestDemo01::test_one
    pytest.main()  # 执行方式2:运行所有用例
    # pytest.main("-v -s TestDemo01::test_three") # 执行方式1
    pytest.main(["-v", "TestDemo01", "test_three"])  # 执行方式2
