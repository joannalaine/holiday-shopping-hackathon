import pytest

from applifashion.tests.tests import task_1, task_2, task_3

PAGE = "tlcHackathonMasterV2.html"


@pytest.mark.part3
def test_1(driver, cross_browser_eyes):
    task_1(driver, PAGE, cross_browser_eyes)


@pytest.mark.part3
def test_2(driver, cross_browser_eyes):
    task_2(driver, PAGE, cross_browser_eyes)


@pytest.mark.part3
def test_3(driver, cross_browser_eyes):
    task_3(driver, PAGE, cross_browser_eyes)
