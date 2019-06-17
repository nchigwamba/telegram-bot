# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Wifi(object):
    def __init__(self, *args, **kwargs):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://192.168.200.1/login.html"

    def login(self):
        pass

    def logout(self):
        pass


    def test_no_apple_t_v_mornings(self):
        driver = self.driver
        driver.get("http://192.168.200.1/login.html")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("b@s@r@ngu")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Remember my login info.'])[1]/following::input[1]").click()
        driver.find_element_by_link_text("Advanced").click()
        driver.find_element_by_link_text("Parental Control").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Parental Control -- Block MAC Address'])[1]/following::input[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='d0:4f:7e:1b:b0:f7'])[1]/following::input[1]").click()
        driver.find_element_by_id("editTod").click()
        driver.find_element_by_id("strTimeHr").click()
        driver.find_element_by_id("strTimeMin").click()
        driver.find_element_by_id("endTimeHr").click()
        driver.find_element_by_id("endTimeMin").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)=':'])[8]/following::input[3]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        driver.find_element_by_link_text("Logout").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Logout'])[1]/following::input[1]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("b@s@r@ngu")
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
