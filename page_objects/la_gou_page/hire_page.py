import settings
from page_objects.base_page import BasePage
from page_locators.la_gou_locators.hire_page_locators import HirePageLocators as Loc
from common.tools import time_sleep


class HirePage(BasePage):

    name = '拉勾招聘列表页面'

    def select_degree(self):
        self._move_select_degree()
        self._click_associate_degree()

    def _move_select_degree(self):
        self.wait_element_is_visible(
            Loc.select_degree_locator,
            action='移动选择学历'
        ).delay().move_element()

    def _click_associate_degree(self):
        self.wait_element_is_visible(
            Loc.associate_degree_locator,
            action='点击选择大专学历'
        ).delay().click_element()
