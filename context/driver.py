from pkgutil import extend_path
from selenium import webdriver
from context.config import settings
from appium import webdriver as appiumWebDriver

class Driver(object):
    """Singleton class for interacting with the selenium webdriver object"""
    instance = None 

    class SeleniumDriverNotFound(Exception):
        pass

    @classmethod
    def get_instance(cls):
        if cls.instance == None:
            cls.instance = Driver()
        return cls.instance

    def __init__(self):
        try:
            if settings.automation_type == 'WEB':
                if settings.browser == "chrome":
                    self.driver = webdriver.Chrome()
                elif settings.browser == "firefox":
                    self.driver = webdriver.Firefox()
                else:
                    raise SeleniumDriverNotFound(
                        f"{settings.browser} not currently supported")
            elif settings.automation_type == 'MOBILE':
                print(f"connection to appium server => {settings.capabilities}")
                try:
                    self.driver = appiumWebDriver.Remote(settings.avd_server, settings.capabilities)
                except:
                    print("sda haana aldaa garaad bnaa")
                print("connected to appium server")
        except:
            print("sda ymaa")

    def get_driver(self):
        return self.driver

    def stop_instance(self):
        self.driver.quit()
        instance = None

    def clear_cookies(self):
        self.driver.delete_all_cookies()

    def navigate(self, url):
        self.driver.get(url)


driver = Driver.get_instance()