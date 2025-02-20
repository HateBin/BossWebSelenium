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


    @pytest.mark.boss
    def test_automated_communication(self, driver):
        driver.get(settings.PROJECT_HOST)
        lp = LoginPage(driver)
        hp = HomePage(driver)
        lp.go_to_login()
        lp.click_wechat_login()
        hp.get_user_name()
        jobs = hp.get_job_options()
        for job in jobs:
            hp.click_job_options(job)
            hp.communicate()




if __name__ == '__main__':
    pytest.main(['-s', '-v', '-m', 'boss', settings.TEST_CASE_DIR])