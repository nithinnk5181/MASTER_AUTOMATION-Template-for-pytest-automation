#import Statements

from WEB.PAGEOBJECTIVES.Login import Login
from UTIL.readproperties import ReadConfig

import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import inspect
import string
import random


"""CONFIGURATIONS"""

BASEURL = ReadConfig.get_BaseURL()
USERNAME = ReadConfig.get_USERNAME()
PASSWORD = ReadConfig.get_PASSWORD()
ADMIN_EMAIL_ID = ReadConfig.get_ADMIN_EMAIL()
ADMIN_LOGIN_SUCCESS_EXPECTED_URL = ReadConfig.get_ADMIN_Login_success_EXPECTED_URL()
ADMIN_FORGET_PASSWORD_URL = ReadConfig.get_ADMIN_Forgetpassword_URL()


class HELPER:

    @staticmethod
    def TAKE_SCREENSHOT(self,Methodname):
        # To take the Screenshot
        now = datetime.datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        #date_stamp = str(datetime.dat
        # etime.now()).split('//')[1].split('.')[0]
        filename = "NBFC_"+dt_string
        self.driver.save_screenshot("C:/Users/NITHIN/PycharmProjects/NBFC/Screenshots/"+Methodname+".png")

    @staticmethod
    def random_generator(size=7, chars=string.ascii_uppercase):
        return ''.join(random.choice(chars) for x in range(7))

    @staticmethod
    def random_generator_10char(size=10, chars=string.ascii_uppercase):
        return ''.join(random.choice(chars) for x in range(10))

    @staticmethod
    def random_generator_4char(size=4, chars=string.ascii_uppercase):
        return ''.join(random.choice(chars) for x in range(4))

    @staticmethod
    def random_generator_mobile_num(size=10, chars=string.digits):
        return ''.join(random.choice(chars) for x in range(10))

    @staticmethod
    def random_generator_mobile_num_12dig(size=12, chars=string.digits):
        return ''.join(random.choice(chars) for x in range(12))


    #Admin Login
    @staticmethod
    def Admin_login_success(self,setup):
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

        except:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            HELPER.TAKE_SCREENSHOT(self, FunName)
            assert False
