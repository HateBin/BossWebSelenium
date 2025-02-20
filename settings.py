import os, time

# 项目根目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 测试用例路径
TEST_CASE_DIR = os.path.join(BASE_DIR, 'test_cases')

# 项目域名
PROJECT_HOST = 'https://www.zhipin.com/'


# url信息
INTERFACE={
    'login': '/communityManagement/#/login'
}

# 日志配置
LOG_CONFIG={
    'name': "testlog",
    'filename': os.path.join(BASE_DIR, 'logs/testlog{}.log'.format(time.strftime('%Y%m%d'))),
    'mode': 'a',
    'encoding': 'utf-8',
    'debug': True
}

# 测试账户信息
TEST_USER_DIST = {'account': 'pengjianbin17', 'password': 'aa123456', 'username': '常州市消委办主任A'}
# TEST_USER_DIST = {'account': 'admin', 'password': 'czxf@123', 'username': '测试人员'}
# TEST_USER_DIST = {'account': 'user003', 'password': 'czxf@123', 'username': 'user003'}



# 全局查找默认等待时间
DEFAULT_TIMEOUT = 3

# 错误截屏保存路径
ERROR_SCREENSHOT_DIR = os.path.join(BASE_DIR, 'screen_shot')


# # 浏览器驱动
# BROWSER_DRIVERS = {
#     'chrome': os.path.join(BASE_DIR, 'drivers', 'chromedriver_115.exe')
#     # 'edge': os.path.join(BASE_DIR, 'drivers', 'msedgedriver_90.exe')
# }