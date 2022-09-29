from appium.webdriver.common.appiumby import AppiumBy as By

class Locator:
    """Locator objects for finding Selenium WebElements"""
    def __init__(self, l_type, selector):
        self.l_type = l_type
        self.selector = selector

    def parameterize(self, *args):
        self.selector = self.selector.format(*args)

class LoginPageLocator:
    """Class for google search page selectors"""
    LOGIN_IP = Locator(By.XPATH, "//*[*[@text=\'IP\']]")
    lOGIN_IP_TEXTVIEW = Locator(By.XPATH, "//android.widget.EditText")
    LOGIN_IP_CHANGE_BUTT = Locator(By.XPATH, "//*[*[@text=\"СОЛИХ\"]]")
    LOGIN_USERNAME = Locator(By.XPATH, "//a[@href='{}']")
    LOGIN_PASSWORD = Locator(By.XPATH, "//a[@href='{}']")