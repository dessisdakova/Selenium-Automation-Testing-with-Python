from selenium import webdriver


class BasePage:
    def __init__(self, driver: webdriver.Chrome):
        self._driver = driver

    @property
    def url(self):
        return "https://practicetestautomation.com"

    def load(self):
        self._driver.get(self.url)

    def get_current_url(self):
        return self._driver.current_url