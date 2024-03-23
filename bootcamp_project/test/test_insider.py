import time

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec



from bootcamp_project.base.base_test import BaseTest
from bootcamp_project.pages import open_positions_page, quality_assurance_page
from bootcamp_project.pages.home_page import HomePage


class TestInsider(BaseTest):

    def test_insider(self):

        home_page = HomePage(self.driver)
        home_page.click_company_button()
        careers_page = home_page.click_careers_button()

        location_text = careers_page.get_location_text()
        self.assertEqual(location_text, 'Sao Paulo')

        life_at_insider_text = careers_page.get_life_at_insider_text()
        self.assertEqual(life_at_insider_text, 'Life at Insider')

        careers_page.click_teams_button()
        quality_assurance_page = careers_page.click_qa_team_button()
        open_positions_page = quality_assurance_page.click_saj_button()

        open_positions_page.click_accept_all_button()
        time.sleep(10)
        open_positions_page.click_filter_container()
        open_positions_page.click_filter_id()

        open_positions_page.check_job_positions()
        time.sleep(10)
        open_positions_page.click_view_button()
        open_positions_page.check_link_text()

        time.sleep(10)
