import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

from features.pages.Interactions import Interactions


class BusinessUnit:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.interactions = Interactions(self.driver)
        self.text = "Administration"
        self.name = "Base"

    btn_new_business = "//div[@class='tool-button add-button icon-tool-button']"
    txt_business_name = "//div[@class='s-TemplatedDialog ui-dialog-content ui-widget-content']/descendant:: input[1]"
    txt_parent_unit = "//div[@class='field ParentUnitId']//div"
    txt_unit = "//input[@aria-owns='select2-results-1']"
    btn_save_unit = "//div[@class='tool-button save-and-close-button icon-tool-button']"
    txt_validation = "//section[@class='content']/descendant:: a[contains(text(),'{}')]"
    def wait_for_element_to_be_clickeable(self, by, locator):
        return self.wait.until(EC.element_to_be_clickable((by, locator)))

    def click_on_new_business(self):
        __element = self.wait_for_element_to_be_clickeable(By.XPATH, self.btn_new_business)
        __element.click()

    def write_unit_name(self):
        __element = self.wait_for_element_to_be_clickeable(By.XPATH, self.txt_business_name)
        __element.send_keys(self.name)

    def choose_from_dropdown(self):
        __element = self.wait_for_element_to_be_clickeable(By.XPATH, self.txt_parent_unit)
        __element.click()
        __txt_unit = self.wait_for_element_to_be_clickeable(By.XPATH, self.txt_unit)
        __txt_unit.send_keys("Administration")
        __txt_unit.send_keys(Keys.ENTER)

    def click_on_save(self):
        __element = self.wait_for_element_to_be_clickeable(By.XPATH, self.btn_save_unit)
        __element.click()
        time.sleep(3)

    def assert_element_created(self):
        variable = self.name
        __validation = self.driver.find_element(By.XPATH, self.txt_validation.format(variable))
        text_to_validate = __validation.text
        assert variable == text_to_validate
