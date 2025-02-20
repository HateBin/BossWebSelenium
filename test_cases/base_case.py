import settings
from common import logger


class BaseCase:
    name = None
    logger = logger
    settings = settings

    @classmethod
    def setup_class(cls):
        cls.logger.info("=========={}测试开始==========".format(cls.name))

    @classmethod
    def teardown_class(cls):
        cls.logger.info("=========={}测试结束==========".format(cls.name))