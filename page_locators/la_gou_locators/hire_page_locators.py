class HirePageLocators:

    select_degree_locator = ('xpath', '/html/body/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/div/ul/li[2]/div')

    associate_degree_locator = (
        'xpath', '/html/body/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/div/ul/li[2]/div/div/ul[2]/li[1]')

    select_salary_locator = ('xpath', '/html/body/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/div/ul/li[3]/div')

    salary_15_25_locator = (
        'xpath', '/html/body/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/div/ul/li[3]/div/div/ul[2]/li[5]')

    # hire_options_container_locator = ('xpath', '/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[1]')
    hire_options_container_locator = ('xpath', '//div[@class="list__YibNq"]')

    hire_pager_container_locator = ('xpath', '/html/body/div[1]/div[2]/div/div[3]/div[3]/div/div[3]/ul')

    # 招聘容器定位
    @staticmethod
    def hire_option_container_locator(number):
        return (
            'xpath',
            # f'/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/div[{number}]',
            f'(//div[@class="item__10RTO"])[{number}]',
        )

    # 招聘薪资定位
    @staticmethod
    def hire_salary_locator(number):
        return (
            'xpath',
            # f'/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/div[{number}]/div[1]/div[1]/div[2]/span',
            f'(//span[@class="money__3Lkgq"])[{number}]',
        )

    # 招聘公司定位
    @staticmethod
    def hire_company_locator(number):
        return (
            'xpath',
            # f'/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/div[{number}]/div[1]/div[2]/div[1]/a',
            f'(//div[@class="company-name__2-SjF"])[{number}]',
        )

    # 招聘标题定位
    @staticmethod
    def hire_title_locator(number):
        return (
            'xpath',
            # f'/html/body/div/div[2]/div/div[3]/div[3]/div/div[1]/div[{number}]/div[1]/div[1]/div[1]/a',
            f'(//a[@id="openWinPostion"])[{number}]',
        )

    # hire_detail_title_locator = ('xpath', '/html/body/div[1]/div[2]/div[1]/div/div[1]/div[1]/h1/span/span/span[1]')
    hire_detail_title_locator = ('xpath', '//span[@class="position-head-wrap-position-name"]')

    # hire_detail_position_type_locator = ('xpath', '/html/body/div[1]/div[2]/div[1]/div/div[1]/dd/h3/span[4]')
    hire_detail_position_type_locator = ('xpath', '//span[@class="tag-point"]')

    # hire_detail_msg_container_locator = ('xpath', '/html/body/div[1]/div[2]/div[2]/div[1]/dl[1]/dd[2]/div')
    hire_detail_msg_container_locator = ('xpath', '//div[@class="job-detail"]')

    # communicate_button_locator = ('xpath', '/html/body/div[1]/div[2]/div[1]/div/div[1]/div[2]/div/div[2]/a')
    communicate_button_locator = ('xpath', '//a[@class="btn fr btn_apply"]')

    communicate_pop_return_button_locator = ('xpath', '/html/body/div[5]/div/div[2]/div/div[2]/div/div/button/span')

    submit_resume_pop_return_button_locator = ('xpath', '/html/body/div[5]/div/div[2]/div/div[2]/div[2]/button[2]')

