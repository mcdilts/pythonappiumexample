# test_example.py
# -*- coding: utf-8 -*-
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.appium_service import AppiumService


# this is for connecting to the genymotion instance that sits on your tunneled port 5555
# @pytest.mark.parametrize("udid, systemPort", [
#   ("35.172.146.129:5555", "8201"),
# ]
#                         )
def test_open_weavr_panel():
    capabilities = {
        'platformName': 'Android',
        'deviceName': 'Genymotion Cloud PaaS',
        'appPackage': 'com.atakmap.app',
        'appActivity': '.ATAKActivity',
        'systemPort': 5556,
        'automationName': 'UiAutomator2',
        'noReset': True,
    }
    appium_service = AppiumService()
    appium_service.start()
    url = 'http://localhost:4723/wd/hub'
    driver = webdriver.Remote(url, capabilities)
    touchactions = TouchAction(driver)

    try:
        # need to wait here because ATAK takes a bit to get it's UI running
        driver.implicitly_wait(20)

        # find the main menu button and click on it
        main_menu_button = driver.find_element_by_class_name("android.widget.ImageButton")
        main_menu_button.click()

        # interact with the main menu by scrolling it until the points of interest app is visible and then clicking on
        # it
        weavr_menu_button = driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text('
            '"Points Of Interest").instance(0));')
        weavr_menu_button.click()

        # find and verify that the tests_weavr_app is present
        weavr_panel = driver.find_element_by_id("com.chesapeaketechnology.takwatch.apps.poi:id/recycleViewPoi")
        assert weavr_panel.is_enabled() == 1

    finally:
        # teardown appium
        driver.quit()
        appium_service.stop()
