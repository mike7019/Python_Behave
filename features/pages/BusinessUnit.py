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

    btn_new_business = "//div[@class='tool-button add-button icon-tool-button']"
    txt_business_name = "//div[@class='s-TemplatedDialog ui-dialog-content ui-widget-content']/descendant:: input[1]"
    txt_parent_unit = "//div[@class='field ParentUnitId']//div"
    lst_unit = "//ul[@id='select2-results-1']"
    btn_save_unit = "//div[@class='tool-button save-and-close-button icon-tool-button']"

    def wait_for_element_to_be_clickeable(self, by, locator):
        return self.wait.until(EC.element_to_be_clickable((by, locator)))

    def click_on_new_business(self):
        __element = self.wait_for_element_to_be_clickeable(By.XPATH, self.btn_new_business)
        __element.click()

    def write_unit_name(self):
        __element = self.wait_for_element_to_be_clickeable(By.XPATH, self.txt_business_name)
        __element.send_keys("fuck")

    def choose_from_dropdown(self):
        __element = self.wait_for_element_to_be_clickeable(By.XPATH, self.txt_parent_unit)
        __element.click()
        options = __element.find_elements(By.TAG_NAME, "li")
        for i in options:
            i_text = str(i)
            if i_text == self.text:
                i.click()
            else:
                print(f'Text of "{i}" does not match with: {self.text}')

    def click_on_save(self):
        __element = self.wait_for_element_to_be_clickeable(By.XPATH, self.btn_save_unit)
