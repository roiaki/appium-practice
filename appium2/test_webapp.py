import time  # 修正箇所

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = dict(
    deviceName='Android',
    platformName='Android',
    browserName='Chrome',
    automationName='UiAutomator2',
)

capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote('http://localhost:4723', options=capabilities_options)
driver.get("http://google.com")

driver.find_element(AppiumBy.XPATH, '//*[@name="q"]').send_keys("Hello Appium!!!")
print(driver.title)

time.sleep(10)

driver.quit()

