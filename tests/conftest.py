import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def driver(request):
    browse = request.config.getoption("--browser")
    if browse == "chrome":
        driver = webdriver.Chrome()
    elif browse == "firefox":
        driver = webdriver.Firefox()
    elif browse == "safari":
        driver = webdriver.Safari()
    else:
        raise TypeError(f"'{browse}' is not supported. Expected chrome, firefox or safari.")

    yield driver

    driver.close()
    driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="firefox", help="Browsers for running tests: chrome, firefox or safari"
    )