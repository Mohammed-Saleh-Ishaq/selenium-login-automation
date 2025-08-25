from selenium.webdriver.common.action_chains import ActionChains
from sample_project.page_object_model_project.locators.locator import Locators

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        #self.welcome_link = (By.CLASS_NAME, "oxd-userdropdown-img")
        #self.logout_link = (By.LINK_TEXT, "Logout")

    def click_welcome(self):
        welcome_element = self.driver.find_element(*Locators.welcome_link)
        ActionChains(self.driver).move_to_element(welcome_element).click().perform()

    def click_logout(self):
        self.click_welcome()  # Ensure the dropdown is open
        logout_element = self.driver.find_element(*Locators.logout_link)
        logout_element.click()
