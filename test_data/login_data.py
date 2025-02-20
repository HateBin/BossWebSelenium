import settings
username = settings.TEST_USER_DIST['account']
password = settings.TEST_USER_DIST['password']
# 正向用例
success_cases = [
    {
        'title': "登录成功-不记住账号密码",
        'request_data': {"username": username, "password": password, "rememberPassword": False}
    }
    # ,
    # {
    #     'title': "登录成功-记住账号密码",
    #     'request_data': {"username": username, "password": password, "rememberPassword": True}
    # }
]

# 反向用例
fail_cases = [
    {
        'title': "用户名为空",
        'request_data': {"username": "", "password": password},
        'error_text': "请输入账号"
    },
    {
        'title': "密码为空",
        'request_data': {"username": username, "password": ""},
        'error_text': "请输入密码"
    },
]

# 用户名密码错误用例
error_cases = [
    {
        'title': "输入的账号不存在",
        'request_data': {"username": "username", "password": password},
        'error_text': "用户不存在"
    },
    {
        'title': "输入的密码错误",
        'request_data': {"username": username, "password": "password"},
        'error_text': "密码错误"
    },
    {
        'title': "拥有角色但没有管理后台权限的用户",
        'request_data': {"username": "单位用户02", "password": "aa123456"},
        'error_text': "当前用户无权限访问本系统，请联系管理员分配权限"
    },
    {
        'title': "用户未拥有角色",
        'request_data': {"username": "pengjianbin1111", "password": "czxf@123"},
        'error_text': "当前用户无权限访问本系统，请联系管理员分配权限"
    }
]