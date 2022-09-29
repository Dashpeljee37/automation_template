from distutils.log import Log
from appium.webdriver.common.appiumby import AppiumBy
from controller.login_controller import login_page
from behave import *

@given('Mobile change base url')
def step(self):
    login_page.configure_ip()

@given("Mobile login as {arg}")
def step(self):
    login_page