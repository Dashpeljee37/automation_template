from context.config import settings
from context.driver import driver 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy


class Page:
    """Base class for all page objects in the Page Object Model"""
    def __init__(self):
        self.driver = driver.get_driver()

    def _execute_with_wait(self, condition):
        return WebDriverWait(self.driver, int(settings.config['MOBILE']['app_timeout'])).until(condition)

    def element_exists(self, locator):
        try:
            self._execute_with_wait(
                EC.presence_of_element_located(
                    (locator.l_type, locator.selector))
            )
            return True
        except TimeoutException:
            return False

    def get_element(self, locator):
        if not self.element_exists(locator):
            raise NoSuchElementException("Could not find {locator.selector}")

        return self.driver.find_element(locator.l_type, locator.selector)