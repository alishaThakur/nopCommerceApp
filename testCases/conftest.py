import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

@pytest.fixture()
def setup(browser):
    serv_obj = Service("C:\Drivers\chromedriver_win32 (1)\chromedriver.exe")
    driver = webdriver.Chrome(service=serv_obj)
    if browser == 'chrome':
        driver = webdriver.Chrome(service=serv_obj)
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome(service=serv_obj)
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

############### Pytest HTML Report ################

# For adding environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = "Customers"
    config._metadata['Tester'] = 'Alisha'

# To modify/delete Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)