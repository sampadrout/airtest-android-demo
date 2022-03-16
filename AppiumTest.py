# -*- coding: utf-8 -*-
import unittest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

class AppiumTest(unittest.TestCase):
    dc = {}
    driver = None

    def setUp(self):
        # This is the Application and ‘app’ desired capability to specify a path to Appium.
        self.dc['app'] = 'EriBank.apk'
        # appPackage and appActivity  desired capability specify app details to Appium
        self.dc['appPackage'] = "com.experitest.ExperiBank"
        self.dc['appActivity'] = ".LoginActivity"
        # platformName desired capabsility specify platform detail to Appium
        self.dc['platformName'] = 'Android'
        # deviceName desired capability specify the device id detail to Appium
        # device id is got from running adb devices command in PC
        self.dc['deviceName'] = 'emulator-5554'
        # Creating the Driver by passing Desired Capabilities.s
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.dc)

    def testFirstAutomation(self):
        if len(self.driver.find_elements(MobileBy.XPATH, "//*[@text='OK']")) > 0:
            self.driver.find_element(MobileBy.XPATH, "//*[@text='OK']").click();
        # Find location of Elements and perform action.
        self.driver.find_element(MobileBy.XPATH, "//*[@text='Username']").send_keys('company')
        self.driver.find_element(MobileBy.XPATH, "//*[@text='Password']").send_keys('company')
        #init_device("Android")
        connect_device("Android:///")
        # auto_setup(__file__, devices=["android://0.0.0.0:4723/emulator-5554"])
        touch(Template(r"tpl1647193221237.png", record_pos=(-0.001, -0.214), resolution=(1080, 2280)))
        # self.driver.find_element_by_xpath("//*[@text='Login']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='Logout']").click()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
