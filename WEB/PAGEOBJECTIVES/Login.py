from selenium.webdriver.common.by import By

class Login:
    """PAGEOBJECTIVES"""

    USERNAME_TXT_XPATH="XXXXXXXXXX"
    PASSWORD_TXT_XPATH="XXXXXXXXXX"
    LOGIN_BTN_XPATH="XXXXXXXXXX"
    


    "METHODS"
    def __init__(self,driver):
        self.driver=driver

    def Sent_username(self,username):
        self.driver.find_element(By.XPATH, value=self.USERNAME_TXT_XPATH).click()
        self.driver.find_element(By.XPATH, value=self.USERNAME_TXT_XPATH).send_keys(username)

    def Sent_password(self,password):
        self.driver.find_element(By.XPATH, value=self.PASSWORD_TXT_XPATH).click()
        self.driver.find_element(By.XPATH, value=self.PASSWORD_TXT_XPATH).send_keys(password)

