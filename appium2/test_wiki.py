import time  # 修正箇所
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = dict(
    deviceName='Android',
    platformName='Android',
    browserName='Chrome',
    automationName='UiAutomator2',
    #chromedriver_autodownload=True,
)

capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote('http://localhost:4723', options=capabilities_options)
driver.get("http://wikipedia.org")
# driver.find_element_by_id('searchLanguage')

dropdown = driver.find_element(By.CSS_SELECTOR, '#searchLanguage')
select = Select(dropdown)
select.select_by_value("hi")

options = driver.find_elements(By.TAG_NAME, 'option')
print(len(options))
for option in options:
    print("Text is : ", option.text, "Lang is:", option.get_attribute('Lang'))


print(driver.title)

# time.sleep(10)

# driver.quit()

