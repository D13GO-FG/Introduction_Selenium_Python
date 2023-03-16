import json

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture
def config(scope='session'):
    # Read the file
    with open('config.json') as config_file:
        config = json.load(config_file)
    # Assert values are acceptable
    assert config['browser'] in ['Firefox', 'Edge', 'Headless firefox']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0
    # Return config so it can be used
    return config


@pytest.fixture
def browser(config):
    # Initialize the WebDriver instance
    if config['browser'] == 'Firefox':
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    elif config['browser'] == 'Edge':
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
    elif config['browser'] == 'Headless firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')

    # Make its calls wait for elements to appear
    driver.implicitly_wait(config['implicit_wait'])

    # Return the WedDriver instance for the setup
    yield driver

    # Quit the WebDriver instance for the cleanup
    driver.quit()


@pytest.fixture()
def setup(browser):
    # Initialize the Driver instance by browser
    if browser == 'edge':
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        print("Launching chrome browser.........")
    elif browser == 'firefox':
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        print("Launching firefox browser.........")
    elif browser == 'brave':
        driver = webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()))
        print("Launching brave browser.........")
    # Make its calls wait up to 10 seconds for element to appear
    driver.implicitly_wait(10)
    # Return the WedDriver instance for the setup
    yield driver
    # Quite the WebDriver instance for the cleanup
    driver.quit()

    return driver


# def pytest_addoption(parser):  # This will get the value from CLI /hooks
#     parser.addoption("--browser")
#
#
# @pytest.fixture()
# def browser(request):  # This will return the Browser value to set up method
#     return request.config.getoption("--browser")
