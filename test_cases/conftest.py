import pytest
from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope='class')
def driver():
    with webdriver.Chrome() as wd:
    # with webdriver.Chrome(options=add_options()) as wd:
        # 最大化游览器
        wd.maximize_window()
        # 返回游览器对象，不能使用return，return返回之后会关闭游览器，无法进行后续操作
        yield wd

def add_options():
    print("—————————— options ——————————")
    # 创建谷歌浏览器驱动参数对象
    chrome_options = webdriver.ChromeOptions()
    # 不加载图片
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    # 使用无界面浏览器模式！！
    chrome_options.add_argument('--headless')
    # 使用隐身模式（无痕模式）
    chrome_options.add_argument('--incognito')
    # 禁用GPU加速
    chrome_options.add_argument('--disable-gpu')
    return chrome_options

# def pytest_addoption(parser):
#     # 定义pytest的参数
#     parser.addoption("--browser", default='chrome')   # 坑 参数都是--小写
#
# @pytest.fixture(scope='class')
# def driver(pytestconfig):
#     if pytestconfig.getoption('--browser')=='edge':
#         with webdriver.Edge(executable_path=settings.BROWSER_DRIVERS['edge']) as wd:
#             wd.maximize_window()
#             yield wd
#     elif pytestconfig.getoption('--browser')=='chrome':
#         with webdriver.Edge(executable_path=settings.BROWSER_DRIVERS['chrome']) as wd:
#             wd.maximize_window()
#             yield wd