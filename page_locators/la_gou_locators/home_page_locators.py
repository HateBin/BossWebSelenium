# -*- coding: utf-8 -*-
"""
@Time ： 2025/2/19 21:20
@Auth ： pengjianbin
@File ：home_page_locators.py
"""

class HomePageLocators:
    # 登录用户名定位
    user_name_locator = ('xpath', '/html/body/div/header/div[1]/div[2]/ul/li[5]/div[1]/span')

    # 首页搜索框定位
    home_search_box_locator = ('xpath', '/html/body/div[1]/div[2]/div[1]/div[1]/div/div/form/input[1]')

    # 首页搜索按钮定位
    home_search_button_locator = ('xpath', '/html/body/div[1]/div[2]/div[1]/div[1]/div/div/form/input[2]')

    # 职位选项定位
    @staticmethod
    def job_option_locator(number):
        index = number + 1
        return 'xpath', f'/html/body/div[1]/div[2]/div[1]/div/div[1]/a[{index}]'
