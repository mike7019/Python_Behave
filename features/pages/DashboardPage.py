import logging
import time

from screenpy_selenium import Wait, BrowseTheWeb
from selenium.common import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.core import driver
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    txt_title = "//h1"
    btn_organization = "//i[@class='s-sidebar-icon fa fa-sitemap premium-feature']"
    btn_business_unit = "//i[@class='s-sidebar-icon fa fa-sitemap']"

<<<<<<< HEAD
    def assert_dashboard_title(self, expected_title):
        actual_title = self.driver.find_element(By.XPATH, self.txt_title).get_text()
        assert expected_title.equals(actual_title)
=======
    def wait_for_element_to_be_clickable(self, by, locator):
        return self.wait.until(EC.element_to_be_clickable((by, locator)))
>>>>>>> b03eb9c68191f1695979c9b0ecfb84a050c03c82

    def get_dashboard_title(self):
        title = self.driver.find_element(By.XPATH, self.txt_title).text
        return title

    def click_on_organization(self):
        element = self.wait_for_element_to_be_clickable(By.XPATH, self.btn_organization)
        element.click()

    def click_on_business_unit(self):
        element = self.wait_for_element_to_be_clickable(By.XPATH, self.btn_business_unit)
        element.click()
