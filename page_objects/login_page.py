from page_objects.base_page import BasePage
from page_locators.login_page_locators import LoginPageLocators as Loc

# import settings, time


class LoginPage(BasePage):
    '''
    把一个页面抽象成一个类，所有这个页面上的功能封装成方法
    '''
    # 页面名称
    name = '登录页面'

    def go_to_login(self):
        self.wait_element_is_visible(
            locator=Loc.go_to_login_button_locator, action='点击跳转登录页按钮'
        ).click_element()

    def click_wechat_login(self):
        self.wait_element_is_visible(
            locator=Loc.wechat_login_button_locator, action='点击微信登录按钮'
        ).click_element()

    def login(self, username, password, rememberPassword=False):
        '''
        登录页面的登录功能
        :param username:
        :param password:
        :param rememberPassword:
        :return:
        '''

        # 2.输入用户名、密码
        # 链式调用，需自己封装 在方法中返回self
        # 2.1输入用户名
        self.wait_element_is_visible(
            locator=Loc.username_locator, action="输入用户名"
        ).send_keys(username)
        # 2.2 输入密码
        self.wait_element_is_visible(
            locator=Loc.password_locator, action='输入密码'
        ).send_keys(password)
        # 2.3 记住密码
        if rememberPassword is True:
            self.wait_element_is_visible(
                locator=Loc.rememberPassword_locator, action='点击记住密码'
            ).click_element()
        # # 保存图形验证码
        # self.wait_element_is_visible(
        #     locator=Loc.imgCode_locator, action='获取图形验证码'
        # ).save_code_png()
        # print(getCode())

        # 3.点击登录按钮
        self.wait_element_is_visible(
            locator=Loc.login_locator, action='点击登录按钮'
        ).click_element()

    def get_user_value(self):
        '''
        获取用户名输入框的value
        :return:
        '''
        return self.wait_element_is_visible(
            locator=Loc.username_locator,
            action='获取用户名输入框的值').get_element_attr('value')


    def get_error_inputBox_text(self):
        '''
        获取错误提示信息
        :return:
        '''
        return self.wait_element_is_visible(
            locator=Loc.error_inputBox_locator,
            action='获取错误提示信息'
        ).get_element_text()

    def get_error_pop_text(self):
        '''
        获取弹框错误提示信息
        :return:
        '''
        return self.wait_element_is_visible(
            locator=Loc.error_pop_locator,
            action='获取错误提示信息'
        ).get_element_text()
