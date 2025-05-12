import configparser

config = configparser.RawConfigParser()
config.read(".\\configuration\\config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseurl')
        return url

    @staticmethod
    def getApplicationUsername():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getApplicatipassword():
        password = config.get('common info', 'password')
        return password
