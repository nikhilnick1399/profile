
from selenium import webdriver

from selenium.webdriver.common.by import By


class Login:
    textbox_username_id = "//input[@id='Email']"
    textbox_password_id = "//input[@id='Password']"
    button_login_xpath = "//button[normalize-space()='Log in']"
    logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver


    def setusername(self,username):
        self.driver.find_element(By.XPATH,self.textbox_username_id).clear()
        self.driver.find_element(By.XPATH,self.textbox_username_id).send_keys(username)

    def setpassword(self,password):
        self.driver.find_element(By.XPATH, self.textbox_password_id).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_id).send_keys(password)

    def clicklogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clicklogout(self):
        self.driver.find_element(By.LINK_TEXT,self.logout_linktext).click()

