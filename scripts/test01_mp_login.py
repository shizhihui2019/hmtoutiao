# 5++++++++++
import time

import pytest
from tools.read_yaml import read_yaml
# 获取日志对象
from tools.get_log import GetLog

log = GetLog.get_logger()

import page
from page.page_in import PageIn
from tools.get_driver import GetDriver


class TestMpLogin:
    # 初始化
    def setup_class(self):
        # 获取driver
        self.driver = GetDriver.get_driver(page.url_mp)
        # 获取PageMpLogin对象
        self.login = PageIn(self.driver).page_get_PageMpLogin()
        print("参数化读取数据为：", read_yaml("mp_login.yaml"))

    # 结束
    def teardown_class(self):
        time.sleep(3)
        # 关闭driver
        GetDriver.quit_driver()

    # 测试业务方法
    # 把数据改成expect="13812345678-,会抛出异常并截图
    @pytest.mark.parametrize("phone,code,expect", read_yaml("mp_login.yaml"))
    # def test_mp_login(self, phone="13812345678", code="246810", expect="13812345678"):
    def test_mp_login(self, phone, code, expect):
        # 调用登录业务方法
        self.login.page_mp_login(phone, code)
        try:
            # 断言
            # print("获取的昵称为:", self.login.page_get_nickname())
            assert expect == self.login.page_get_nickname()  # 坑坑坑,,没有指定异常信息
        except Exception as e:
            # 日志 9+++++++
            log.error(e)
            # 截图
            self.login.base_get_img()
            # 抛异常
            raise
