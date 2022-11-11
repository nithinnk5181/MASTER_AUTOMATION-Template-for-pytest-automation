import configparser

config=configparser.RawConfigParser()
config.read("/home/niithin/Downloads/AUTOMATION_PROJECTS/NBFC_WEB/CONFIG/config.ini")


class ReadConfig():

    ###ADMIN###
    @staticmethod
    def get_BaseURL():
        URL=config.get('WEB','BASEURL')
        return URL

    @staticmethod
    def get_USERNAME():
        USR=config.get('WEB','USERNAME')
        return USR
    
    @staticmethod
    def get_PASSWORD():
        PASS=config.get('WEB','PASSWORD')
        return PASS





    @staticmethod
    def get_ADMIN_EMAIL():
        email = config.get('WEB', 'EMAIL')
        return email

    @staticmethod
    def get_ADMIN_Login_success_EXPECTED_URL():
        URL = config.get('WEB', 'LOGIN_EXPECTED_URL')
        return URL

    @staticmethod
    def get_ADMIN_Forgetpassword_URL():
        URL = config.get('WEB', 'FORGET_PASSWORD_URL')
        return URL