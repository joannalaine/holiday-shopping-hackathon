import pytest

from applifashion.pages.store_page import StorePage

PAGE = "tlcHackathonMasterV2.html"


@pytest.mark.part3
def test_1(driver, cross_browser_eyes):
    store_page = StorePage(driver, PAGE)
    store_page.open()
    store_page.visual_check(cross_browser_eyes, test="Test 1", step="main page")


@pytest.mark.part3
def test_2(driver, cross_browser_eyes):
    store_page = StorePage(driver, PAGE)
    store_page.open()
    store_page.filter_by("Black")
    store_page.visual_check(cross_browser_eyes, test="Test 2", step="filter by color", region=store_page.PRODUCT_GRID)


@pytest.mark.part3
def test_3(driver, cross_browser_eyes):
    store_page = StorePage(driver, PAGE)
    store_page.open()
    store_page.choose_product("Appli Air x Night")
    store_page.visual_check(cross_browser_eyes, test="Test 3", step="product details")
