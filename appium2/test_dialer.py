import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from appium import webdriver
from appium.options.android import UiAutomator2Options

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

desired_caps = dict(
    deviceName='Android',
    platformName='Android',
    appPackage='com.android.dialer',
    appActivity='.main.impl.MainActivity',
    #chromedriver_autodownload=True,
)

capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote('http://localhost:4723', options=capabilities_options)

driver.find_element(AppiumBy.ID, 'com.android.dialer:id/fab').click()
wait = WebDriverWait(driver, 200)
driver.find_element(AppiumBy.ID, 'com.android.dialer:id/one').click()
driver.find_element(AppiumBy.ID, 'com.android.dialer:id/two').click()
driver.find_element(AppiumBy.ID, 'com.android.dialer:id/three').click()

driver.find_element(AppiumBy.ID, 'com.android.dialer:id/search_action_text').click()

last_name_field = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.EditText[@text='姓']")))
last_name_field.send_keys('山田')

first_name_field = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.EditText[@text='名']")))
first_name_field.send_keys('太郎')

element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("電話番号"))')

tel_field = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.EditText[@text='電話番号']")))
tel_field.send_keys('123456789')

time.sleep(10)
driver.quit()

