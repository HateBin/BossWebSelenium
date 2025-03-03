import pytest
import random
from selenium import webdriver


# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope='class')
def driver():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        # "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
        # "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"
    ]
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument(f'user-agent={random.choice(user_agents)}')
    with webdriver.Chrome(options=options) as wd:
        # with webdriver.Chrome(options=add_options()) as wd:
        wd.execute_cdp_cmd(
            "Page.addScriptToEvaluateOnNewDocument",
            {
                "source": """
                    Object.defineProperty(navigator, 'webdriver', {
                        get: () => undefined
                    })
                """
            }
        )
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
