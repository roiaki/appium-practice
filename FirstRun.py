
from appium import webdriver
from appium.options.android import UiAutomator2Options

desired_caps = dict(

    deviceName='Android',
    platformName='Android',
    browserName='Chrome',
    automationName='UiAutomator2',

)

capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)