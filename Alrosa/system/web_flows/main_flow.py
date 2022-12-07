from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from system.web_pages.main_page import MainPage

TIMEOUT_NORM = 30


def go_to_investors_page(driver):
    page = MainPage(driver)
    page.to_investors_section.wait_until_clickable(TIMEOUT_NORM)
    page.to_investors_section.click()
    assert driver.current_url.endswith('/investors/')


def go_to_results_and_reports_page(driver):
    page = MainPage(driver)
    page.results_and_reports_section.wait_until_clickable(TIMEOUT_NORM)
    page.results_and_reports_section.click()
    assert driver.current_url.endswith('/results-reports/')


def get_chapters_list(driver):
    page = MainPage(driver)
    chapters_list = [
        e.text_content()
        for e in page.chapter_title.html_element_list
    ]
    chapters_list = [x.replace('\n', '') for x in chapters_list]
    chapters_list = [x.strip() for x in chapters_list]
    return chapters_list


def get_bread_scrumbs_list(driver):
    page = MainPage(driver)
    bread_scrumbs_list = [
        e.text_content()
        for e in page.bread_scrumb.html_element_list
    ]
    return bread_scrumbs_list


def go_to_main_page(driver):
    page = MainPage(driver)
    page.main_page_button.wait_until_clickable(TIMEOUT_NORM)
    page.main_page_button.click()
    assert driver.current_url == 'https://alrosa.ru/'


def point_on_jewelery_chapter(driver):
    page = MainPage(driver)
    page.jewelery_section.wait_until_clickable(TIMEOUT_NORM)
    actions = ActionChains(driver)
    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(page.jewelery_section_2))
    actions.move_to_element(element).perform()


def go_to_buy_online_page(driver):
    page = MainPage(driver)
    page.buy_online_section.wait_until_clickable(TIMEOUT_NORM)
    page.buy_online_section.click()
    assert driver.current_url.endswith('/buy-online/')


def go_to_alrosadiamond(driver):
    page = MainPage(driver)
    page.alrosadiamond_tab.wait_until_clickable(TIMEOUT_NORM)
    page.alrosadiamond_tab.scroll_into_view()
    page.alrosadiamond_tab.click()


def check_count_in_cart(driver):
    page = MainPage(driver)
    count = page.count_in_cart.html_element.text_content()
    return count
