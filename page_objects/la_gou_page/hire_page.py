import settings
from page_objects.base_page import BasePage
from page_locators.la_gou_locators.hire_page_locators import HirePageLocators as Loc
from common.tools import regular_expression, update_communicate_count, time_sleep


class HirePage(BasePage):
    name = '拉勾招聘列表页面'

    def selected(self):
        self._move_select_degree()
        self._click_associate_degree()

        self._move_select_salary()
        self._click_salary_expected()

    def get_hire_options_count(self):
        count = self._get_hire_options_count()
        self.logger.info(f'拉勾招聘列表页面获取招聘选项数量为: {count}')
        return count

    def current_is_last_page(self):
        self.delay().script_windows_element(script_type='bottom', is_logger=False)
        pager_elements = self._get_hire_pager_sub_elements()
        next_page_attr = pager_elements[-1].get_attribute('aria-disabled')
        if next_page_attr == 'ture':
            return True
        else:
            return False

    def click_next_page(self):
        pager_elements = self._get_hire_pager_sub_elements()
        pager_elements[-1].click()

    def communicate(self, hire_count):
        communicate_count = 0
        for number in range(1, hire_count + 1):

            self._slide_to_visible(number)
            time_sleep()


            salary: tuple = self._get_hire_salary(number)
            salary_str = f'{salary[0]}-{salary[1]}k'
            company_name = self._get_hire_company_name(number)
            title_text = self._get_hire_title(number)

            # 如果薪资不符合期望，跳过
            if salary[1] < settings.SALARY_EXPECTATION:
                self.logger.info(f'{company_name}招聘: {title_text}薪资{salary_str}, 不符合期望')
                continue

            # 初始化标题通过和失败计数
            title_pass_count = 0
            title_fail_count = 0

            # 检查标题是否包含所有期望的关键字
            for passOption in settings.PASS_TITLE_TEXTS:  # 遍历期望存在的关键字
                if passOption in title_text:  # 如果关键字存在标题中则记录title_pass_count数量
                    title_pass_count += 1
            if title_pass_count != len(settings.PASS_TITLE_TEXTS):  # 如果记录的title_pass_count数量与期望的数量不一致，则跳过
                self.logger.info(
                    f'{company_name}招聘: {title_text}不符合期望, 标题存在不包含关键字: {settings.PASS_TITLE_TEXTS}')
                continue

            # 检查标题是否包含任何失败关键字
            fail_title_texts = settings.FAIL_TEXTS + settings.FAIL_TITLE_TEXTS
            for failOption in fail_title_texts:  # 遍历不期望存在的关键字
                if failOption in title_text:  # 如果关键字存在标题中则记录title_fail_count数量并且终止循环
                    title_fail_count += 1
                    self.logger.info(f'{company_name}招聘: {title_text}不符合期望, 标题包含关键字: {failOption}')
                    break
            if title_fail_count > 0:  # 如果存在不期望的关键字在标题中时，则跳过
                continue

            company_fail_count = 0
            for failCompanyText in settings.FAIL_COMPANIES:
                if failCompanyText in company_name:  # 如果公司名称包含不期望的关键字，则记录company_fail_count数量并且终止循环
                    company_fail_count += 1
                    self.logger.info(
                        f'{company_name}招聘: {title_text}不符合期望, 公司名称包含关键字: {failCompanyText}')
                    break

            self._click_hire_title(number)
            windows_handles = self.get_windows_handles_element(is_logger=False)
            try:
                assert len(windows_handles) == 3
            except Exception as e:
                self.logger.exception(f'获取的页面数量不正确, 获取的页面数量为: {len(windows_handles)}')
                raise e
            self.switch_to_new_window(windows_handles[-1], is_logger=False)
            re_title_text = regular_expression(r'^(.*?)\[.+\]$', title_text)[0]
            try:
                assert self._get_hire_detail_title() == re_title_text
            except Exception as e:
                self.logger.exception(f'进入招聘详情页失败')
                raise e

            hire_position_type = self._get_hire_position_type()

            if hire_position_type not in ('测试工程师', '自动化测试'):
                self.logger.info(
                    f'{company_name}招聘: {title_text}不符合期望, 职位类型不符合期望: {hire_position_type}')
                self._close_hire_detail_page(windows_handles)
                continue

            hire_detail_msg = self._get_hire_detail_msg()

            fail_msg_text_count = 0
            for failMsgText in settings.FAIL_TEXTS:
                if failMsgText in hire_detail_msg:
                    fail_msg_text_count += 1
                    self.logger.info(
                        f'{company_name}招聘: {title_text}招聘详情不符合期望, 存在关键字: {failMsgText}')
                    break

            if fail_msg_text_count > 0:
                self._close_hire_detail_page(windows_handles)
                continue

            communicate_button_text = self._get_communicate_button_text()

            self._click_communicate_button()



            if communicate_button_text == '立即沟通':
                self.logger.debug(f'{company_name}招聘: {title_text}已进行沟通')
                # self._click_communicate_pop_return_button()
            else:
                self.logger.debug(f'{company_name}招聘: {title_text}已进行投简历')
                # self._click_submit_resume_pop_return_button()

            self._close_hire_detail_page(windows_handles)

            communicate_count += 1
            update_communicate_count('laGou', add=1)

        return {'communicateCount': communicate_count}

    def _move_select_degree(self):
        self.wait_element_is_visible(
            Loc.select_degree_locator,
            action='移动选择学历',
            is_logger=False
        ).delay().move_element()

    def _click_associate_degree(self):
        self.wait_element_is_visible(
            Loc.associate_degree_locator,
            action='点击选择大专学历',
            is_logger=False
        ).delay().click_element()

    def _move_select_salary(self):
        self.wait_element_is_visible(
            Loc.select_salary_locator,
            action='移动选择薪资',
            is_logger=False
        ).delay().move_element()

    def _click_salary_expected(self):
        self.wait_element_is_visible(
            Loc.salary_15_25_locator,
            action='点击选择薪资',
            is_logger=False
        ).delay().click_element()

    def _get_hire_options_count(self):
        return len(self.wait_elment_is_loaded(
            Loc.hire_options_container_locator,
            action='获取招聘数量',
            is_logger=False
        ).get_child_elements())

    def _get_hire_pager_sub_elements(self):
        return self.wait_elment_is_loaded(
            Loc.hire_pager_container_locator,
            action='获取分页器子元素',
            is_logger=False
        ).get_child_elements()

    def _get_hire_salary(self, number):
        salary_text = self.wait_elment_is_loaded(
            Loc.hire_salary_locator(number),
            action='获取招聘薪资',
            is_logger=False
        ).get_element_text()

        # 使用正则表达式提取薪资范围
        min_salary, max_salary = regular_expression(r'^(\d+)k-(\d+)k', salary_text)

        # 将提取的薪资转换为整数
        min_salary, max_salary = int(min_salary), int(max_salary)

        # 返回归一化处理后的薪资范围
        return min_salary, max_salary

    def _get_hire_company_name(self, number):
        return self.wait_elment_is_loaded(
            Loc.hire_company_locator(number),
            action='获取招聘公司名称',
            is_logger=False
        ).get_element_text()

    def _get_hire_title(self, number):
        return self.wait_elment_is_loaded(
            Loc.hire_title_locator(number),
            action='获取招聘标题',
            is_logger=False
        ).get_element_text()

    def _click_hire_title(self, number):
        self.wait_elment_is_loaded(
            Loc.hire_title_locator(number),
            action='点击招聘标题',
            is_logger=False
        ).delay().click_element()

    def _get_hire_detail_title(self):
        hire_detail_title = self.wait_elment_is_loaded(
            Loc.hire_detail_title_locator,
            action='获取招聘详情标题',
            is_logger=False
        ).get_element_text().replace(' ', '')
        return hire_detail_title

    def _get_hire_position_type(self):
        return self.wait_elment_is_loaded(
            Loc.hire_detail_position_type_locator,
            action='获取招聘职位类型',
            is_logger=False
        ).get_element_text()

    def _get_hire_detail_msg(self):
        return self.wait_elment_is_loaded(
            Loc.hire_detail_msg_container_locator,
            action='获取招聘详情信息',
            is_logger=False
        ).get_element_text()

    def _get_communicate_button_text(self):
        return self.wait_element_is_visible(
            locator=Loc.communicate_button_locator,
            action='获取沟通按钮文本',
            is_logger=False
        ).get_element_text()

    def _click_communicate_button(self):
        self.wait_element_is_visible(
            locator=Loc.communicate_button_locator,
            action='点击沟通按钮',
            is_logger=False
        ).delay().click_element()

    def _click_communicate_pop_return_button(self):
        self.wait_element_is_visible(
            locator=Loc.communicate_pop_return_button_locator,
            action='点击沟通弹窗返回按钮',
            is_logger=False
        ).delay().click_element()

    def _click_submit_resume_pop_return_button(self):
        self.wait_element_is_visible(
            locator=Loc.submit_resume_pop_return_button_locator,
            action='点击提交简历弹窗返回按钮',
            is_logger=False
        ).delay().click_element()

    def _slide_to_visible(self, number):
        self.wait_elment_is_loaded(
            Loc.hire_option_container_locator(number),
            action='滑动至元素可见',
            is_logger=False
        ).script_specify_element(is_end_block=True)

    def _close_hire_detail_page(self, windows_handles: list):
        self.delay()
        self.close_current_window_element(is_logger=False)
        self.switch_to_new_window(windows_handles[1], is_logger=False)
