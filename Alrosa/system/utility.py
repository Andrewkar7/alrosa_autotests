from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common import exceptions


def wait_until_clickable(driver: WebDriver, xpath, timeout):
    driver.implicitly_wait(0)
    try:
        WebDriverWait(driver, timeout, 1).until(
            method=EC.visibility_of_element_located((By.XPATH, xpath)),
            message="element is not visible: " + xpath)
        WebDriverWait(driver, timeout, 1).until(
            method=EC.element_to_be_clickable((By.XPATH, xpath)),
            message="element is not clickable: " + xpath)
    except exceptions.TimeoutException:
        driver.implicitly_wait(4)
        return False
    driver.implicitly_wait(4)
    return True


def scroll_into_view(driver: WebDriver, element):
    driver.execute_script(
        "arguments[0].scrollIntoView(true);", element
    )
