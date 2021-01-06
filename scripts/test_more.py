import pytest
import allure
from page.page_more import PageMore
from base.base_driver import init_driver


class TestDisplay:

    def setup(self):
        self.driver = init_driver()
        self.more = PageMore(self.driver)

    def teardown(self):
        self.driver.quit()

    def test_2G(self):
        self.more.page_click_more()
        self.more.page_click_more_mobile_network()
        self.more.page_click_more_mobile_network_first()
        self.more.page_click_more_mobile_network_first_2G()

    @allure.severity(allure.severity_level.BLOCKER)
    def test_3G(self):
        self.more.page_click_more()
        self.more.page_click_more_mobile_network()
        self.more.page_click_more_mobile_network_first()
        self.more.page_click_more_mobile_network_first_3G()

    @allure.severity(allure.severity_level.CRITICAL)
    def test_4G(self):
        print("1")
        assert 1

    @allure.severity(allure.severity_level.CRITICAL)
    def test_5G(self):
        print("0")
        assert 0