from page_objects.login_page import LoginPage
from test_cases.base_case import BaseCase
import pytest

from test_data.login_data import *


class TestLogin(BaseCase):
    name = '登录功能'

    @pytest.mark.success
    @pytest.mark.loginsuccess
    # 数据参数化，case为数据参数名，success_cases为传入的数据
    @pytest.mark.parametrize('case', success_cases)
    def test_login_success(self, driver, case):
        '''
        登录页面的登录功能
        :param username: 用户名
        :param password: 密码
        :param rememberPassword: 是否记住账号密码
        :return:
        '''
        self.logger.info('***{}用例开始测试***'.format(case['title']))
        # 1.访问登录页面
        driver.get(self.settings.PROJECT_HOST)
        # 实例化登录页面
        lp = LoginPage(driver)
        # # 调用登录方法
        # lp.login(**case['request_data']) ## 增加登录注销用户用例
        self.logger.info('***{}用例结束测试***'.format(case['title']))


if __name__ == '__main__':
    pytest.main(['-s', '-v', '-m', 'success', settings.TEST_CASE_DIR])