from selenium.webdriver.common.by import By

from .page_element import PageElement
from .base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, driver.current_url)
        self.driver = driver

    @property
    def to_investors_section(self):
        return PageElement(self.driver,
            "//a[contains(@class, 'js-menu-opener') "
            "and contains(text(), 'Инвесторам')]"
        )

    @property
    def jewelery_section(self):
        return PageElement(self.driver,
            "//a[contains(@class, 'js-menu-opener') "
            "and contains(text(), 'Ювелирные украшения')]"
        )

    @property
    def jewelery_section_2(self):
        return By.XPATH, "//a[contains(@class, 'js-menu-opener') " \
                         "and contains(text(), 'Ювелирные украшения')]"

    @property
    def results_and_reports_section(self):
        return PageElement(self.driver,
            "//span[contains(text(), ' Результаты и отчеты ')]"
        )

    @property
    def buy_online_section(self):
        return PageElement(self.driver,
            "//a[contains(text(), ' Приобрести в интернете ')]"
        )

    @property
    def chapter_title(self):
        return PageElement(self.driver,
            """//div[contains(@class, 'ar-news-media__block-item')]
            //child::a[contains(@class, 'ar-news-media__title')]"""
        )

    @property
    def bread_scrumb(self):
        return PageElement(self.driver,
            """//div[contains(@class, 'ar-section__content ar-breadcrumbs__content')]
            //child::a[contains(@class, 'ar-breadcrumbs__item')]"""
        )

    @property
    def main_page_button(self):
        return PageElement(self.driver,
            "//a[contains(text(), 'Главная')]"
        )

    @property
    def alrosadiamond_tab(self):
        return PageElement(self.driver,
            "//a[contains(text(), 'alrosadiamond.ru')]"
        )

    @property
    def count_in_cart(self):
        return PageElement(self.driver,
            """//a[contains(@class, 'header__cart')]//child::span"""
        )

