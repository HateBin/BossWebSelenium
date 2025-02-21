import settings
from common import logger


class BaseCase:
    name = None
    logger = logger
    settings = settings

    @classmethod
    def setup_class(cls):
        cls.logger.info("=========={}程序开始==========".format(cls.name if cls.name else ""))

    @classmethod
    def teardown_class(cls):
        cls.logger.info("=========={}程序结束==========".format(cls.name if cls.name else ""))