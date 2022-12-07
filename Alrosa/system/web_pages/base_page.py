from selenium.webdriver.remote.webdriver import WebDriver


class BasePage():
    def __init__(self, driver: WebDriver, host):
        self.driver = driver
        self.host = host
