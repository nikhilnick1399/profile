import configparser
config = configparser.ConfigParser()
config.read(r"C:\Users\nikhi\PycharmProjects\framework1\configuration\config.ini")

class Readconfig:
    @staticmethod
    def getappURL():
        url = config.get("common_info","baseURL")

        return url

    @staticmethod
    def getusername():
        username = config.get("common_info", "username")

        return username

    @staticmethod
    def getpassword():
        password = config.get("common_info", "password")

        return password