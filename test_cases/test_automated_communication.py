# -*- coding: utf-8 -*-
"""
@Time ： 2025/2/19 20:55
@Auth ： pengjianbin
@File ：test_automated_communication.py
"""

from page_objects.login_page import LoginPage
from page_objects.home_page import HomePage
from test_cases.base_case import BaseCase
import pytest
import settings

class TestAutomatedCommunication(BaseCase):


    @pytest.mark.BossAuto
    def test_automated_communication(self, driver):
        self.logger.info('启动自动化沟通')
        count = 0
        is_break = False
        driver.get(settings.PROJECT_HOST)
        lp = LoginPage(driver)
        hp = HomePage(driver)
        lp.go_to_login()
        lp.click_wechat_login()
        hp.get_user_name()
        jobs = hp.get_job_options()
        for job in jobs:
            hp.click_job_options(job)
            result = hp.communicate()
            count += result['communicateCount']
            if result['isBreak']:
                is_break = True
                break
        if is_break:
            self.logger.info(f'自动化沟通结束, 今天的沟通次数已用完, 总共沟通次数为: {count}')
        else:
            self.logger.info(f'自动化沟通结束, 今天的沟通次数未用完, 总共沟通次数为: {count}')





if __name__ == '__main__':
    pytest.main(['-s', '-v', '-m', 'BossAuto', settings.TEST_CASE_DIR])