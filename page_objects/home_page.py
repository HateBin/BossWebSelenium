# -*- coding: utf-8 -*-
"""
@Time ： 2025/2/19 21:19
@Auth ： pengjianbin
@File ：home_page.py
"""
import settings
from page_objects.base_page import BasePage
from page_locators.home_page_locators import HomePageLocators as Loc
from common.tools import text_mapping_switch, regular_expression


class HomePage(BasePage):
    name = '首页'

    def get_user_name(self):
        """
        获取用户名
        :return:
        """
        self.wait_element_is_visible(
            locator=Loc.user_name_locator,
            timeout=600,
            action='获取用户名'
        )
        try:
            assert self.get_element_text()
        except AssertionError:
            self.logger.error('获取用户名失败')
            raise
        self.logger.debug('获取用户名成功')

    def get_job_options(self):
        number = 0
        jobs = []
        # self.wait_element_is_visible(
        #     locator=Loc.job_options_locator,
        #     action='获取岗位选项'
        # )
        while True:
            number += 1
            if self.wait_element_is_visible(
                    locator=Loc.job_option_locator(number),
                    action='获取岗位选项'
            ).get_element_attr('class') == 'recommend-job-btn has-tooltip':
                jobs.append(self.wait_element_is_visible(
                    locator=Loc.job_name_locator(number),
                    action='获取岗位名称'
                ).get_element_text())
            elif self.wait_element_is_visible(
                    locator=Loc.job_option_locator(number),
                    action='获取岗位选项'
            ).get_element_attr('class') == 'add-expect-btn':
                break
        return jobs

    def click_job_options(self, job_name):
        number = 0
        while True:
            number += 1
            if self.wait_element_is_visible(
                    locator=Loc.job_option_locator(number),
                    action='获取岗位选项'
            ).get_element_attr('class') == 'recommend-job-btn has-tooltip':
                option_text = self.wait_element_is_visible(
                    locator=Loc.job_name_locator(number),
                    action='获取岗位名称'
                ).get_element_text()
                if option_text == job_name:
                    self.wait_element_is_visible(
                        locator=Loc.job_name_locator(number),
                        action='获取岗位名称'
                    ).click_element()
                    break
            elif self.wait_element_is_visible(
                    locator=Loc.job_option_locator(number),
                    action='获取岗位选项'
            ).get_element_attr('class') == 'add-expect-btn':
                self.logger.exception('岗位不存在')
                raise

    def communicate(self):
        old_job_count = 0
        job_count = self._get_job_count()
        for number in range(1, job_count + 1):
            salary: tuple[int, int] = self._get_salary(number)
            if salary[1] < settings.SALARY_EXPECTATION:
                break

    def _get_salary(self, number) -> tuple[int, int]:
        salary_text = text_mapping_switch(self.wait_element_is_visible(
            locator=Loc.job_salary_locator(number),
            action='获取岗位薪资'
        ).get_element_text())
        min_salary, max_salary = regular_expression('^(.*?)-(.*?)K', salary_text)
        return int(min_salary), int(max_salary)

    def _get_job_count(self):
        return len(self.wait_element_is_visible(
            locator=Loc.job_list_locator,
        ).get_child_elements())
