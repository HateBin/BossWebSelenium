import sys
import settings
import re
import time
import random
import os
import yaml
import datetime
import urllib.parse


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

def update_communicate_count(count_type: str, update: int = None, add: int = None):
    current_date = get_date('%Y-%m-%d')
    if update:
        yaml_write('communicate_record', [count_type, current_date], str(update))
    if add:
        current_data = yaml_read('communicate_record')
        current_count = current_data[count_type].get(current_date)
        if not current_count:
            current_count = 0
            yaml_write('communicate_record', [count_type, current_date], '0')
        current_count = int(current_count) + add
        yaml_write('communicate_record', [count_type, current_date], str(current_count))

def convert_page_path_to_url_and_params(page_path):
    path_data = {}
    page_path = page_path.replace(' ', '')
    for host in settings.PROJECT_HOSTS.values():
        if page_path.startswith(host):
            page_path = page_path.replace(host, '')
            break
    if '?' not in page_path or page_path.endswith('?'):
        if page_path.endswith('?'):
            page_path = page_path.replace('?', '')
        path_data['url'] = page_path
        return path_data
    page_path_list = page_path.split('?')
    path_data['url'] = page_path_list[0]
    path_data['params'] = {}
    path_params_str = page_path_list[1]
    if '&' in path_params_str:
        path_params_list = path_params_str.split('&')
    else:
        path_params_list = [path_params_str]
    for path_params in path_params_list:
        path_params_key_value = path_params.split('=')
        # decoded_value = urllib.parse.unquote(urllib.parse.unquote(path_params_key_value[1]))
        path_data['params'][path_params_key_value[0]] = path_params_key_value[1]
    return path_data

def rest_time(minutes: list or tuple = None):
    if not minutes:
        minutes = settings.REST_TIME_FRAME
    min_sec = minutes[0] * 60
    max_sec = minutes[1] * 60
    time.sleep(random.uniform(min_sec, max_sec))

def get_online_image_name(online_image_path, is_format: bool = True):
    online_image_name = online_image_path.split('/')[-1]
    if not is_format:
        online_image_name = online_image_name.split('.')[0]
    return online_image_name

if __name__ == '__main__':
    # exp = r'^(.*?)\[.+\]$'
    # print(regular_expression(exp, '软件测试工程师[南山区]'))
    # print(regular_expression(exp, '11000-16000元/月'))
    # update_communicate_count(count_type='laGou', add=1)
    print(get_online_image_name('https://lagou-zhaopin-fe.lagou.com/fed/lg-www-fed/position/pc/yitou.png', is_format=False))