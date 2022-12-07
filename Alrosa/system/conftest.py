import os
import pytest

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

stages = {
    "prod": "https://alrosa.ru/"
}


def pytest_addoption(parser):
    parser.addoption(
        "--platform",
        action="store",
        default="chrome"
    )
    parser.addoption(
        "--stage",
        action="store",
        default="prod"
    )
    parser.addoption(
        "--binpath",
        action="store",
        default=os.getcwd() + "/system/drivers/chromedriver"
    )
    parser.addoption(
        "--headless",
        action="store",
        default=False
    )
    parser.addoption(
        "--tabs",
        action="store",
        default=False
    )
    parser.addoption(
        "--proxy",
        action="store",
        default=None
    )


def pytest_generate_tests(metafunc):
    if 'driver_path' in metafunc.fixturenames:
        metafunc.parametrize(
            'driver_path',
            [metafunc.config.getoption('binpath')],
            scope='session'
        )
    if 'host' in metafunc.fixturenames:
        metafunc.parametrize(
            'host',
            [stages.get(metafunc.config.getoption('stage'))],
            scope='session'
        )


def determine_driver_scope(fixture_name, config):
    if config.getoption("--tabs"):
        return "session"
    return "function"


@pytest.fixture(scope=determine_driver_scope)
def driver_factory():
    drivers = []

    def _create_driver(
            driver_path, host):
        options = webdriver.ChromeOptions()
        options.add_argument('--window-size=1920,1080')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(
            executable_path=driver_path, options=options)
        driver.implicitly_wait(15)
        driver.get(host)
        drivers.append(driver)
        return driver

    yield _create_driver
    for driver in drivers:
        driver.quit()


@pytest.fixture(scope=determine_driver_scope)
def driver_init_args(driver_path, host):
    return [driver_path, host]


@pytest.fixture(scope=determine_driver_scope)
def driver(driver_factory, driver_init_args):
    return driver_factory(*driver_init_args)


class LocalStorage():

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def set(self, key, value):
        self.driver.execute_script("window.localStorage.setItem(arguments[0], arguments[1]);", key, value)

    def clear(self):
        self.driver.execute_script("window.localStorage.clear();")


@pytest.fixture(scope="function", autouse=True)
def to_localstorage(driver):
    storage = LocalStorage(driver)
    storage.set('var', 10)
    yield
    storage.clear()
