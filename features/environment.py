from selenium import webdriver

import ConfigReader


def before_all(context):

    browser_name = ConfigReader.read_configuration("basic info", "browser")
    if browser_name.__eq__("chrome"):
        context.driver = webdriver.Chrome()
    elif browser_name.__eq__("firefox"):
        context.driver = webdriver.Firefox()
    elif browser_name.__eq__("edge"):
        context.driver = webdriver.Edge()

    context.driver.maximize_window()


def after_all(context):
    context.driver.quit()
