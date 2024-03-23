from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from bootcamp_project.pages.quality_assurance_page import QualityAssurancePage
from bootcamp_project.base.base_page import BasePage
from selenium.webdriver import Keys


class CareersPage(BasePage):

    ready_to_disrupt = (By.XPATH, '//*[@id="page-head"]/div/div/div[1]/div/h1')
    life_at_insider = (By.XPATH, '/html/body/div[1]/section[4]/div/div/div/div[1]/div/h2')
    location = (By.CSS_SELECTOR, '#location-slider > div > ul > li:nth-child(2) > div.location-info > p')
    teams_button = (By.XPATH, '//a[contains(text(),"See all teams")]')
    qa_team_button = (By.XPATH, '//body/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[2]/div[12]/div[1]/a[1]')

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_page_load()

    def wait_page_load(self):
        self.wait.until(ec.visibility_of_element_located(self.ready_to_disrupt))

    def click_teams_button(self):
        WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(self.teams_button)
        ).send_keys(Keys.RETURN)

    def click_qa_team_button(self):
        WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(self.qa_team_button)
        ).send_keys(Keys.RETURN)
        return QualityAssurancePage(self.driver)

    def get_location_text(self):
        return WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(self.location)
        ).text

    def get_life_at_insider_text(self):
        return WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(self.life_at_insider)
        ).text
