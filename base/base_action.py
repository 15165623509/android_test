from selenium.webdriver.support.wait import WebDriverWait


class Base:

    def __init__(self, driver):
        self.driver = driver

    def base_find_element(self, loc, timeout=30, poll=0.5):
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*loc))

    def base_click(self, loc):
        self.base_find_element(loc).click()

    def base_input(self, loc, value):
        self.base_find_element(loc).send_keys(value)

    def base_clear(self, loc):
        self.base_find_element(loc).clear()