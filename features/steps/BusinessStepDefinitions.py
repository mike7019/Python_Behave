import time

from behave import given, when, then

from features.pages.BusinessUnit import BusinessUnit
from features.pages.DashboardPage import DashboardPage


@when(u'actor creates a new unit bussiness')
def step_impl(context):
    dashboard_page = DashboardPage(context.driver)
    business_Page = BusinessUnit(context.driver)
    dashboard_page.click_on_organization()
    dashboard_page.click_on_business_unit()
    business_Page.click_on_new_business()
    business_Page.write_unit_name()
    business_Page.choose_from_dropdown()
    business_Page.click_on_save()
    time.sleep(10)


@then(u'actor will see the unit created')
def step_impl(context):
    pass