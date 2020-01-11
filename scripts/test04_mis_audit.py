import time
import pytest
import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
# 获取日志对象
from tools.get_log import GetLog

log = GetLog.get_logger()


class TestMisAudit:
    # 初始化
    def setup_class(self):
        # 获取driver
        driver = GetDriver.get_driver(page.url_mis)
        # 获取统一入口类对象
        self.page_in = PageIn(driver)
        # 调用登陆业务成功方法(需要在PageMisLogin新增)
        self.page_in.page_get_PageMisLogin().page_mis_login_success()
        # 获取PageMisAudit对象
        self.audit = self.page_in.page_get_PageMisAudit()

    # 结束
    def teardown_class(self):
        time.sleep(3)
        # 关闭driver
        GetDriver.quit_driver()

    # 审核文章测试方法===>可以再运行一遍test02_mp_article.py新增发布内容,然后再执行test04_mis_audit.py
    # @pytest.mark.parametrize()
    def test_mis_audit(self, title=page.article_title, channel=page.article_channel):
        # 调用审核业务方法
        self.audit.page_mis_audit(title, channel)
        try:
            # 断言
            assert self.audit.page_assert_success(title="bj-test17-999", channel="数据库")
        except Exception as e:
            # 日志
            log.error(e)
            # 截图
            self.audit.base_get_img()
            # 抛异常
            raise
