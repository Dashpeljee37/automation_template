from lib2to3.pgen2 import driver
from tkinter import PAGES
from appium.webdriver.common.appiumby import AppiumBy as By
import time
from context.config import settings
from pages.page import Page
from pages.login_locator import LoginPageLocator

class LoginPage(Page):
    
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = LoginPage()
        return cls.instance

    def __init__(self):
        super().__init__()

    def configure_ip(self):                
        element = super().get_element(LoginPageLocator.LOGIN_IP)
        element.click()
        time.sleep(1)
        text_view = super().get_element(LoginPageLocator.lOGIN_IP_TEXTVIEW)
        print(text_view.get_attribute("text") + ' - ' + settings.config['MOBILE']['ip'])
        if text_view.get_attribute("text") != settings.config['MOBILE']['ip']:
            text_view.click()
            text_view.clear()
            text_view.send_keys(settings.config['MOBILE']['ip'])
            if text_view.get_attribute("text") == settings.config['MOBILE']['ip']:
                print(f"{settings.config['MOBILE']['ip']} гэсэн IP-г орууллаа.")
        else:
            print("IP аль хэдийн тохируулагдсан байна.")
        super().get_element(LoginPageLocator.LOGIN_IP_CHANGE_BUTT).click()
        # except Exception as e:
        #     print(f"Ip тохируулах үйлдэл хийхэд ямар нэгэн алдаа гарлаа. Алдаа нь: {e}")

    def insert_user_credential(self):
        username = super().get_element(LoginPageLocator.LOGIN_USERNAME)
        username.click()
        username.clear()
        username.send_keys()

login_page = LoginPage.get_instance()