
import pytest
from selenium import webdriver
import time

from pageobjects.LoginPage import Login
from utilities.readproperties import Readconfig
from utilities.customlogger import Loggen

class TestLogin001:
    baseURL = Readconfig.getappURL()
    username = Readconfig.getusername()
    password = Readconfig.getpassword()
    # logger = Loggen.get_logger()
    logger =Loggen.get_logger()


    def test_homepagetile(self,setup):
        self.logger.info("*****TestLogin001*****")
        self.logger.info("*****verifying home pape title*****")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title


        if act_title == "nopCommerce demo store. Login":
            assert True
            self.logger.info("*****Test passed*****")
        else:
            assert False


    def test_login(self,setup):
        self.driver = setup

        self.driver.get(self.baseURL)

        self.lp = Login(self.driver)
        self.lp.setusername(self.username)

        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        act_title = self.driver.title
        # self.lp.clicklogout()

        if act_title == "Dashboard / nopCommerce administration" :
            assert True
        else :
            time.sleep(2)

            self.driver.save_screenshot(r"C:\Users\nikhi\PycharmProjects\framework1\screenshots\screenshot" + "test_login.png")
            self.driver.close()
            assert False

# other way
#         assert 'Dashboard  nopCommerce administration' in act_title

