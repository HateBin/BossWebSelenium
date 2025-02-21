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
        """
        执行自动化沟通测试，模拟用户登录并进行职位沟通

        参数:
        - driver: 浏览器驱动实例，用于操作网页

        此函数不返回任何值
        """
        # 记录测试开始
        self.logger.info('启动自动化沟通')

        # 初始化计数器和控制变量
        count = 0
        is_break = False

        # 访问项目主页
        driver.get(settings.PROJECT_HOST)

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

        # 遍历每个职位选项
        for job in jobs:
            # 点击职位选项
            hp.click_job_options(job)

            # 进行沟通并获取结果
            result = hp.communicate()

            # 获取沟通次数并累加到总次数
            communicate_count = result['communicateCount']
            count += communicate_count

            # 如果需要中断循环，则设置标志变量并跳出循环
            if result['isBreak']:
                is_break = True
                break

        # 根据is_break的值，记录不同的结束信息
        if is_break:
            self.logger.info(f'自动化沟通结束, 今天的沟通次数已用完, 总共沟通次数为: {count}')
        else:
            self.logger.info(f'自动化沟通结束, 今天的沟通次数未用完, 总共沟通次数为: {count}')





if __name__ == '__main__':
    pytest.main(['-s', '-v', '-m', 'BossAuto', settings.TEST_CASE_DIR])