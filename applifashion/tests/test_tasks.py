from applitools.selenium import Eyes
from selenium.webdriver.chrome.webdriver import WebDriver

from applifashion.pages.store_page import StorePage


def task_1(driver: WebDriver, page: str, eyes: Eyes):
    """
    Check the main page of the app by using Applitools Eyes to take a screenshot of the entire page.

    :param driver: Selenium Chrome WebDriver pytest fixture
    :param page: Path of webpage under test
    :param eyes: Applitools Eyes pytest fixture
    """
    store_page = StorePage(driver, page)
    store_page.open()
    store_page.visual_check(eyes, test="Test 1", step="main page")


def task_2(driver: WebDriver, page: str, eyes: Eyes):
    """
    Filter the results on the main page by the color black. Use Applitools Eyes’ Check Region feature to capture only a
    screenshot of the shoes grid and verify that only two black shoes appear.

    :param driver: Selenium Chrome WebDriver pytest fixture
    :param page: Path of webpage under test
    :param eyes: Applitools Eyes pytest fixture
    """
    store_page = StorePage(driver, page)
    store_page.open()
    store_page.filter_by("Black")
    store_page.visual_check(eyes, test="Test 2", step="filter by color", region=store_page.PRODUCT_GRID)


def task_3(driver: WebDriver, page: str, eyes: Eyes):
    """
    Without filtering, click on the Appli Air x Night shoe. Use Applitools to take a screenshot of the entire page to
    verify all of the details about the product.

    :param driver: Selenium Chrome WebDriver pytest fixture
    :param page: Path of webpage under test
    :param eyes: Applitools Eyes pytest fixture
    """
    store_page = StorePage(driver, page)
    store_page.open()
    store_page.choose_product("Appli Air x Night")
    store_page.visual_check(eyes, test="Test 3", step="product details")
