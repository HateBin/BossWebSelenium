# -*- coding: utf-8 -*-
"""
@Time ： 2025/2/19 21:19
@Auth ： pengjianbin
@File ：home_page.py
"""
import settings
from page_objects.base_page import BasePage
from page_locators.home_page_locators import HomePageLocators as Loc
from common.tools import text_mapping_switch, regular_expression, time_sleep


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
            job_option_class_name = self.wait_element_is_visible(
                locator=Loc.job_option_locator(number),
                action='获取岗位选项'
            ).get_element_attr('class')
            if job_option_class_name == 'recommend-job-btn has-tooltip':
                jobs.append(self.wait_element_is_visible(
                    locator=Loc.job_name_locator(number),
                    action='获取岗位名称'
                ).get_element_text())
            elif job_option_class_name == 'add-expect-btn':
                break
        return jobs

    def click_job_options(self, job_name):
        number = 0
        while True:
            number += 1
            job_option_class_name = self.wait_element_is_visible(
                locator=Loc.job_option_locator(number),
                action='获取岗位选项'
            ).get_element_attr('class')
            if job_option_class_name == 'recommend-job-btn has-tooltip':
                if self.wait_element_is_visible(
                        locator=Loc.job_name_locator(number),
                        action='获取岗位名称'
                ).get_element_text() == job_name:
                    self.wait_element_is_visible(
                        locator=Loc.job_name_locator(number),
                        action='获取岗位名称'
                    ).click_element()
                    break
            elif job_option_class_name == 'add-expect-btn':
                self.logger.exception('岗位不存在')
                raise

    def communicate(self):
        old_job_count = 0
        communicate_count = 0
        while True:
            job_count = self._get_hire_count()
            if job_count == old_job_count:
                self.logger.info('招聘列表数量未发生变化, 结束该列表的操作')
                break
            self.logger.info(f'获取招聘列表数量为: {job_count}')
            for number in range(1 + old_job_count, job_count + 1):
                title_text = self._get_hire_title(number)
                salary: tuple = self._get_hire_salary(number)
                if salary[1] <= settings.SALARY_EXPECTATION:
                    self.logger.info(f'{title_text}薪资{salary[0]}-{salary[1]}k, 不符合期望')
                    continue
                title_pass_count = 0
                title_fail_count = 0
                for passOption in settings.PASS_OPTIONS:
                    if passOption in title_text:
                        title_pass_count += 1
                if title_pass_count != len(settings.PASS_OPTIONS):
                    self.logger.info(f'{title_text}不符合期望, 标题存在不包含关键字: {settings.PASS_OPTIONS}')
                    continue
                for failOption in settings.FAIL_OPTIONS:
                    if failOption in title_text:
                        title_fail_count += 1
                        self.logger.info(f'{title_text}不符合期望, 标题包含关键字: {failOption}')
                        break
                if title_fail_count > 0:
                    continue
                self._click_hire_option(number)
                time_sleep()
                hire_detail_msg = self._get_hire_detail_msg()
                msg_fail_count = 0
                for failOption in settings.FAIL_OPTIONS:
                    if failOption in hire_detail_msg:
                        msg_fail_count += 1
                        self.logger.info(f'{title_text}不符合期望, 招聘详情包含了关键字: {failOption}')
                        break
                if msg_fail_count > 0:
                    continue
                if not self._click_communicate_button():
                    continue
                time_sleep()
                if self._get_communicate_pop_title() == '无法进行沟通':
                    self.logger.info('无法进行沟通')
                    return {'communicateCount': communicate_count, 'isBreak': True}
                else:
                    communicate_count += 1
                    self._click_communicate_pop_return()
                    time_sleep()
                self._script_element_hire_list(number)
            old_job_count = job_count
        return {'communicateCount': communicate_count, 'isBreak': False}

    def _get_hire_count(self):
        return len(self.wait_element_is_visible(
            locator=Loc.hire_list_locator,
            action='获取招聘列表'
        ).get_child_elements())

    def _get_hire_salary(self, number) -> tuple:
        salary_text = text_mapping_switch(self.wait_element_is_visible(
            locator=Loc.hire_salary_locator(number),
            action='获取招聘薪资'
        ).get_element_text())
        min_salary, max_salary = regular_expression(r'^(\d+)-(\d+)', salary_text)
        min_salary, max_salary = int(min_salary), int(max_salary)
        if max_salary > 1000:
            min_salary /= 1000
            max_salary /= 1000
        return min_salary, max_salary

    def _get_hire_title(self, number):
        return self.wait_element_is_visible(
            locator=Loc.hire_title_locator(number),
            action='获取招聘标题'
        ).get_element_text()

    def _click_hire_option(self, number):
        self.wait_element_is_visible(
            locator=Loc.hire_option_locator(number),
            action='点击招聘选项'
        ).click_element()

    def _get_hire_detail_msg(self):
        msg = self.wait_element_is_visible(
            locator=Loc.hire_detail_msg_locator,
            action='获取招聘详情'
        ).get_element_text()
        return msg

    def _click_communicate_button(self):
        button_text = self.wait_element_is_visible(
            locator=Loc.communicate_button_locator,
            action='点击沟通按钮'
        ).get_element_text()
        if button_text == '立即沟通':
            self.wait_element_is_visible(
                locator=Loc.communicate_button_locator,
                action='点击沟通按钮'
            ).click_element()
            return True
        return False

    def _get_communicate_pop_title(self):
        return self.wait_element_is_visible(
            locator=Loc.communicate_pop_title_locator,
            action='获取沟通弹窗标题'
        ).get_element_text()

    def _click_communicate_pop_return(self):
        self.wait_element_is_visible(
            locator=Loc.communicate_pop_return_button_locator,
            action='点击沟通弹窗"留在此页"'
        ).click_element()

    def _script_element_hire_list(self, number):
        self.wait_element_is_visible(
            locator=Loc.hire_option_locator(number),
            action='滚动招聘列表'
        ).script_element()
