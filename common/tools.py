import sys
import settings
import re
import time
import random


def get_opts(name):
    '''
    获取传入的命令行参数
    :param name:
    :return:
    '''
    args = sys.argv[1:]
    # 如果命令行中参数名有多个值，则需要使用""进行包裹
    # 如 -m "success and login"
    if name in args:
        return args[args.index(name) + 1]


def text_mapping_switch(text):
    for key, value in settings.TEXT_MAPPINGS.items():
        text = text.replace(key, value)
    return text

def regular_expression(expression, text):
    """
    正则表达式
    :param text:
    :return:
    """
    pattern = expression
    regex = re.compile(pattern)
    result = regex.search(text)
    groups = None
    if result:
        groups = result.groups()
    return groups

def time_sleep(second=None):
    if not second:
        second = random.uniform(1, 3)
    time.sleep(second)


if __name__ == '__main__':
    exp = r'^(\d+)-(\d+)'
    print(regular_expression(exp, '12-24K·13薪'))
    print(regular_expression(exp, '11000-16000元/月'))