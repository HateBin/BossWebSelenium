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

    # 职位名称定位
    @staticmethod
    def job_name_locator(number):
        index = number + 1
        return 'xpath', f'/html/body/div[1]/div[2]/div[1]/div/div[1]/a[{index}]/span'

    # 招聘薪资定位
    @staticmethod
    def hire_salary_locator(number):
        return 'xpath', f'/html/body/div[1]/div[2]/div[2]/div/div/div[1]/ul/div[{number}]/li/div[1]/div/span'

    # 招聘标题定位
    @staticmethod
    def hire_title_locator(number):
        return 'xpath', f'/html/body/div[1]/div[2]/div[2]/div/div/div[1]/ul/div[{number}]/li/div[1]/div/a'

    # 招聘公司定位
    @staticmethod
    def hire_company_locator(number):
        return 'xpath', f'/html/body/div[1]/div[2]/div[2]/div/div/div[1]/ul/div[{number}]/li/div[2]/a/span'

    # 招聘选项容器定位
    hire_options_container_locator = ('xpath', '/html/body/div[1]/div[2]/div[2]/div/div/div[1]')

    # 招聘选项定位
    @staticmethod
    def hire_option_locator(number):
        return 'xpath', f'/html/body/div[1]/div[2]/div[2]/div/div/div[1]/ul/div[{number}]/li'

    # 招聘详情描述容器定位
    hire_detail_msg_container_locator = ('xpath', '/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]')

    # 招聘选项标签定位
    @staticmethod
    def hire_option_label_locator(number):
        return 'xpath', f'/html/body/div[1]/div[2]/div[2]/div/div/div[1]/ul/div[{number}]/li/img'

    # 招聘列表定位
    hire_list_locator = ('xpath', '/html/body/div[1]/div[2]/div[2]/div/div/div[1]/ul')

    # 招聘学历定位
    hire_education_background_locator = (
        'xpath', '/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/ul/li[3]')

    # 招聘详情描述定位
    hire_detail_msg_locator = ('xpath', '/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/p')

    # 招聘者状态定位
    recruiter_state_locator = ('xpath', '/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div[2]/h2/span')

    # 沟通按钮定位
    communicate_button_locator = ('xpath', '/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/a[2]')

    # 沟通弹窗标题定位
    communicate_pop_title_locator = ('xpath', '/html/body/div[8]/div[2]/div[1]/h3')

    # 沟通弹窗返回按钮定位
    communicate_pop_return_button_locator = ('xpath', '/html/body/div[8]/div[2]/div[3]/a[1]')

    # 导航栏"推荐"的类名定位
    navigation_bar_recommend_class_locator = ('xpath', '/html/body/div[1]/div[1]/div/div/div[1]/div[2]/ul/li[2]')

    # 导航栏"推荐"定位
    navigation_bar_recommend_locator = ('xpath', '/html/body/div[1]/div[1]/div/div/div[1]/div[2]/ul/li[2]/a')