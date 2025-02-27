import sys
import settings
import re
import time
import random
import os
import yaml
import datetime


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
        operation_interval = settings.OPERATION_INTERVAL
        if isinstance(operation_interval, list):
            second = random.uniform(operation_interval[0], operation_interval[1])
        else:
            second = operation_interval
    time.sleep(second)

def get_date(res_format: str = None, year=None, month=None, day=None, hour=None, minute=None, second=None):
    """
    获取日期和时间
    :return:
    """
    now_date_time = datetime.datetime.now()
    get_year = now_date_time.year + (year if year else 0)
    get_month = now_date_time.month + (month if month else 0)
    get_day = now_date_time.day + (day if day else 0)
    get_hour = now_date_time.hour + (hour if hour else 0)
    get_minute = now_date_time.minute + (minute if minute else 0)
    get_second = now_date_time.second + (second if second else 0)
    if res_format is None:
        res_format = '%Y-%m-%d %H:%M:%S'
    if '%Y' in res_format:
        res_format = res_format.replace('%Y', '%04d' % get_year)
    if '%m' in res_format:
        res_format = res_format.replace('%m', '%02d' % get_month)
    if '%d' in res_format:
        res_format = res_format.replace('%d', '%02d' % get_day)
    if '%H' in res_format:
        res_format = res_format.replace('%H', '%02d' % get_hour)
    if '%M' in res_format:
        res_format = res_format.replace('%M', '%02d' % get_minute)
    if '%S' in res_format:
        res_format = res_format.replace('%S', '%02d' % get_second)
    return res_format


# 读取yaml文件
def yaml_read(yaml_name, yaml_key=None, dic_name=None):
    if dic_name:
        path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)) + f'/{dic_name}/{yaml_name}')
    else:
        path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)) + f'/yaml/{yaml_name}')
    is_exist = os.path.exists(path + '.yml')
    if is_exist:
        path += '.yml'
    else:
        is_exist = os.path.exists(path + '.yaml')
        if is_exist:
            path += '.yaml'
    with open(path, 'r', encoding='utf-8') as f:
        yaml_r = yaml.load(f, Loader=yaml.FullLoader)
        if yaml_key:
            return yaml_r.get(yaml_key)
        else:
            return yaml_r


# 写入yaml文件
def yaml_write(yaml_name, yaml_key, content, dic_name=None):
    if dic_name:
        path = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + f'/{dic_name}/{yaml_name}'
    else:
        path = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + f'/yaml/{yaml_name}'
    is_exist = os.path.exists(path + '.yml')
    if is_exist:
        path += '.yml'
    else:
        is_exist = os.path.exists(path + '.yaml')
        if is_exist:
            path += '.yaml'
    with open(path, 'r', encoding='utf-8') as f:
        yaml_r = yaml.safe_load(f)
    if type(yaml_key) in (tuple, list):
        if len(yaml_key) == 1:
            yaml_r[yaml_key[0]] = content
        if len(yaml_key) == 2:
            yaml_r[yaml_key[0]][yaml_key[1]] = content
    else:
        yaml_r[yaml_key] = content
    with open(path, 'w', encoding='utf-8') as f:
        yaml.dump(yaml_r, f, default_flow_style=False, allow_unicode=True)
    return 200

def update_communicate_count(update: int = None, add: int = None):
    current_date = get_date('%Y-%m-%d')
    if update:
        yaml_write('communicate_record', current_date, str(update))
    if add:
        current_count = yaml_read('communicate_record', current_date)
        if not current_count:
            current_count = 0
            yaml_write('communicate_record', current_date, '0')
        current_count = int(current_count) + add
        yaml_write('communicate_record', current_date, str(current_count))


if __name__ == '__main__':
    # exp = r'^(\d+)-(\d+)'
    # print(regular_expression(exp, '12-24K·13薪'))
    # print(regular_expression(exp, '11000-16000元/月'))
    update_communicate_count(add=1)
