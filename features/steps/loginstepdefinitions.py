from behave import given, when, then
from driver import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import ConfigReader
from features.pages.DashboardPage import DashboardPage
from features.pages.LoginPage import LoginPage


@given(u'that the user is on the login site')
def step_impl(context):
    login_page = LoginPage(context.driver)
    login_page.open_the_login_page()


@when(u'he types login data')
def step_impl(context):
    login_page = LoginPage(context.driver)
    login_page.fill_username()
    login_page.fill_password()
    login_page.click_on_login()


@then(u'will see the dashboard page')
def step_impl(context):
    dashboard_page = DashboardPage(context.driver)
    dashboard_page.validate_the_title()
