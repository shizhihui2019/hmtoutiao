from time import sleep
from selenium.webdriver.common.by import By
from base.base import Base


class AppBase(Base):
    '''存储 app应用专属方法'''

    # # 从右向左滑动
    def base_app_right_to_left(self, area_loc, find_text):
        # 获取区域元素
        el = self.base_find(area_loc)
        # 获取区域 位置
        location = el.location
        y = location.get("y")
        # 获取元素宽高
        # 宽*0.8 高*0.5 宽*0.2 高*0.5,高取一样值,定一个点不动,宽取范围值,左右滑动
        size = el.size
        width = size.get("width")
        height = size.get("height")
        # 计算 start_x start_y end_x end_y
        start_x = width * 0.8
        start_y = y + height * 0.5
        end_x = width * 0.2
        end_y = y + height * 0.5

        # 组合 find_text包含的元素定位信息
        # //android.widget.HorizontalScrollView-->代表//class
        loc = By.XPATH, "//android.widget.HorizontalScrollView//*[contains(@text,'{}')]".format(find_text)

        # 获取当前页面结构
        page_source = self.driver.page_source
        while True:
            # 首先 查找一次当前页面是否存在 要找的元素
            try:
                el = self.base_find(loc, timeout=3)
                print("找到指定频道啦！")
                sleep(2)
                el.click()
                sleep(2)
                # 跳出循环
                break
            except:
                print("当前页面没有找到指定的频道元素！")
                # 滑动屏幕
                self.driver.swipe(start_x, start_y, end_x, end_y, 2000)
                # self.driver.swipe(start_x=940, start_y=390, end_x=4, end_y=315, duration=2000)-->错误
            if page_source == self.driver.page_source:
                print("滑不动啦，找不到！")
                raise Exception("异常啦！滑到最后一屏幕也没找到！")
            else:
                # 更新 paage_source的值
                page_source = self.driver.page_source

    def base_app_down_to_up(self,area_loc, find_text ):
        # 获取区域元素
        el = self.base_find(area_loc)
        # 获取元素宽高
        # 宽*0.2 高*0.5 宽*0.8 高*0.5,高取一样值,定一个点不动,宽取范围值,左右滑动
        size = el.size
        width = size.get("width")
        height = size.get("height")
        # 计算 start_x start_y end_x end_y
        start_x = width * 0.5
        start_y = height * 0.85
        end_x = width * 0.5
        end_y = height * 0.15

        # 组合 find_text包含的元素定位信息
        # //android.widget.HorizontalScrollView-->代表//class
        loc = By.XPATH, "//*[@bounds='[0,390][1080,1716]']//*[contains(@text,'{}')]".format(find_text)

        # 获取当前页面结构
        page_source = self.driver.page_source
        while True:
            # 首先 查找一次当前页面是否存在 要找的元素
            try:
                print("正在查找包含文章标题:{}".format(find_text))
                el = self.base_find(loc, timeout=3)
                print("找到 包含{} 文化周那个的标题啦! --> 文化周那个标题为:{}".format(find_text,el.text))
                sleep(2)
                el.click()
                sleep(2)
                # 跳出循环
                break
            except:
                print("当前页面没有找到指定的文章标题!")
                # 滑动屏幕
                self.driver.swipe(start_x, start_y, end_x, end_y, 2000)
            if page_source == self.driver.page_source:
                print("滑不动啦，找不到！")
                raise Exception("异常啦！滑到最后一屏幕也没找到！")
            else:
                # 更新 paage_source的值
                page_source = self.driver.page_source
