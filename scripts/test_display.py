from time import sleep
import pytest
from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page_display import PageDisplay


class TestDisplay:

    def setup(self):
        self.driver = init_driver()
        self.display = PageDisplay(self.driver)

    def teardown(self):
        sleep(3)
        self.driver.quit()

    @pytest.mark.parametrize("args", analyze_file("test_display.yaml", "test_input"))
    def test_display_input_return(self, args):
        value = args["text"]
        self.display.page_click_display()
        self.display.page_click_search()
        self.display.page_search_input(value)
        self.display.page_search_input_return()


