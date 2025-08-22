from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import unittest

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from ..pages.loginpages import LoginPage
#from sample_project.page_object_model_project.pages.loginpages import LoginPage

class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        return super().setUp(self)
    
    def test_login_valid(self):
        driver = self.driver

        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        login =LoginPage(driver)
        login.enter_username("Adimin")
        login.enter_password("admin123")
        login.click_login()
        #self.driver.find_element(By.NAME, "username").send_keys("Admin")
        #self.driver.find_element(By.NAME, "password").send_keys("admin123")
        #self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        #self.driver.find_element(By.CLASS_NAME, "oxd-userdropdown-img").click()
        #self.driver.find_element(By.LINK_TEXT, "Logout").click()
        time.sleep(2)
    

    @classmethod
    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("test finish")
        return super().tearDown(self)


if __name__ == '__main__':
    unittest.main()







