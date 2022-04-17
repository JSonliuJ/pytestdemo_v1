# -- encoding: utf-8 --
# @time:    	2022/4/12 23:30
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com
# indirect = Ture 把传递过来的参数当函数执行
import pytest


# 1.单个parametrize装饰：参数方式传入
# 1.1一个参数一个值
@pytest.mark.parametrize("val", ["value1"])
def test_case1(val):
    print("\n" + val)
    assert val == "value1"


# 1.2 一个参数多个值
@pytest.mark.parametrize("val", ["value1", "value2", "valuen"])
def test_case1(val):
    assert 'value' in val

# @pytest.mark.parametrize("val", [{"username1":"value1"}, {"username2":"value2"}])
@pytest.mark.parametrize("val", ({"username1":"value1"}, {"username2":"value2"}))
def test_case02(val):
    print(val)

# 1.3 多个参数多个值
# @pytest.mark.parametrize("user,pwd",
#                          [("user1", "123456"), ("user2", "123457"), ("user3", "123458"), ("user4", "123459")])
# def test_recharge(user, pwd):
#     print(user + " : " + pwd)
#     assert 'user' in user

# 2 组合参数化:多组参数，依次组合。
'''
使用多个@pytest.mark.parametrize
示例:用例有4个: 0,2/0,3/1,2/1,3 迪卡尔积
'''
@pytest.mark.parametrize("x", [0, 1])
@pytest.mark.parametrize("y", [2, 3])
def test_foo(x, y):
    print("%s/%s" % (y, x))

@pytest.mark.parametrize("params1", ["user01"])
@pytest.mark.parametrize("params2", [["value_p2","value_p3"],["value_pp2,value_pp3"]])
def test_func01(params1,params2):
    d = {}
    d[params1] = params2
    print(d)
'''
函数参数化：将函数以参数方式传入
'''
user_data = ["Jonliu","张三","lusy"]


@pytest.fixture(scope='module')
def login(request):
    '''登录函数'''
    user = request.param['user']
    password = request.param['password']
    print('用户名：%s' % user)
    print('密码：%s' % password)
    return request.param

login_data = [{'user': 'admin01', 'password': '123456'}, {'user': 'admin02', 'password': 'abc123'}]
@pytest.mark.parametrize('login',login_data,indirect=True)
def test_login(login):
    a = login
    print(a)
    assert 'admin' in a['user']
