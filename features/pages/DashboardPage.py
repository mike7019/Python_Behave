import logging
from selenium.webdriver.common.by import By


class AssertionUtils:

    def __init__(self, driver):
        self.driver = driver

    txt_title = "//h1"

    def assert_dashboard_title(self, expected_title):
        actual_title = self.driver.find_element(By.XPATH, self.txt_title).text()
        logging.info('Watch out!')  # will print a message to the console
        print(actual_title)
        assert expected_title == actual_title

