from behave import given, when, then

from features.pages import DashboardPage
from features.pages.DashboardPage import AssertionUtils
from features.pages.LoginPage import LoginPage


@given(u'that the user is on the login site')
def step_impl(context):
    login_page = LoginPage(context.driver)
    login_page.open_the_login_page()


@when(u'he types login data "{username}" "{password}"')
def step_impl(context, username, password):
    login_page = LoginPage(context.driver)
    login_page.fill_username(username)
    login_page.fill_password(password)
    login_page.click_on_login()


@then(u'will see the "{text}" page')
def step_impl(context, text):
    expected_title = text
    DashboardPage.AssertionUtils(expected_title)

