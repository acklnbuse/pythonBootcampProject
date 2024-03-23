from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from bootcamp_project.base.base_page import BasePage
from selenium.webdriver import Keys, ActionChains


class OpenPositionPage(BasePage):
    all_open_positions = (By.XPATH, '//*[@id="page-head"]/div/div/div/h3')
    filter_container = (By.XPATH,'//body/section[@id="career-position-filter"]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/span[1]/span[1]/span[1]')
    accept_all_button = (By.XPATH, '//*[@id="wt-cli-accept-all-btn"]')
    job_list = (By.CSS_SELECTOR, '#jobs-list')

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_page_load()

    def wait_page_load(self):
        self.wait.until(ec.visibility_of_element_located(self.all_open_positions))

    def click_accept_all_button(self):
        WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(self.accept_all_button)
        ).send_keys(Keys.RETURN)

    def click_filter_container(self):
        WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(self.filter_container)
        ).send_keys(Keys.RETURN)

    def click_filter_id(self):
        element = self.driver.find_element(By.XPATH, '/html/body/span/span/span[2]/ul/li[2]')
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(element).perform()
        element.click()

    def check_job_positions(self):
        job_positions = self.driver.find_elements(*self.job_list)
        for position in job_positions:
            department_text = position.find_element(By.CSS_SELECTOR, '#jobs-list > div:nth-child(1) > div > span').text
            location_text = position.find_element(By.CSS_SELECTOR, '#jobs-list > div:nth-child(1) > div > div').text

        #if "Quality Assurance" in department_text:
            #print('In department areas found Quality Assurance.')
        #else:
            #print('Warning: In department areas cannot find Quality Assurance.')

        #if "Istanbul, Turkey" in location_text:
            #print('In location areas found Istanbul, Turkey.')
        #else:
            #print('Warning: In location areas cannot find Istanbul, Turkey.')

    def take_screenshot(self, text_status):
        filename = f"test_result_{text_status}.png"
        self.driver.save_screenshot(filename)

    def click_view_button(self):
        element = self.driver.find_element(By.XPATH, '//*[@id="jobs-list"]/div[1]/div/a')
        action_chains = ActionChains(self.driver)

        action_chains.move_to_element(element).perform()
        element.click()

    def check_link_text(self):

        current_url = self.driver.current_url

        if "https://jobs.lever.co/useinsider/0ba4065b-955a-4661-ad4a-f32479f63757" in current_url:
            print("Success: The form page is directed.")
        else:
            print(f"Failed: Expected URL `https://jobs.lever.co/useinsider/0ba4065b-955a-4661-ad4a-f32479f63757`, but Actual URL '{current_url}'")
