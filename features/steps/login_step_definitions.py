from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@given(u'that the user is on the login site')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://demo.serenity.is/Account/Login/?ReturnUrl=%2F")
    time.sleep(3)



@when(u'he types login data')
def step_impl(context):
    txt_username = context.driver.find_element(By.XPATH, "//input[@id='LoginPanel0_Username']")
    txt_username.clear()
    txt_username.send_keys("admin")
    txt_password = context.driver.find_element(By.XPATH, "//input[@id='LoginPanel0_Password']")
    txt_password.clear()
    txt_password.send_keys("sereniy")
    btn_submit = context.driver.find_element(By.XPATH, "//button[@id='LoginPanel0_LoginButton']")
    btn_submit.click()
    time.sleep(3)


@then(u'will see the dashboard page')
def step_impl(context):
    assert context.driver.find_element(By.XPATH, "//h1").is_displayed()
