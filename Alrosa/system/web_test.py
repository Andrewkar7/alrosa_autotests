import allure

from allure_commons.types import AttachmentType
from selenium.webdriver.remote.webdriver import WebDriver

from system.web_flows import main_flow as flow


@allure.feature('Test №1')
def test_1(driver: WebDriver):
    try:
        flow.go_to_investors_page(driver)
        flow.go_to_results_and_reports_page(driver)
        bread_scrumbs = flow.get_bread_scrumbs_list(driver)
        exp_bread_scrumbs = ['Главная', 'Инвесторам', 'Результаты и отчеты']
        assert bread_scrumbs == exp_bread_scrumbs
        chapters = flow.get_chapters_list(driver)
        print(chapters)
        exp_chapters = ['IR-релизы', 'Финансовые результаты', 'Операционные результаты',
                        'Результаты продаж', 'Годовые отчеты', 'ESG отчеты', 'Прогноз']
        for chap in exp_chapters:
            assert chap in chapters
        flow.go_to_main_page(driver)
    except:
        with allure.step('Делаем скриншот'):
            allure.attach(driver.get_screenshot_as_png(), name='Screenshot',
                          attachment_type=AttachmentType.PNG)
        raise


@allure.feature('Test №2')
def test_2(driver: WebDriver):
    try:
        flow.point_on_jewelery_chapter(driver)
        flow.go_to_buy_online_page(driver)
        flow.go_to_alrosadiamond(driver)
        driver.switch_to.window(driver.window_handles[1])
        assert driver.current_url == "https://alrosadiamond.ru/"
        count = flow.check_count_in_cart(driver)
        assert int(count) == 0
    except:
        with allure.step('Делаем скриншот'):
            allure.attach(driver.get_screenshot_as_png(), name='Screenshot',
                          attachment_type=AttachmentType.PNG)
        raise
