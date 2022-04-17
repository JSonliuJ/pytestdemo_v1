import pytest
from selenium import webdriver

@pytest.fixture(scope='class')
def driver_init():
    print("前置操作")
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    yield driver,True
    print("后置处理工作")
    driver.quit()

@pytest.fixture(scope="function")
def login():
    print("登录操作！")

@pytest.fixture(scope='module',autouse=True)
def windows_maximization():
    print("浏览器窗口最大化")

# 注册标签方式1：
# def pytest_configure(config):
#     marker_list = ["recharge"]
#     for markers in marker_list:
#         config.addinivalue_line(
#             "markers",markers
#         )