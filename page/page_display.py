import allure
import page
from base.base_action import Base


class PageDisplay(Base):

    # 点击显示
    @allure.step(title="点击显示")
    def page_click_display(self):
        self.base_click(page.setting_display)

    # 点击搜索按钮
    def page_click_search(self):
        self.base_click(page.setting_display_search)

    # 输入框输入内容
    @allure.step(title="输入框输入内容")
    def page_search_input(self, value):
        allure.attach(value, "搜索内容", allure.attachment_type.TEXT)
        self.base_input(page.setting_display_search_input, value)
        # allure.attach.file("", '截图', attachment_type=allure.attachment_type.PNG)
        # allure.attach.file("截图", r"C:\Users\lenovo\PycharmProjects\android_test\report\picture.png",  attachment_type=allure.attachment_type.PNG)

    # 点击返回
    def page_search_input_return(self):
        self.base_click(page.setting_display_search_return)

