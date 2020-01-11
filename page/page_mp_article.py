# 10++++++++++++++++++
import time

import page
from base.base import Base


class PageMpArticle(Base):
    # 点击 内容管理
    def page_click_content_manage(self):
        time.sleep(3)
        self.base_click(page.mp_content_manage)

    # 点击 发布文章
    def page_click_publish_article(self):
        time.sleep(2)
        self.base_click(page.mp_publish_article)

    # 输入 文章标题
    def page_input_title(self, title):
        time.sleep(2)
        self.base_input(page.mp_title, title)

    # 输入 文章内容
    def page_input_article_content(self, content):
        time.sleep(2)
        # 切换iframe
        # 切换iframe,建议使用 元素
        # 回到默认目录--> parent_frame,switch_to两种方法
        el = self.base_find(page.mp_iframe)
        self.driver.switch_to.frame(el)
        # 输入内容
        self.base_input(page.mp_content, content)
        # 切换默认目录
        self.driver.switch_to.default_content()

    # 选择封面
    def page_click_cover(self):
        time.sleep(2)
        # 点击 选择封面
        self.base_click(page.mp_cover)

    # 选择 频道
    def page_click_channel(self):
        # 点击选择频道
        self.base_click(page.mp_select)
        time.sleep(3)
        # 选择具体频道
        self.base_click(page.mp_select_database)

    # 点击 发表
    def page_click_commit(self):
        self.base_click(page.mp_commit)

    # 获取发布 结果提示信息
    def page_get_commit_result(self):
        return self.base_get_text(page.mp_commit_result)

    # 组合发布业务方法
    def page_publish_article(self, title, content):
        self.page_click_content_manage()
        self.page_click_publish_article()
        self.page_input_title(title)
        self.page_input_article_content(content)
        self.page_click_cover()
        self.page_click_channel()
        self.page_click_commit()
