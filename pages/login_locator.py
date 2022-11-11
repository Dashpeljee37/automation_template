from appium.webdriver.common.appiumby import AppiumBy as By

class Locator:
    """Locator objects for finding Selenium WebElements"""
    def __init__(self, l_type, selector):
        self.l_type = l_type
        self.selector = selector
class LoginPageLocator:
    """Class for google search page selectors"""
    LOGIN_IP = Locator(By.XPATH, "//*[*[@text=\'IP\']]")
    lOGIN_IP_TEXTVIEW = Locator(By.XPATH, "//android.widget.EditText")
    LOGIN_IP_CHANGE_BUTT = Locator(By.XPATH, "//*[*[@text=\"СОЛИХ\"]]")
    LOGIN_USERNAME = Locator(By.XPATH, "//android.view.ViewGroup[2]/android.widget.EditText")
    LOGIN_PASSWORD = Locator(By.XPATH, "//android.view.ViewGroup[3]/android.widget.EditText")
    LOGIN_BUTT = Locator(By.XPATH, '//*[@text=\"НЭВТРЭХ\"]')
    POPUP = Locator(By.XPATH, '//*[@text=\"ХААХ\"]')