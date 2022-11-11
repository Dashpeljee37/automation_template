from context.config import settings
from context.driver import driver 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import allure
from allure_commons.types import AttachmentType
import io, base64
from PIL import Image
import os


class Page:
    """Base class for all page objects in the Page Object Model"""
    def __init__(self):
        self.driver = driver.get_driver()

    def _execute_with_wait(self, condition, timeout):
        return WebDriverWait(self.driver, timeout).until(condition)

    def element_exists(self, locator,timeout):
        try:
            self._execute_with_wait(
                EC.presence_of_element_located(
                    (locator.l_type, locator.selector)),timeout
            )
            return True
        except TimeoutException:
            print("element is not found")
            return False

    def get_element(self, locator,):
        if not self.element_exists(locator,int(settings.config['MOBILE']['app_timeout'])):
            raise NoSuchElementException("Could not find {locator.selector}")

        return self.driver.find_element(locator.l_type, locator.selector)

    def wait_element_by_timeout(self,locator,timeout):
        if not self.element_exists(locator,timeout):
            raise NoSuchElementException("Could not find {locator.selector}")
        
        return self.driver.find_element(locator.l_type, locator.selector)

    def picture(self,element,name=""):
        path = ".\\.tmp\\temp.png"
        self.driver.get_screenshot_as_file(path) 
        # img = Image.open(io.BytesIO(base64.decodebytes(bytes(self.driver.get_screenshot_as_base64(), "utf-8"))))
        # img.save(path)
        with open(path,"rb") as image:
            file = image.read()
            byte_array = bytearray(file)
            allure.attach(byte_array, name=name, attachment_type=AttachmentType.PNG)
        os.unlink(".\\.tmp\\temp.png")