# Source: https://applitools.com/tutorials/selenium-python.html
import os
import pytest
from applitools.selenium import (
    logger,
    FileLogger,
    VisualGridRunner,
    Eyes,
    BatchInfo,
    BrowserType,
    DeviceName,
    ScreenOrientation,
)
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

batch_info = BatchInfo("Holiday Shopping")


def eyes_setup(runner):
    eyes = Eyes(runner)
    logger.set_logger(FileLogger("mostrecent.log", mode="w"))
    # Initialize the eyes SDK and set your private API key.
    eyes.api_key = os.environ["APPLITOOLS_KEY"]
    return eyes


@pytest.fixture(name="chrome_eyes", scope="function")
def chrome_eyes_setup(runner):
    """
    Basic Eyes setup for Chrome browser only. It'll abort test if not closed properly.
    """
    eyes = eyes_setup(runner)

    # Set batch info for all tasks
    #  Add desired browser and viewport
    eyes.configure.set_batch(batch_info)
    (
        eyes.configure.add_browser(1200, 800, BrowserType.CHROME)
    )
    yield eyes
    # If the test was aborted before eyes.close was called, ends the test as aborted.
    eyes.abort()


@pytest.fixture(name="cross_browser_eyes", scope="function")
def all_eyes_setup(runner):
    """
    Basic Eyes setup for multiple browsers. It'll abort test if not closed properly.
    """
    eyes = eyes_setup(runner)

    # Set batch info for all tasks
    #  Add desired browsers and viewports
    #  Add mobile emulation device in Portrait mode
    eyes.configure.set_batch(batch_info)
    (
        eyes.configure.add_browser(1200, 800, BrowserType.CHROME)
        .add_browser(1200, 800, BrowserType.FIREFOX)
        .add_browser(1200, 800, BrowserType.EDGE_CHROMIUM)
        .add_browser(1200, 800, BrowserType.SAFARI)
        .add_device_emulation(DeviceName.iPhone_X, ScreenOrientation.PORTRAIT)
    )
    yield eyes
    # If the test was aborted before eyes.close was called, ends the test as aborted.
    eyes.abort()


@pytest.fixture(name="driver", scope="function")
def driver_setup():
    """
    New browser instance per test and quit.
    """
    driver = webdriver.Chrome(ChromeDriverManager().install())
    yield driver
    # Close the browser.
    driver.quit()


@pytest.fixture(name="runner", scope="session")
def runner_setup():
    """
    One test runner for all tests. Print test results at the end of execution.
    """
    runner = VisualGridRunner(10)
    yield runner
    all_test_results = runner.get_all_test_results()
    print(all_test_results)
