import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Interactions:

    def __init__(self, driver):
        self.driver = driver

    def move_to(self, x, y):
        actions = ActionChains(self.driver)
        actions.move_by_offset(x, y).click().perform()
        time.sleep(1)

    def dropdown_li_list(self, element, text):
        element = self.driver.find_element(By.XPATH, element)
        options = element.find_elements(By.TAG_NAME, "li")
        for i in options:
            i_text = str(i)
            if i_text == text:
                i.click()
            else:
                print(f'Text of "{i}" does not match with: {text}')

    def dropdown_select_list(self, element, text):
        element = Select(self.driver.find_element(By.XPATH, element))
        element.select_by_visible_text(text)

    def js_click(self, element):
        self.driver.execute_script("arguments[0].click();", element)
