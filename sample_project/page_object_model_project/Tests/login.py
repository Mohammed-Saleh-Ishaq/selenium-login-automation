from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import unittest

class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        return super().setUp(self)
    
    def test_login_valid(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.driver.find_element(By.CLASS_NAME, "oxd-userdropdown-img").click()
        self.driver.find_element(By.LINK_TEXT, "Logout").click()
        time.sleep(2)
    

    @classmethod
    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("test finish")
        return super().tearDown(self)


if __name__ == '__main__':
    unittest.main()







