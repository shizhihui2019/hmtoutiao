import time
import page
from base.web_base import WebBase


class PageMisAudit(WebBase):

    # 点击信息管理
    def page_click_info_manage(self):
        self.base_click(page.mis_info_manage)
        time.sleep(2)

    # 点击内容审核
    def page_click_content_audit(self):
        self.base_click(page.mis_content_audit)
        time.sleep(2)

    # 输入文章标题
    def page_input_title(self, title):
        self.base_input(page.mis_title, title)
        time.sleep(2)

    # 输入频道
    def page_input_channel(self, channel):
        self.base_input(page.mis_channel, channel)
        time.sleep(2)

    # 选择状态-->待审核
    def page_click_status(self):
        self.web_base_click_ul_li("请选择状态", "待审核")
        time.sleep(2)

    # 点击查询按钮
    def page_click_search_btn(self):
        self.base_click(page.mis_search)
        time.sleep(1)


    # 点击通过
    def page_click_pass_btn(self):
        self.base_click(page.mis_pass_btn)
        time.sleep(2)

    # 确认通过
    def page_click_confirm_pass(self):
        self.base_click(page.mis_confirm_pass)
        time.sleep(2)

    # 获取文章id文本
    def page_get_article_id(self):
        return self.base_get_text(page.mis_article_id)

    # 组合业务方法
    def page_mis_audit(self, title, channel):
        self.page_click_info_manage()
        self.page_click_content_audit()
        self.page_input_title(title)
        self.page_input_channel(channel)
        self.page_click_status()
        self.page_click_search_btn()
        time.sleep(3) #不能少此步
        self.article_id = self.page_get_article_id()
        print(("正在审核的文章id为:", self.article_id))
        self.page_click_pass_btn()
        self.page_click_confirm_pass()

    # 断言
    def page_assert_success(self,title, channel):
        time.sleep(5)
        # 刷新
        self.driver.refresh()
        # 输入标题
        self.page_input_title(title)
        # 输入频道
        self.page_input_channel(channel)
        # 点击状态
        self.web_base_click_ul_li("请选择状态","审核通过")
        # 点击查询
        self.page_click_search_btn()
        time.sleep(3)
        return self.web_base_element_exists(self.article_id)# 判断元素是否存在
