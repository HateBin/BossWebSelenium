# -*- coding: utf-8 -*-
"""
@Time ： 2025/2/19 21:19
@Auth ： pengjianbin
@File ：home_page.py
"""
import settings
from page_objects.base_page import BasePage
from page_locators.boss_locators.home_page_locators import HomePageLocators as Loc
from common.tools import text_mapping_switch, regular_expression, time_sleep, update_communicate_count


class HomePage(BasePage):
    # 页面名称
    name = 'BOSS首页'

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

    def get_job_options(self):
        """
        获取页面上的岗位选项名称列表。

        此函数通过循环遍历页面上的岗位选项，直到遇到特定的类名为止。
        它使用了等待元素可见的方法来确保页面元素加载完成，以提高代码的健壮性。

        Returns:
            list: 包含所有成功获取的岗位名称的列表。
        """
        # 初始化岗位计数器和岗位名称列表
        number = 0
        jobs = []

        # 无限循环，直到找到'add-expect-btn'类名的元素为止
        while True:
            number += 1

            # 等待岗位选项元素可见，并获取其'class'属性值
            job_option_class_name = self.wait_element_is_visible(
                locator=Loc.job_option_locator(number),
                action='获取岗位选项',
                is_logger=False,
            ).get_element_attr('class')

            # 如果当前元素的类名是'recommend-job-btn has-tooltip'，则获取岗位名称并添加到列表中
            if job_option_class_name == 'recommend-job-btn has-tooltip':
                jobs.append(self.wait_element_is_visible(
                    locator=Loc.job_name_locator(number),
                    action='获取岗位名称',
                    is_logger=False,
                ).get_element_text())
            # 如果当前元素的类名是'add-expect-btn'，则结束循环
            elif job_option_class_name == 'add-expect-btn':
                break

        # 返回收集到的岗位名称列表
        return jobs

    def click_job_options(self, job_name):
        """
        点击指定的岗位选项。

        该函数通过传入的岗位名称，在岗位列表中查找并点击相应的岗位选项。
        它通过一个无限循环遍历岗位列表，直到找到匹配的岗位名称或遇到结束标志。

        参数:
        - job_name (str): 需要点击的岗位的名称。

        异常:
        - 如果岗位不存在，会记录异常并抛出。
        """
        number = 0
        while True:
            number += 1
            # 获取岗位选项的类名，以确定是否为推荐岗位按钮。
            job_option_class_name = self.wait_element_is_visible(
                locator=Loc.job_option_locator(number),
                action='获取岗位选项'
            ).get_element_attr('class')

            # 检查当前岗位选项是否为推荐岗位按钮。
            if job_option_class_name == 'recommend-job-btn has-tooltip':
                # 检查岗位名称是否与传入的job_name匹配。
                if self.wait_element_is_visible(
                        locator=Loc.job_name_locator(number),
                        action='获取岗位名称',
                        is_logger=False,
                ).get_element_text() == job_name:
                    # 如果岗位名称匹配，点击该岗位选项并退出循环。
                    self.wait_element_is_visible(
                        locator=Loc.job_name_locator(number),
                        action='获取岗位名称',
                    ).click_element()
                    break
            # 如果岗位选项不是推荐岗位按钮，检查是否为添加期望岗位按钮，这标志着岗位列表的结束。
            elif job_option_class_name == 'add-expect-btn':
                # 如果未找到指定的岗位，记录异常并抛出。
                self.logger.exception('岗位不存在')
                raise

    def communicate(self):
        """
        与招聘网站进行交互，根据设定的条件筛选并尝试沟通。

        该方法会不断检查新的招聘列表，与符合条件的招聘启事进行沟通，直到没有更多符合的启事或达到重试次数上限。
        """
        # 初始化变量
        old_job_count = 0
        retry_count = 0
        return_data = {'communicateCount': 0, 'isBreak': False, 'isGoToChat': False, 'switchJob': False}

        # 无限循环，直到满足退出条件
        while True:
            # 获取当前招聘数量
            job_count = self._get_hire_count()

            # 如果招聘数量没有变化，开始重试
            if job_count == old_job_count:
                retry_count += 1
                self.logger.info(f'招聘列表数量未发生变化, 开始进行重试')
            # 重试最多3次
            while 0 < retry_count <= 3:
                self.logger.info(f'重试次数：{retry_count}次')
                self._script_hire_list_bottom()  # 滑动招聘列表到当前列表中最后
                time_sleep()  # 加入等待时间
                job_count = self._get_hire_count()  # 重新获取当前招聘数量
                # 如果数量仍然没有变化，增加重试次数
                if job_count == old_job_count:
                    self.logger.info(f'招聘列表数量未发生变化, 开始进行重试')
                    retry_count += 1
                else:
                    # 如果数量变化，重置重试次数并跳出循环
                    retry_count = 0
                    break

            # 如果重试次数超过3次，结束操作
            if retry_count > 3:
                self.logger.info('招聘列表数量未发生变化, 结束该列表的操作')
                return_data['switchJob'] = True
                break

            # 遍历新的招聘启事，从新获取的招聘中开始遍历
            for number in range(1 + old_job_count, job_count + 1):

                title_text = self._get_hire_title(number)  # 获取招聘的标题
                company_name = self._get_hire_company(number)  # 获取招聘的公司名称
                salary: tuple = self._get_hire_salary(number)  # 获取招聘的薪资，tuple[0]为最低，tuple[1]为最高
                salary_str = f'{salary[0]}-{salary[1]}k'

                # 如果薪资不符合期望，跳过
                if salary[1] < settings.SALARY_EXPECTATION:
                    self.logger.info(f'{company_name}招聘: {title_text}薪资{salary_str}, 不符合期望')
                    continue

                # 如果招聘的子元素大于等于3个（则表示该招聘子元素存在标签）
                if self._get_hire_sub_element_count(number) >= 3:
                    is_fail_hire_label = False  # 用于标记招聘的标签是否符合期望
                    hire_label_text = self._get_hire_label_text(number)  # 获取招聘的标签
                    for failHireLabel in settings.FAIL_HIRE_LABELS:  # 遍历期望不存在的标签
                        if failHireLabel in hire_label_text:  # 如果标签存在期望不存在的标签，则表示标签不符合期望并终止循环
                            self.logger.info(f'{company_name}招聘: {title_text}的标签不符合期望: {hire_label_text}')
                            is_fail_hire_label = True
                            break
                    if is_fail_hire_label:  # 如果标签不符合期望，跳过
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

                is_fail_company = False
                for failCompanyText in settings.FAIL_COMPANIES:
                    if failCompanyText in company_name:  # 如果公司名称包含不期望的关键字，则记录company_fail_count数量并且终止循环
                        is_fail_company = True
                        self.logger.info(
                            f'{company_name}招聘: {title_text}不符合期望, 公司名称包含关键字: {failCompanyText}')
                        break

                if is_fail_company:  # 如果存在不期望的关键字在公司名称中时，则跳过
                    continue

                self._script_hire_visible_element(number)

                # 尝试点击招聘选项
                self._click_hire_option(number)

                time_sleep()

                # 滚动招聘详情组件
                self._script_element_hire_detail()

                time_sleep()

                try:
                    # 获取招聘者状态并检查是否符合期望
                    recruiter_state = self._get_recruiter_state()  # 获取招聘者状态
                    is_pass_recruiter_state = False  # 用于表示招聘者状态是否符合期望
                    for passRecruiterState in settings.PASS_RECRUITER_STATES:  # 遍历期望的招聘者状态
                        if passRecruiterState in recruiter_state:  # 如果招聘者状态符合期望，则记录is_pass_recruiter_state为True并终止循环
                            is_pass_recruiter_state = True
                            break
                    if not is_pass_recruiter_state:  # 如果招聘者状态不符合期望，则跳过
                        self.logger.info(
                            f'{company_name}招聘: {title_text}不符合期望, 招聘者状态不符合期望: {recruiter_state}')
                        continue
                except:
                    self.logger.error('获取招聘者状态失败')
                    pass

                education_background = self._get_hire_education_background()
                # 检查招聘者学历是否符合期望
                if education_background not in settings.PASS_EDUCATION_BACKGROUNDS:
                    self.logger.info(
                        f'{company_name}招聘: {title_text}不符合期望, 学历不符合期望: {education_background}')
                    continue

                # 获取招聘详情并检查是否包含失败关键字
                hire_detail_msg = self._get_hire_detail_msg()  # 获取招聘详情
                is_fail_msg = False  # 用于表示招聘详情是否包含不期望存在的关键字
                for failOption in settings.FAIL_TEXTS:  # 遍历不期望的关键字
                    if failOption in hire_detail_msg:  # 如果详情描述中包含了不期望存在的关键字则记录is_fail_msg为True并终止循环
                        is_fail_msg = True
                        self.logger.info(
                            f'{company_name}招聘: {title_text}不符合期望, 招聘详情包含了关键字: {failOption}')
                        break
                if is_fail_msg:  # 如果详情描述中包含了不期望存在的关键字，则跳过
                    continue

                # 尝试点击沟通按钮
                if not self._click_communicate_button():  # 如果点击沟通按钮失败，则跳过
                    continue

                time_sleep()

                if not self._get_navigation_bar_recommend_class():
                    self._click_navigation_bar_recommend()
                    time_sleep()
                    return_data['isGoToChat'] = True
                    return return_data
                time_sleep()

                # 检查是否能够进行沟通
                if self._get_communicate_pop_title() == '无法进行沟通':  # 如果沟通弹出标题为“无法进行沟通”，则返回沟通计数和是否正常结束表示
                    self.logger.info('无法进行沟通')
                    return_data['isBreak'] = True
                    return return_data
                else:  # 如果沟通弹出标题不为“无法进行沟通”，则记录沟通次数和点击留在此页
                    return_data['communicateCount'] += 1  # 记录沟通次数

                    # 更新yaml文件的历史沟通次数
                    update_communicate_count(count_type='boss', add=1)

                    self._click_communicate_pop_return()  # 点击留在此页
                    self.logger.debug(f'{company_name}招聘: {title_text}, 薪资{salary_str}, 已完成立即沟通')
                    time_sleep()

            # 更新旧的招聘数量
            old_job_count = job_count

        # 返回沟通计数和是否正常结束
        return return_data

    def _get_hire_count(self):
        """
        获取当前页面上招聘列表的项目数量。

        此方法通过等待招聘列表可见，然后计算列表中的子元素数量来确定招聘项目的总数。
        使用定制的定位器来找到招聘列表，并通过获取子元素的数量来返回招聘人数。

        Returns:
            int: 招聘列表中的项目数量。
        """
        return len(self.wait_element_is_visible(
            locator=Loc.hire_list_locator,
            action='获取招聘列表数量',
            is_logger=False,
        ).get_child_elements())

    def _get_hire_salary(self, number) -> tuple:
        """
        获取招聘薪资范围。

        本函数通过定位招聘薪资文本并使用正则表达式提取最小和最大薪资。
        如果最大薪资超过1000，则将薪资范围除以1000进行归一化处理。

        参数:
        - number: 用于定位招聘薪资的编号。

        返回:
        - min_salary, max_salary: 归一化处理后的最小和最大薪资。
        """
        # 获取招聘薪资文本并进行文本映射转换
        salary_text = text_mapping_switch(self.wait_element_is_visible(
            locator=Loc.hire_salary_locator(number),
            action='获取招聘薪资',
            is_logger=False,
        ).get_element_text())

        # 使用正则表达式提取薪资范围
        min_salary, max_salary = regular_expression(r'^(\d+)-(\d+)', salary_text)

        # 将提取的薪资转换为整数
        min_salary, max_salary = int(min_salary), int(max_salary)

        # 如果最大薪资超过1000，则将薪资范围除以1000进行归一化处理
        if max_salary > 1000:
            min_salary /= 1000
            max_salary /= 1000

        # 返回归一化处理后的薪资范围
        return min_salary, max_salary

    def _get_hire_title(self, number):
        """
        根据数字获取对应的招聘标题

        这个方法主要用于在一个假设的页面上，根据给定的数字定位到具体的招聘标题元素，并返回其文本内容
        它使用了webdriver的等待方法来确保元素在执行操作前是可见的，这是为了提高测试的稳定性和可靠性

        参数:
        - number: 一个整数，用于定位特定招聘标题的索引或标识符

        返回值:
        返回找到的招聘标题的文本内容如果未找到或操作失败，则可能返回空字符串或None
        """
        return self.wait_elment_is_loaded(
            locator=Loc.hire_title_locator(number),
            action='获取招聘标题',
            is_logger=False,
        ).get_element_text()

    def _get_hire_company(self, number):
        """
        根据编号获取对应的招聘公司名称。

        此方法通过等待特定的招聘公司元素变得可见，然后返回该元素的文本内容，
        即招聘公司的名称。此方法主要用于自动化测试过程中，识别和获取特定的招聘公司信息。

        参数:
        - number (int): 招聘公司的编号，用于定位特定的招聘公司元素。

        返回:
        - str: 特定招聘公司的名称文本。
        """
        # 使用显式等待，确保招聘公司元素可见后再进行文本获取操作
        return self.wait_elment_is_loaded(
            locator=Loc.hire_company_locator(number),
            action='获取招聘公司',
            is_logger=False,
        ).get_element_text()

    def _click_hire_option(self, number):
        """
        点击招聘选项

        该方法等待招聘选项可见，然后点击它。使用特定的定位器基于提供的数字找到正确的招聘选项。

        参数:
        - number (int): 用于确定特定招聘选项的数字

        返回:
        无
        """
        # 等待招聘选项可见，并执行点击操作
        self.wait_element_is_visible(
            locator=Loc.hire_option_locator(number),
            action='点击招聘选项',
            is_logger=False,
        ).delay().click_element()

    def _get_hire_sub_element_count(self, number):
        """
        根据招聘选项的编号获取其子元素的数量。

        此函数通过等待指定的招聘选项可见，然后获取其下级元素的数量。
        主要用于UI自动化测试中，以验证特定招聘选项下子选项的数量。

        参数:
        - number: 招聘选项的编号，用于定位特定的招聘选项。

        返回值:
        - 返回指定招聘选项下子元素的数量。
        """
        # 调用wait_element_is_visible方法等待元素可见，并通过get_child_elements方法获取子元素列表
        # 最后使用len函数计算子元素数量并返回
        return len(self.wait_element_is_visible(
            locator=Loc.hire_option_locator(number),
            action='获取招聘选项子元素数量',
            is_logger=False,
        ).get_child_elements())

    def _get_hire_label_text(self, number):
        """
        根据招聘选项的编号获取招聘选项标签的文本。

        参数:
        - number (int): 招聘选项的编号，用于定位特定的招聘选项标签。

        返回:
        - str: 招聘选项标签的文本。

        此方法通过等待特定的招聘选项标签变为可见，然后获取该标签的 'alt' 属性值，
        该值通常描述了标签所代表的招聘选项的文本内容。
        """
        # 等待招聘选项标签出现并获取其 'alt' 属性值
        return self.wait_element_is_visible(
            locator=Loc.hire_option_label_locator(number),
            action='获取招聘选项标签文本',
            is_logger=False,
        ).get_element_attr('alt')

    def _get_hire_education_background(self):
        """
        获取招聘学历背景信息。

        该方法通过等待特定元素变得可见来获取招聘岗位的学历背景要求文本。

        参数:
        - number: 该参数在此方法中未被使用，但可能在上下文中具有意义。

        返回值:
        - 返回招聘学历背景的文本信息。
        """
        # 等待元素变得可见，并获取该元素的文本内容
        return self.wait_element_is_visible(
            locator=Loc.hire_education_background_locator,
            action='获取招聘学历背景',
            is_logger=False,
        ).get_element_text()

    def _get_hire_detail_msg(self):
        """
        获取招聘详情页面的文本消息。

        该方法通过等待特定元素变得可见来获取招聘详情页面的文本信息。
        使用预定义的定位器来识别页面上的元素，并提取该元素的文本内容。

        :return: 招聘详情页面的文本消息。
        """
        # 等待招聘详情消息元素可见，并获取该元素的文本
        msg = self.wait_element_is_visible(
            locator=Loc.hire_detail_msg_locator,
            action='获取招聘详情文本',
            is_logger=False,
        ).get_element_text()
        return msg

    def _get_recruiter_state(self):
        """
        获取当前招聘者的状态。

        该方法通过等待指定的元素（通过Loc.recruiter_state_locator定位）变为可见状态后，
        获取该元素的文本内容作为招聘者状态返回。

        :return: 招聘者当前的状态文本。
        """
        return self.wait_elment_is_loaded(
            locator=Loc.recruiter_state_locator,
            action='获取招聘者状态',
            is_logger=False,
        ).get_element_text()

    def _click_communicate_button(self):
        """
        点击沟通按钮方法。

        该方法用于寻找并点击页面上的“立即沟通”按钮。如果按钮文本是“立即沟通”，则点击按钮并返回True，否则返回False。
        此方法主要用于UI自动化测试中，与用户界面进行交互，模拟用户点击按钮的行为。

        Returns:
            bool: 如果点击了“立即沟通”按钮，则返回True，否则返回False。
        """
        # 获取沟通按钮的文本
        button_text = self.wait_elment_is_loaded(
            locator=Loc.communicate_button_locator,
            action='获取沟通按钮文本',
            is_logger=False,
        ).get_element_text()

        # 检查按钮文本是否为“立即沟通”
        if button_text == '立即沟通':
            # 如果是“立即沟通”按钮，点击它
            self.wait_elment_is_loaded(
                locator=Loc.communicate_button_locator,
                action='点击沟通按钮',
                is_logger=False,
            ).click_element()
            return True
        return False

    def _get_communicate_pop_title(self):
        """
        获取沟通弹窗的标题文本。

        该方法通过等待特定元素变得可见，然后获取该元素的文本内容，
        以实现对沟通弹窗标题的提取。

        :return: 沟通弹窗标题的文本字符串。
        """
        # 使用显式等待，确保沟通弹窗标题元素可见，并获取其文本内容
        return self.wait_element_is_visible(
            locator=Loc.communicate_pop_title_locator,
            action='获取沟通弹窗标题',
            is_logger=False,
        ).get_element_text()

    def _click_communicate_pop_return(self):
        """
        点击沟通弹窗中的"留在此页"按钮。

        此函数通过等待元素变得可见，然后对其进行点击。
        使用了Loc.communicate_pop_return_button_locator作为元素的定位器。
        """
        self.wait_element_is_visible(
            locator=Loc.communicate_pop_return_button_locator,
            action='点击沟通弹窗"留在此页"',
            is_logger=False,
        ).click_element()

    def _script_hire_list_bottom(self):
        self.script_windows_element(script_type='bottom', is_logger=False)

    def _script_hire_visible_element(self, number):
        """
        滑动招聘列表直到指定的招聘选项可见，并执行脚本操作使该元素成为活动元素。

        参数:
        - number: 指定的招聘选项的序号，用于定位特定的招聘选项。

        返回值:
        无直接返回值，但通过链式调用最终调用了script_element方法。
        """
        # 等待指定的招聘选项可见，并执行滑动操作。这里不记录日志是为了避免不必要的输出干扰。
        self.wait_elment_is_loaded(
            locator=Loc.hire_option_locator(number),
            action='滑动招聘列表直到指定招聘选项可见',
            is_logger=False,
        ).script_specify_element(is_end_block=True)


    def _script_element_hire_detail(self):
        self.wait_element_is_visible(
            locator=Loc.hire_detail_msg_container_locator,
            action='滑动招聘详情',
            is_logger=False,
        ).script_specify_element()

    def _get_navigation_bar_recommend_class(self):
        return self.wait_element_is_visible(
            locator=Loc.navigation_bar_recommend_class_locator,
            action='获取导航栏推荐的类名',
            is_logger=False,
        ).get_element_attr('class')

    def _click_navigation_bar_recommend(self):
        self.wait_element_is_visible(
            locator=Loc.navigation_bar_recommend_locator,
            action='点击导航栏推荐的元素',
            is_logger=False,
        ).click_element()
