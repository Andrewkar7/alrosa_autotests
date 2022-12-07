import system.utility as ut
import lxml.html as htree

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from io import StringIO


class PageElement():
    def __init__(self, driver: WebDriver, xpath):
        self._driver = driver
        self._xpath = xpath

    @property
    def webelement(self):
        return self._driver.find_element(By.XPATH, self._xpath)

    @property
    def text(self):
        return self.webelement.text

    @property
    def html_element(self):
        source = self._driver.page_source
        tree = htree.parse(StringIO(source))
        return tree.xpath(self._xpath)[0]

    @property
    def html_element_list(self):
        source = self._driver.page_source
        tree = htree.parse(StringIO(source))
        return tree.xpath(self._xpath)

    def click(self):
        return self.webelement.click()

    def wait_until_clickable(self, timeout):
        return ut.wait_until_clickable(self._driver, self._xpath, timeout)

    def scroll_into_view(self):
        ut.scroll_into_view(self._driver, self.webelement)
