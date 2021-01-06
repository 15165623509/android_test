import allure

import page
from base.base_action import Base


class PageMore(Base):

    # 点击显示
    def page_click_more(self):
        self.base_click(page.setting_more)

    # 点击移动网络
    @allure.step("点击移动网络")
    def page_click_more_mobile_network(self):
        self.base_click(page.setting_more_mobile_network)
        # allure.attach.file(r"../report/picture.png", "picture", attachment_type=allure.attachment_type.PNG)

    # 点击首选网络类型
    def page_click_more_mobile_network_first(self):
        self.base_click(page.setting_more_mobile_network_first)

    # 点击移动网络-2G
    def page_click_more_mobile_network_first_2G(self):
        self.base_click(page.setting_more_mobile_network_first_2G)

    # 点击移动网络-3G
    def page_click_more_mobile_network_first_3G(self):
        self.base_click(page.setting_more_mobile_network_first_3G)




