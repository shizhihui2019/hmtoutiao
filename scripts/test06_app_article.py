from page.page_in import PageIn
from tools.get_driver import GetDriver


class TestAppArticle:

    # 初始化
    def setup_class(self):
        # 获取driver
        driver = GetDriver.get_app_driver()
        # 通过统一入口类 对象
        self.page_in = PageIn(driver)
        # 调用登陆成功以来方法 (需要在PageAppArticle)
        self.page_in.page_get_PageAppLogin().page_app_login_success()
        # 获取PageAppArticle对象
        self.article = self.page_in.page_get_PageAppArticle()

    # 结束
    def teardown_class(self):
        # 关闭driver
        GetDriver.quit_app_driver()

    # 查找文章测试方法
    def test_app_article(self):
        # 调用查找文章方法
        self.article.page_app_article(find_text="java",title_text="java")
