from time import sleep

from base.base import Base


class AppBase(Base):
    '''存储app应用专属方法'''

    def app_base_swipe(self, y):
        # 获取手机分辨率-->返回{}
        size = self.driver.get_window_size()
        # 宽
        width = size.get('width')
        # 高
        height = size.get('height')
        # 滑动前等待
        sleep(2)

        # 宽*0.8 高*0.5 宽*0.2 高*0.5,高取一样值,定一个点不动,宽取范围值,左右滑动
        start_x = width * 0.8
        start_y = y + height * 0.5
        end_x = width * 0.2
        end_y = y + width * 0.5

        self.driver.swipe(start_x, start_y, end_x, end_y, 2000)

        # 滑动前:
        page1 = self.driver.page_source()

        # 滑动后
        if page1 == self.driver.page_source():
            print("找到元素啦!")

        else:
            page1 = self.driver.page_source()
            print("没有找到对应元素!")
