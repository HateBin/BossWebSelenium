from page_objects.base_page import BasePage
from page_locators.boss_locators.login_page_locators import LoginPageLocators as Loc

class LoginPage(BasePage):
    '''
    把一个页面抽象成一个类，所有这个页面上的功能封装成方法
    '''
    # 页面名称
    name = 'BOSS登录页面'

    def go_to_login(self):
        """
        点击跳转登录页按钮，进入登录页面。

        该方法用于在当前页面找到并点击跳转到登录页面的按钮。它使用`wait_element_is_visible`方法
        等待跳转按钮出现并变得可见，然后点击该按钮以导航到登录页面。
        """
        self.wait_element_is_visible(
            locator=Loc.go_to_login_button_locator, action='点击跳转登录页按钮'
        ).click_element()

    def click_wechat_login(self):
        """
        点击微信登录按钮，以便用户可以通过微信登录。

        该方法使用显式等待来确保微信登录按钮可见，然后点击该按钮。
        """
        self.wait_element_is_visible(
            locator=Loc.wechat_login_button_locator, action='点击微信登录按钮'
        ).click_element()
