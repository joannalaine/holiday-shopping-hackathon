import pytest

from applifashion.pages.store_page import StorePage

PAGE = "tlcHackathonMasterV1.html"


@pytest.mark.part1
def test_1(driver, chrome_eyes):
    store_page = StorePage(driver, PAGE)
    store_page.open()
    store_page.visual_check(chrome_eyes, test="Test 1", step="main page")


@pytest.mark.part1
def test_2(driver, chrome_eyes):
    store_page = StorePage(driver, PAGE)
    store_page.open()
    store_page.filter_by("Black")
    store_page.visual_check(chrome_eyes, test="Test 2", step="filter by color", region=store_page.PRODUCT_GRID)


@pytest.mark.part1
def test_3(driver, chrome_eyes):
    store_page = StorePage(driver, PAGE)
    store_page.open()
    store_page.choose_product("Appli Air x Night")
    store_page.visual_check(chrome_eyes, test="Test 3", step="product details")
