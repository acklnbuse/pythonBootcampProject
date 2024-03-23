from selenium.webdriver import Keys, ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from bootcamp_project.pages.open_positions_page import OpenPositionPage
from bootcamp_project.base.base_page import BasePage


class QualityAssurancePage(BasePage):

    see_all_jobs_button = (By.XPATH, '//*[@id="page-head"]/div/div/div[1]/div/div/a')

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_page_load()

    def wait_page_load(self):
        self.wait.until(ec.visibility_of_element_located(self.see_all_jobs_button))

    def click_saj_button(self):
        WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(self.see_all_jobs_button)
        ).send_keys(Keys.RETURN)
        return OpenPositionPage(self.driver)

