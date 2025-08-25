from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import unittest
import HtmlTestRunner
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#import sys
#import os
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
#from ..pages.loginpages import LoginPage
#from .pages.homepage import HomePage

from sample_project.page_object_model_project.pages.loginpages import LoginPage
from sample_project.page_object_model_project.pages.homepage import HomePage

class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        #return super().setUp(self)
    
    def test_01_login_valid(self):
        driver = self.driver

        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        login =LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homePage = HomePage(driver)
        homePage.click_welcome()
        homePage.click_logout()
        #self.driver.find_element(By.NAME, "username").send_keys("Admin")
        #self.driver.find_element(By.NAME, "password").send_keys("admin123")
        #self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        #self.driver.find_element(By.CLASS_NAME, "oxd-userdropdown-img").click()
        #self.driver.find_element(By.LINK_TEXT, "Logout").click()
        time.sleep(2)
    
    def test_02_invalid_username(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        
        login =LoginPage(driver)
        login.enter_username("wrong user") # Invalid username
        login.enter_password("admin123")
        #message = driver.find_element_by((By.CLASS_NAME, "oxd-alert-content-text"))
        #self.assertEqual(message, "invalid credential bhai")
        login.click_login()
        
        # Wait for error message to appear
        wait = WebDriverWait(driver, 10)
        error_element = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "oxd-alert-content-text"))
    )
        

        actual_message = error_element.text.strip()
        expected_message = "Invalid credentials"
        self.assertEqual(actual_message, expected_message)

        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        #self.driver.close()
        cls.driver.quit()
        print("test finish")
        #return super().tearDown(self)


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/hutaz/Desktop/selenium_project/reports'))


#import sample_project.page_object_model_project.pages.homepage as hp
#print(hp.__file__)





