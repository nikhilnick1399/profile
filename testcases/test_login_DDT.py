import time

from pageobjects.LoginPage import Login
from utilities.Xlutils import readdata
from utilities.readproperties import Readconfig
from utilities.customlogger import Loggen
from utilities import Xlutils


class TestLogin001:
    baseURL = Readconfig.getappURL()

    logger = Loggen.get_logger()
    path = r"C:\Users\nikhi\PycharmProjects\framework1\testdata\test_data.xlsx"

    def test_login_ddt(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(5)
        self.driver.get(self.baseURL)
        list=[]
        self.lp = Login(self.driver)
        self.rowcount = Xlutils.getrowcount(self.path, "Sheet1")

        for r in range(2, self.rowcount + 1):

            self.username = Xlutils.readdata(self.path, "Sheet1", r, 1)
            self.password = Xlutils.readdata(self.path, "Sheet1", r, 2)
            self.exp = Xlutils.readdata(self.path, "Sheet1", r, 3)

            self.lp.setusername(self.username)
            self.lp.setpassword(self.password)
            self.lp.clicklogin()
            time.sleep(2)
            act_title = self.driver.title

            if act_title == "Dashboard / nopCommerce administration":

                print(" test passed")
                assert True
                list.append("pass")
                self.lp.clicklogout()

            else:
                # self.driver.save_screenshot(
                #     r"C:\Users\nikhi\PycharmProjects\framework1\screenshots\screenshot" + "test_login.png")
                print("test failed")
                list.append("fail")

        if "fail" in list:
            assert False

        self.driver.close()

# other way
#         assert 'Dashboard  nopCommerce administration' in act_title
