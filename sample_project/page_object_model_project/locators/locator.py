from selenium.webdriver.common.by import By
class Locators:

    # loginpage.py objects
    username_input = (By.NAME, "username")
    password_input = (By.NAME, "password")
    submit_button = (By.XPATH, "//button[@type='submit']")
    
    # Homepage.py objects
    welcome_link = (By.CLASS_NAME, "oxd-userdropdown-img")
    logout_link = (By.LINK_TEXT, "Logout")