import time

from selenium.common import WebDriverException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




class Interactions:

    def __init__(self, driver):
        self.driver = driver

    def move_to(self, x, y):
        actions = ActionChains(self.driver)
        actions.move_by_offset(x, y).click().perform()
        time.sleep(1)

    def dropdown_ul_list(self, element, text):
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

    def drag_n_drop(self, source, target):
        element = self.driver.find_element(By.NAME, source)
        target = self.driver.find_element(By.NAME, target)
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(element, target).perform()

    def switch_to_new_window(self, windowName):
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)

    def switch_to_single_frame(self, frameName):
        self.driver.switch_to.frame(frameName)

    def back_to_context(self):
        self.driver.switch_to.default_content()

    def accept_alert(self):
        alert = self.driver.switch_to.alert

    def explicit_wait(self, locator, timeout):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, locator))
            )
        finally:
            self.driver.quit()

    def implicit_wait(self, timeout):
        self.driver.implicitly_wait(timeout)

