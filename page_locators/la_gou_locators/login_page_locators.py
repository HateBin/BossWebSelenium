class LoginPageLocators:
    '''
    登录页面的定位信息
    '''

    # 定位信息放到类属性中
    # 登录页按钮定位
    go_to_login_button_locator = ('xpath', '/html/body/div/header/div[1]/div[2]/ul/li[1]/a')
    # 微信登录按钮定位
    wechat_login_button_locator = ('xpath', '/html/body/div[3]/div/div[2]/div/div[2]/div/div[2]/div[1]/div[1]/img[1]')
