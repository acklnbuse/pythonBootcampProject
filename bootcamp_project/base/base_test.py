import unittest
from selenium import webdriver


class BaseTest(unittest.TestCase):
    driver = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.driver = webdriver.Chrome()
        self.errors = []
        self.driver.get('https://useinsider.com/')
        self.driver.maximize_window()

    def get_driver(self, driver):
        if driver == 'chrome':
            self.driver = webdriver.Chrome()
        elif driver == 'safari':
            self.driver = webdriver.Safari()
        elif driver == 'firefox':
            self.driver = webdriver.Firefox()
        return self.driver

    def finalize(self):
        if self.errors:
            error_message = "\n".join(self.errors)
            raise AssertionError(f"Soft assertion failed wiith the following messages: {error_message}")

    def close_browser(self):
        self.driver.quit()
