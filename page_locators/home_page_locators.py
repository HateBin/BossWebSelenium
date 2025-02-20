# -*- coding: utf-8 -*-
"""
@Time ： 2025/2/19 21:20
@Auth ： pengjianbin
@File ：home_page_locators.py
"""

class HomePageLocators:
    # 登录用户名定位
    user_name_locator = ('xpath', '/html/body/div[1]/div[1]/div/div/div[1]/div[3]/ul/li[2]/a/span')
    # 职位选项定位
    job_options_locator = ('xpath', '/html/body/div[1]/div[2]/div[1]/div/div[1]')

    @staticmethod
    def job_option_locator(number):
        index = number + 1
        return 'xpath', f'/html/body/div[1]/div[2]/div[1]/div/div[1]/a[{index}]'

    @staticmethod
    def job_name_locator(number):
        index = number + 1
        return 'xpath', f'/html/body/div[1]/div[2]/div[1]/div/div[1]/a[{index}]/span'

    @staticmethod
    def hire_salary_locator(number):
        return 'xpath', f'/html/body/div[1]/div[2]/div[2]/div/div/div[1]/ul/div[{number}]/li/div[1]/div/span'

    @staticmethod
    def hire_title_locator(number):
        return 'xpath', f'/html/body/div[1]/div[2]/div[2]/div/div/div[1]/ul/div[{number}]/li/div[1]/div/a'

    @staticmethod
    def hire_option_locator(number):
        return 'xpath', f'/html/body/div[1]/div[2]/div[2]/div/div/div[1]/ul/div[{number}]/li'

    hire_list_locator = ('xpath', '/html/body/div[1]/div[2]/div[2]/div/div/div[1]/ul')

    hire_detail_msg_locator = ('xpath', '/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/p')

    communicate_button_locator = ('xpath', '/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/a[2]')

    communicate_pop_title_locator = ('xpath', '/html/body/div[8]/div[2]/div[1]/h3')
    communicate_pop_return_button_locator = ('xpath', '/html/body/div[8]/div[2]/div[3]/a[1]')