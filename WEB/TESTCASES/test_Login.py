#  pytest -v -s --html=Reports/test_Login.html --self-contained-html TESTCASES/test_Login.py --browser Chrome
#  pytest -v -s TESTCASES/test_Login.py --browser Firefox
#  pytest -v -s TESTCASES/test_Login.py --browser Chrome



#import Statements
from PAGEOBJECTIVES.Login import Login
from UTIL.readproperties import ReadConfig
from HELPER.helper import HELPER

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest
import inspect

BASEURL = ReadConfig.get_BaseURL()
USERNAME = ReadConfig.get_USERNAME()
PASSWORD = ReadConfig.get_PASSWORD()
ADMIN_EMAIL_ID = ReadConfig.get_ADMIN_EMAIL()
ADMIN_LOGIN_SUCCESS_EXPECTED_URL = ReadConfig.get_ADMIN_Login_success_EXPECTED_URL()
ADMIN_FORGET_PASSWORD_URL = ReadConfig.get_ADMIN_Forgetpassword_URL()




##Message validations In page

Partner_Invalid_login_msg1_XPATH="//*[text()='This field is required']"
Partner_Invalid_login_msg2_XPATH="//*[text()='Invalid login credentials.']"



class Test_login:

    @pytest.mark.run(order=1)
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Login_success(self,setup):
        self.driver = setup
        self.driver.get(BASEURL)

        #ClassObjects
        self.LO=Login(self.driver)


        #Testcases Starts Here
        self.LO.Sent_username(USERNAME)
        self.LO.Sent_password(PASSWORD)
        self.LO.Click_signin()

        try:
            WebDriverWait(self.driver, 10).until(EC.url_to_be(ADMIN_LOGIN_SUCCESS_EXPECTED_URL))  # Wait for the next page to load
            self.driver.close()
            assert True
        except:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            HELPER.TAKE_SCREENSHOT(self, FunName)
            assert False


    @pytest.mark.run(order=2)
    @pytest.mark.regression
    def test_Login_failed_with_no_input(self,setup):
        self.driver = setup
        self.driver.get(BASEURL)
        #ClassObjects
        self.LO=Login(self.driver)

        #Testcases Starts Here

        self.LO.Sent_username("")
        self.LO.Sent_password("")
        self.LO.Click_signin()

        try:
            self.driver.find_element(By.XPATH, value= Partner_Invalid_login_msg1_XPATH)
            try:
                WebDriverWait(self.driver, 5).until(EC.url_to_be(ADMIN_LOGIN_SUCCESS_EXPECTED_URL))  # Wait for the next page to load
                # To take the Screenshote
                FunName = inspect.currentframe().f_code.co_name
                HELPER.TAKE_SCREENSHOT(self, FunName)
                assert False
            except:
                self.driver.close()
                assert True
        except:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            HELPER.TAKE_SCREENSHOT(self, FunName)
            assert False
