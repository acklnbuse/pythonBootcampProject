from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from bootcamp_project.pages.careers_page import CareersPage
from bootcamp_project.base.base_page import BasePage


class HomePage(BasePage):
    demo_hub = (By.XPATH, '//*[@id="announce"]/div[1]/div/span/b')
    navbar_nav = (By.CSS_SELECTOR, '#navbarNavDropdown > ul:nth-child(1) > li')
    careers_button = (By.XPATH, '//*[@id="navbarNavDropdown"]/ul[1]/li[6]/div/div[2]/a[2]')

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_page_load()

    def wait_page_load(self):
        self.wait.until(ec.visibility_of_element_located(self.demo_hub))

    def click_company_button(self):
        nav_list = self.driver.find_elements(*self.navbar_nav)
        for nav in nav_list:
            nav = nav.find_element(By.CSS_SELECTOR, 'a')
            if nav.text == 'Company':
                nav.click()

    def click_careers_button(self):
        self.driver.find_element(*self.careers_button).click()
        return CareersPage(self.driver)
