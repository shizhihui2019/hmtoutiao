# 13+++++++++++++++
import pytest
import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
# 获取日志对象
from tools.get_log import GetLog
from tools.read_yaml import read_yaml

log = GetLog.get_logger()


class TestMisLogin:
    # 初始化
    def setup_class(self):
        # 获取driver
        driver = GetDriver.get_driver(page.url_mis)
        # 获取PageMisLogin
        self.mis_login = PageIn(driver).page_get_PageMisLogin()

    # 结束
    def teardown_class(self):
        # 关闭driver
        GetDriver.quit_driver()

    # 登陆测试方法
    # def test_mis_login(self, username="testid", pwd="testpwd123",expect:"管理员"):
    @pytest.mark.parametrize("username,pwd,expect", read_yaml("mis_login.yaml"))
    def test_mis_login(self, username, pwd, expect):
        # 调用登陆业务方法
        self.mis_login.page_mis_login(username, pwd)

        print("登录的结果为:", self.mis_login.page_get_nickname())
        try:
            # 断言
            assert expect in self.mis_login.page_get_nickname()
        except Exception as e:
            # 日志
            log.error(e)
            # 截图
            self.mis_login.base_get_img()
            # 抛异常
            raise
