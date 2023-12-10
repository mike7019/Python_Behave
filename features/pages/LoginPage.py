import time

from selenium.webdriver.common.by import By

import ConfigReader


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    txt_username = "//input[@id='LoginPanel0_Username']"
    txt_password = "//input[@id='LoginPanel0_Password']"
    btn_submit = "//button[@id='LoginPanel0_LoginButton']"

    def open_the_login_page(self):
        self.driver.get(ConfigReader.read_configuration("basic info", "url"))
        time.sleep(3)

    def fill_username(self):
        user_field = self.driver.find_element(By.XPATH, self.txt_username)
        user_field.clear()
        user_field.send_keys("admin")

    def fill_password(self):
        pass_field = self.driver.find_element(By.XPATH, self.txt_password)
        pass_field.clear()
        pass_field.send_keys("serenity")

    def click_on_login(self):
        login_button = self.driver.find_element(By.XPATH, self.btn_submit)
        login_button.click()
        time.sleep(3)