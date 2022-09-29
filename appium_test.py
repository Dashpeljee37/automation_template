from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time

desired_cap = {
"app" : "C:\\Users\\Dashka\\Documents\\SQ\\PROJECTS\\OBR\\1.2.2-Test.apk",
"deviceName" : "RF9N508BB5H",
"platformName" : "Android"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)

# driver = webdriver.Remote(
#     command_executor="http://localhost:4723/wd/hub", 
#     desired_capabilities=desired_cap
# )

driver.implicitly_wait(3)
driver.find_element(AppiumBy.XPATH,"//*[*[@text=\'IP\']]").click()
time.sleep(1)
input = driver.find_element(AppiumBy.XPATH,"//android.widget.EditText")
input.click()
input.clear()
input.send_keys('https://doob.world:6496/v1')
driver.find_element(AppiumBy.XPATH,'//*[*[@text=\"СОЛИХ\"]]').click()
username = driver.find_element(AppiumBy.XPATH,"//android.view.ViewGroup[2]/android.widget.EditText")
username.click()
username.clear()
username.send_keys("anuujin.e")
password = driver.find_element(AppiumBy.XPATH,'//android.view.ViewGroup[3]/android.widget.EditText')
password.click()
password.clear()
password.send_keys("qweqwe123")

driver.find_element(AppiumBy.XPATH,'//*[@text=\"НЭВТРЭХ\"]').click()

#driver.quit()