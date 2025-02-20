import sys


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


if __name__ == '__main__':
    # 可返回命令行的参数
    res = sys.argv
    print(res)