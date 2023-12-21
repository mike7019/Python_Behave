from behave import given, when, then

from features.pages.DashboardPage import DashboardPage
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
    dashboard_page = DashboardPage(context.driver)
    expected_title = text
    actual_title = dashboard_page.get_dashboard_title()
    assert expected_title == actual_title, f"Expected title: {expected_title}, Actual title: {actual_title}"


