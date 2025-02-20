class LoginPageLocators:
    '''
    登录页面的定位信息
    '''

    # 定位信息放到类属性中
    # 登录页按钮定位
    go_to_login_button_locator = ('xpath', '/html/body/div[1]/div[1]/div[1]/div[4]/div/a')
    # 微信登录按钮定位
    wechat_login_button_locator = ('xpath', '/html/body/div/div/div[2]/div[2]/div[2]/div[1]/div[4]/a')
    # 用户输入框定位
    username_locator = ('xpath', '//input[@id="form_item_account"]')
    # 密码输入框定位
    password_locator = ('xpath', '//input[@id="form_item_password"]')
    # 登录按钮定位
    login_locator = ('xpath', '//*[@class="ant-btn ant-btn-primary ant-btn-lg ant-btn-block"]')
    # 记住密码勾选框定位
    rememberPassword_locator = ('xpath', '//*[@class="ant-checkbox"]')
    # 图形验证码
    imgCode_locator = (
        'xpath',
        '/html/body/div[*]/div/div/div/div/div/div/div[2]/form/div[3]/div/div/div/div/img'
    )
    # 输入框错误提示 -- 账号和密码都为空时该元素会出现两个
    error_inputBox_locator = ('xpath', '//*[@class ="ant-form-item-explain-error"]')
    # 错误提示弹窗
    error_pop_locator = ('xpath', '//*[@class ="ant-message-notice-content"]')

