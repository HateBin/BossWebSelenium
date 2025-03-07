import os, time

# 项目根目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 测试用例路径
TEST_CASE_DIR = os.path.join(BASE_DIR, 'test_cases')

# 项目域名
PROJECT_HOSTS = {
    'boss': 'https://www.zhipin.com',
    'laGou': 'https://www.lagou.com/wn'
}

LA_GOU_PAGE_PATH = {
    'hire': '/zhaopin',
}

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

# 默认操作间隔, [min, max] or int
OPERATION_INTERVAL = [2, 3]

# 休息时间范围[min, max]，单位是min，用于在执行完一轮操作后，进行休息
REST_TIME_FRAME = [5, 10]

# 全局查找默认等待时间
DEFAULT_TIMEOUT = 60

# 登录等待时间, 秒为单位
LOGIN_TIMEOUT = 600

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

PASS_EDUCATION_BACKGROUNDS = ['大专', '本科']

SALARY_EXPECTATION = 15  # 期望薪资，单位为k

IS_ACCEPT_HARDWARE = False  # 是否接受硬件
IS_ACCEPT_BANKING_OR_FINANCE = False  # 是否接受银行或者金融

FAIL_TEXTS = [
    '统招',
    '学信网',
    '东莞',
    '厦门',
    '广州',
    '武汉',
    '珠海',
    '佛山',
    '日本',
    '英语',
    '英文',
    'english',
    '游戏',
    '安全测试',
    '可靠性',
    '区块链',
    '兼职',
    '制造',
]

HARDWARE_TEXTS = [
    '硬件',
    '嵌入式',
    '机器人',
    '整机',
    '无人机',
    '蓝牙',
    'iot',
    '万用表',
    '打印机',
]

BANKING_OR_FINANCE_TEXTS = [
    '银行',
    '证券',
    '金融',
    '借贷',
    '信贷',
]

PASS_TITLE_TEXTS = {
    'or': ['测试', 'qa', 'qe'],
    'and': [],
}

FAIL_TITLE_TEXTS = [
    '主管',
    '负责人',
    # '组长',
    '经理',
]

FAIL_COMPANIES = [
    '拓保',
    '跨越速运',
    '华为',
    '腾讯',
]

PASS_RECRUITER_STATES = [
    '在线',
    '刚刚活跃',
    '今日活跃',
]

FAIL_HIRE_LABELS = [
    '猎头',
    '派遣',
]

LA_GOU_POSITION_TYPES = [
    '测试工程师',
    '自动化测试',
    '测试开发',
]
