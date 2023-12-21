from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import ConfigReader


def before_all(context):
    browser_name = ConfigReader.read_configuration("basic info", "browser")
    if browser_name.__eq__("chrome"):
        chromedriver_path = 'chromedriver'
        chrome_options = Options()
        #chrome_options.add_argument("--headless") #mode sin cabeza
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--allow-running-insecure-content")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--test-type")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-translate")
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-download-notification")
        chrome_options.add_argument(f'--webdriver-path={chromedriver_path}')
        driver = context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        return driver
        # context.driver = webdriver.Chrome(options=chrome_options)
        # webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
