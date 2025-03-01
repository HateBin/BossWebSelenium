# -*- coding: utf-8 -*-
"""
@Time ： 2025/2/19 21:19
@Auth ： pengjianbin
@File ：home_page.py
"""
import settings
from page_objects.base_page import BasePage
from page_locators.la_gou_locators.home_page_locators import HomePageLocators as Loc
from common.tools import time_sleep


class HomePage(BasePage):
    # 页面名称
    name = '拉勾首页'

    def refresh_page(self):
        self.refresh_element(is_logger=False)

    def get_user_name(self):
        """
        获取当前用户的用户名。

        该方法用在给用户时间扫码进行登录，通过等待元素获取用户名称，用户登录完成后进入主页后等待元素则会获取到用户名称，则视为登录成功

        Raises:
            AssertionError: 如果无法获取用户名，则抛出断言错误。
        """
        # 等待用户名元素可见，最大等待时间为600秒
        self.wait_element_is_visible(
            locator=Loc.user_name_locator,
            timeout=settings.LOGIN_TIMEOUT,
            action='获取用户名'
        )
        try:
            # 尝试获取用户名元素的文本内容
            assert self.get_element_text()
        except AssertionError:
            # 如果获取用户名失败，记录错误日志并抛出异常
            self.logger.error('获取用户名失败')
            raise

    def query_job(self):
        self._input_home_search_box('软件测试')
        self._click_search_button()


    def _input_home_search_box(self, text):
        self.wait_element_is_visible(
            locator=Loc.home_search_box_locator,
            timeout=settings.LOGIN_TIMEOUT,
            action='输入搜索框'
        ).send_keys(text)


    def _click_search_button(self):
        self.wait_element_is_visible(
            locator=Loc.home_search_button_locator,
            timeout=settings.LOGIN_TIMEOUT,
            action='点击搜索按钮'
        ).delay(2).click_element()