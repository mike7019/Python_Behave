import time

from behave import given, when, then

from features.pages.BusinessUnit import BusinessUnit
from features.pages.DashboardPage import DashboardPage


@when(u'actor creates a new unit bussiness')
def step_impl(context):
    dashboard_page = DashboardPage(context.driver)
    business_page = BusinessUnit(context.driver)
    dashboard_page.click_on_organization()
    dashboard_page.click_on_business_unit()
    business_page.click_on_new_business()
    business_page.write_unit_name()
    business_page.choose_from_dropdown()
    business_page.click_on_save()

    time.sleep(2)


@then(u'actor will see the unit created')
def step_impl(context):
    business_page = BusinessUnit(context.driver)
    business_page.assert_element_created()
