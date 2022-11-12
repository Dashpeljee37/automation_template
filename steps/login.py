from controller.login_controller import login_page
from behave import *

@given('Mobile change base url')
def step(self):
    login_page.configure_ip()

@when('insert value to username by "{value}"')
def step(self,value):
    login_page.insert_into_username_by(value)

@then('check value from username by "{value}"')
def step(self,value):
    login_page.check_value_from_username_by(value)
