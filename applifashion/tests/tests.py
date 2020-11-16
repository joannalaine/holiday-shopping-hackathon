from applitools.selenium import Eyes
from selenium.webdriver.chrome.webdriver import WebDriver

from applifashion.pages.store_page import StorePage


def task_1(driver: WebDriver, page: str, eyes: Eyes):
    store_page = StorePage(driver, page)
    store_page.open()
    store_page.visual_check(eyes, test="Test 1", step="main page")


def task_2(driver: WebDriver, page: str, eyes: Eyes):
    store_page = StorePage(driver, page)
    store_page.open()
    store_page.filter_by("Black")
    store_page.visual_check(eyes, test="Test 2", step="filter by color", region=store_page.PRODUCT_GRID)


def task_3(driver: WebDriver, page: str, eyes: Eyes):
    store_page = StorePage(driver, page)
    store_page.open()
    store_page.choose_product("Appli Air x Night")
    store_page.visual_check(eyes, test="Test 3", step="product details")
