from appium.webdriver.common.appiumby import AppiumBy as By
import time
from context.config import settings
from pages.page import Page
from pages.login_locator import LoginPageLocator
import allure

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
        try:
            popup = super().wait_element_by_timeout(LoginPageLocator.POPUP,3000)
            popup.click()
        except:
            pass
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
                super().picture(text_view,f"{settings.config['MOBILE']['ip']} гэсэн IP-г орууллаа.")
        else:
            print("IP аль хэдийн тохируулагдсан байна.")
        super().get_element(LoginPageLocator.LOGIN_IP_CHANGE_BUTT).click()
        # except Exception as e:
        #     print(f"Ip тохируулах үйлдэл хийхэд ямар нэгэн алдаа гарлаа. Алдаа нь: {e}")

    def insert_into_username_by(self,value):
        username = super().get_element(LoginPageLocator.LOGIN_USERNAME)
        username.click()
        username.clear()
        username.send_keys(value)

    def check_value_from_username_by(self,value):
        username = super().get_element(LoginPageLocator.LOGIN_USERNAME)
        username_value = username.get_attribute("text")
        if username_value == value:
            print("Оруулсан утга зөв байна.")
        else:
            print("Оруулсан утга буруу байна.")

    def insert_user_credential(self):
        username = super().get_element(LoginPageLocator.LOGIN_USERNAME)
        username.click()
        username.clear()
        username.send_keys()

login_page = LoginPage.get_instance()