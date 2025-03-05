# -*- coding: utf-8 -*-
"""
@Time ： 2025/2/19 20:55
@Auth ： pengjianbin
@File ：test_automated_communication.py
"""

from test_cases.base_case import BaseCase
from common.tools import rest_time
import pytest
import settings

class TestAutomatedCommunication(BaseCase):


    @pytest.mark.boss
    def test_automated_boss_communication(self, driver):
        """
        执行自动化沟通测试，模拟用户登录并进行职位沟通

        参数:
        - driver: 浏览器驱动实例，用于操作网页

        此函数不返回任何值
        """

        from page_objects.boss_page.login_page import LoginPage
        from page_objects.boss_page.home_page import HomePage


        # 记录测试开始
        self.logger.info('启动自动化沟通')

        # 初始化计数器和控制变量
        count = 0
        is_break = False

        # 访问项目主页
        driver.get(settings.PROJECT_HOSTS['boss'])

        # 实例化登录页和主页对象
        lp = LoginPage(driver)
        hp = HomePage(driver)

        # 进入登录页面并点击微信登录
        lp.go_to_login()
        lp.click_wechat_login()

        # 获取用户名，用于验证登录
        hp.get_user_name()

        # 获取所有职位选项
        jobs = hp.get_job_options()
        job_index = 0
        while True:
            job = jobs[job_index]
            # 遍历每个职位选项
            while True:
                # 点击职位选项
                hp.click_job_options(job)

                # 进行沟通并获取结果
                result = hp.communicate()

                # 获取沟通次数并累加到总次数
                communicate_count = result['communicateCount']
                count += communicate_count

                if result['isGoToChat']:
                    continue

                # 如果需要中断循环，则设置标志变量并跳出循环
                if result['switchJob'] or result['isBreak']:
                    if result['isBreak']:
                        is_break = True
                    break
            if is_break:
                break
            if job_index + 1 == len(jobs):
                job_index = 0
                hp.refresh_page()
                # rest_time()
            else:
                job_index += 1
        # 根据is_break的值，记录不同的结束信息
        if is_break:
            self.logger.info(f'自动化沟通结束, 今天的沟通次数已用完, 总共沟通次数为: {count}')
        else:
            self.logger.info(f'自动化沟通结束, 今天的沟通次数未用完, 总共沟通次数为: {count}')


    @pytest.mark.laGou
    def test_automated_la_gou_communication(self, driver):
        """
        执行自动化沟通测试，模拟用户登录并进行职位沟通

        参数:
        - driver: 浏览器驱动实例，用于操作网页

        此函数不返回任何值
        """

        from page_objects.la_gou_page.login_page import LoginPage
        from page_objects.la_gou_page.home_page import HomePage
        from page_objects.la_gou_page.hire_page import HirePage

        # 记录测试开始
        self.logger.info('启动自动化沟通')

        # 初始化计数器和控制变量
        count = 0

        # 访问项目主页
        driver.get(settings.PROJECT_HOSTS['laGou'])

        # 实例化登录页和主页对象
        lp = LoginPage(driver)
        hop = HomePage(driver)
        hip = HirePage(driver)

        # 登录
        lp.login()

        # 获取用户名，用于验证登录
        hop.get_user_name()

        hop.query_job()

        # hip.selected()

        while True:

            current_page_hire_count = hip.get_hire_options_count()

            result: dict = hip.communicate(current_page_hire_count)

            count += result['communicateCount']

            if hip.current_is_last_page():
                break
            else:
                hip.click_next_page()

        self.logger.info(f'自动化执行完毕，沟通次数为: {count}')








if __name__ == '__main__':
    pytest.main(['-s', '-v', '-m', 'laGou', settings.TEST_CASE_DIR])