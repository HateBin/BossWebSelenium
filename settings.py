import os, time

# 项目根目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 测试用例路径
TEST_CASE_DIR = os.path.join(BASE_DIR, 'test_cases')

# 项目域名
PROJECT_HOST = 'https://www.zhipin.com/'

# url信息
INTERFACE = {
    'login': '/communityManagement/#/login'
}

# 日志配置
LOG_CONFIG = {
    'name': "testlog",
    'filename': os.path.join(BASE_DIR, 'logs/testlog{}.log'.format(time.strftime('%Y%m%d'))),
    'mode': 'a',
    'encoding': 'utf-8',
    'debug': True
}

# 全局查找默认等待时间
DEFAULT_TIMEOUT = 3

# 错误截屏保存路径
ERROR_SCREENSHOT_DIR = os.path.join(BASE_DIR, 'screen_shot')

TEXT_MAPPINGS = {
    '': '1',
    '': '2',
    '': '3',
    '': '4',
    '': '5',
    '': '6',
    '': '7',
    '': '8',
    '': '9',
    '': '0',
}


SALARY_EXPECTATION = 17 # 期望薪资，单位为k
