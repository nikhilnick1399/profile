import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
        print("launching chrome browser")
    elif browser=="firefox":
        driver =webdriver.Firefox()
    else:
       driver =webdriver.Chrome()
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

def pytest_configure(config):
    metadata = getattr(config,"_metadata",None)
    if metadata is not None:
        metadata["Project name"]= "no commerce"
        metadata["Module name"] = "customers"
        metadata["Tester"] = "nikhil"
