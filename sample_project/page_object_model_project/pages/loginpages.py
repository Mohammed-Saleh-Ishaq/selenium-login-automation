from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        # Element locators
        self.username_input = (By.NAME, "username")
        self.password_input = (By.NAME, "password")
        self.submit_button = (By.XPATH, "//button[@type='submit']")

    def enter_username(self, username):
        self.driver.find_element(*self.username_input).clear()

        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).clear()

        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.submit_button).click()
