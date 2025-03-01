# -*- coding: utf-8 -*-
"""
@Time ： 2025/2/19 21:20
@Auth ： pengjianbin
@File ：home_page_locators.py
"""

class HomePageLocators:
    # 登录用户名定位
    user_name_locator = ('xpath', '/html/body/div[1]/div[1]/div/div/div[1]/div[3]/ul/li[2]/a/span')
    # 职位选项容器定位
    job_options_locator = ('xpath', '/html/body/div[1]/div[2]/div[1]/div/div[1]')

    # 职位选项定位
    @staticmethod
    def job_option_locator(number):
        index = number + 1
        return 'xpath', f'/html/body/div[1]/div[2]/div[1]/div/div[1]/a[{index}]'
