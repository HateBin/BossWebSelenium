import pytest
import os
import settings
from common.tools import get_opts

if __name__ == '__main__':
    # pytest.main(['-s','-v',"--alluredir=./reports/temp", settings.TEST_CASE_DIR])
    # os.system('allure generate ./reports/temp -o ./reports/report --clean')
    # 定义传入的参数信息
    args = ['-s', '-v', '--alluredir=./reports/temp', settings.TEST_CASE_DIR]
    # 获取命令行-m参数的值
    arg = get_opts('-m')
    # 若-m参数不为空，则将参数和参数值传入参数信息中
    if arg:
        args.insert(0, '-m {}'.format(arg))
    arg = get_opts('--browser')
    if arg:
        args.insert(0, '--browser=={}'.format(arg))  # 坑：这里只能写key=value的形式，不要用空格
    # 运行代码并生成测试报告
    pytest.main(args)
    os.system('allure generate ./reports/temp -o ./reports/report --clean')