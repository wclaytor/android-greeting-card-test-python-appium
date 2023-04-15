import subprocess
import pytest
import logging

# Android environment
from appium import webdriver
# Options are only available since client version 2.3.0
# If you use an older client then switch to desired_capabilities
# instead: https://github.com/appium/python-client/pull/720
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

def pytest_configure(config):
    logging.basicConfig(level=logging.INFO)

def appium_options():
    options = UiAutomator2Options()
    options.device_name = "Android08"
    options.app = "./apk/GreetingCard.apk"
    caps = dict(
        autoGrantPermissions=True
    )
    options.load_capabilities(caps)
    return options


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Remote('http://127.0.0.1:4723', options=appium_options())

    yield driver
    driver.quit()
